#!/usr/bin/env python3
"""将网页转换为 Markdown，并把图片下载到本地。

脚本刻意只使用 Python 标准库，便于在无法安装依赖的受限工作区中运行。
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import html
from html.parser import HTMLParser
import mimetypes
import os
from pathlib import Path
import re
import sys
from typing import Iterable
from urllib.parse import quote, unquote, urljoin, urlparse
from urllib.request import Request, urlopen


VOID_TAGS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

SKIP_TAGS = {
    "script",
    "style",
    "noscript",
    "template",
    "svg",
    "canvas",
    "iframe",
    "form",
}

SKIP_CONTENT_TAGS = {"nav", "footer"}

BLOCK_TAGS = {
    "article",
    "aside",
    "blockquote",
    "body",
    "div",
    "dl",
    "fieldset",
    "figcaption",
    "figure",
    "header",
    "hr",
    "li",
    "main",
    "ol",
    "p",
    "pre",
    "section",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "ul",
}

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0 Safari/537.36"
)

OPENAI_DOCS_HOSTS = {"developers.openai.com"}

COPY_UI_CLASSES = {
    "exclude-from-copy",
    "react-syntax-highlighter-line-number",
    "page-copy-action",
}

HIDDEN_CLASSES = {"hidden", "sr-only"}

PREFERRED_HIDDEN_CODE_LANGUAGES = {
    "bash",
    "javascript",
    "json",
    "plaintext",
    "python",
    "text",
}

LANGUAGE_ALIASES = {
    "cli": "bash",
    "curl": "bash",
    "js": "javascript",
    "node": "javascript",
    "node.js": "javascript",
    "plain": "text",
    "plaintext": "text",
    "shell": "bash",
    "sh": "bash",
    "typescript": "typescript",
}


class Node:
    def __init__(
        self,
        tag: str | None = None,
        attrs: dict[str, str] | None = None,
        text: str | None = None,
        parent: "Node | None" = None,
    ) -> None:
        self.tag = tag
        self.attrs = attrs or {}
        self.text = text or ""
        self.parent = parent
        self.children: list[Node] = []

    def append(self, node: "Node") -> None:
        node.parent = self
        self.children.append(node)


class DOMBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.root = Node("document")
        self.stack = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        node = Node(tag, {k.lower(): v or "" for k, v in attrs})
        self.stack[-1].append(node)
        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if self.stack[-1].tag == tag and tag not in VOID_TAGS:
            self.stack.pop()

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_data(self, data: str) -> None:
        if data:
            self.stack[-1].append(Node(text=data))

    def handle_entityref(self, name: str) -> None:
        self.handle_data(html.unescape(f"&{name};"))

    def handle_charref(self, name: str) -> None:
        self.handle_data(html.unescape(f"&#{name};"))


class ImageStore:
    def __init__(
        self,
        base_url: str,
        output_md: Path,
        assets_dir: Path,
        timeout: int,
        user_agent: str,
        skip_images: bool,
    ) -> None:
        self.base_url = base_url
        self.output_md = output_md
        self.assets_dir = assets_dir
        self.timeout = timeout
        self.user_agent = user_agent
        self.skip_images = skip_images
        self.seen: dict[str, str] = {}
        self.failures: list[str] = []
        self.counter = 0

    def markdown_path_for(self, src: str, alt: str = "") -> str:
        if not src:
            return ""
        absolute = urljoin(self.base_url, src)
        if self.skip_images:
            return absolute
        if absolute in self.seen:
            return self.seen[absolute]
        try:
            rel_path = self._download(absolute, alt)
        except Exception as exc:  # noqa: BLE001 - report best-effort failures.
            self.failures.append(f"{absolute} ({exc})")
            rel_path = absolute
        self.seen[absolute] = rel_path
        return rel_path

    def _download(self, url: str, alt: str) -> str:
        self.counter += 1
        self.assets_dir.mkdir(parents=True, exist_ok=True)
        parsed = urlparse(url)
        if parsed.scheme == "data":
            data, content_type = read_data_uri(url)
            final_url = url
        else:
            headers = {"User-Agent": self.user_agent, "Referer": self.base_url}
            request = Request(url, headers=headers)
            with urlopen(request, timeout=self.timeout) as response:
                data = response.read()
                content_type = response.headers.get("content-type", "").split(";")[0]
                final_url = response.geturl()
        ext = extension_for(final_url, content_type)
        slug = slugify(alt) or slugify(Path(unquote(urlparse(final_url).path)).stem)
        if not slug:
            slug = "image"
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
        filename = f"{self.counter:03d}-{slug[:48]}-{digest}{ext}"
        target = self.assets_dir / filename
        target.write_bytes(data)
        try:
            rel = Path(os.path.relpath(target, self.output_md.parent)).as_posix()
        except ValueError:
            rel = target.as_posix()
        return quote(rel, safe="/._-")


def fetch_url(url: str, timeout: int, user_agent: str) -> tuple[str, bytes, str]:
    local_path = Path(url).expanduser()
    if not urlparse(url).scheme and local_path.exists():
        url = local_path.resolve().as_uri()
    if urlparse(url).scheme == "data":
        data, content_type = read_data_uri(url)
        return url, data, content_type
    request = Request(url, headers={"User-Agent": user_agent})
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("content-type", "")
        final_url = response.geturl()
        data = response.read()
    return final_url, data, content_type


def decode_html(data: bytes, content_type: str) -> str:
    charset_match = re.search(r"charset=([\w.-]+)", content_type, re.I)
    if charset_match:
        try:
            return data.decode(charset_match.group(1), errors="replace")
        except LookupError:
            pass
    head = data[:4096].decode("ascii", errors="ignore")
    meta_match = re.search(r"<meta[^>]+charset=[\"']?([\w.-]+)", head, re.I)
    if meta_match:
        try:
            return data.decode(meta_match.group(1), errors="replace")
        except LookupError:
            pass
    return data.decode("utf-8", errors="replace")


def parse_html(markup: str) -> Node:
    parser = DOMBuilder()
    parser.feed(markup)
    parser.close()
    return parser.root


def iter_nodes(node: Node) -> Iterable[Node]:
    yield node
    for child in node.children:
        yield from iter_nodes(child)


def first_node(root: Node, tag: str) -> Node | None:
    for node in iter_nodes(root):
        if node.tag == tag:
            return node
    return None


def nodes_by_tag(root: Node, tag: str) -> list[Node]:
    return [node for node in iter_nodes(root) if node.tag == tag]


def class_tokens(node: Node) -> set[str]:
    return {token for token in node.attrs.get("class", "").split() if token}


def has_any_class(node: Node, names: set[str]) -> bool:
    return bool(class_tokens(node) & names)


def has_descendant_tag(node: Node, tag: str) -> bool:
    return any(child.tag == tag for child in iter_nodes(node))


def ancestors(node: Node) -> Iterable[Node]:
    current = node.parent
    while current:
        yield current
        current = current.parent


def is_openai_docs_url(url: str) -> bool:
    return urlparse(url).netloc.lower() in OPENAI_DOCS_HOSTS


def is_copy_ui_node(node: Node) -> bool:
    if has_any_class(node, COPY_UI_CLASSES):
        return True
    if "data-page-copy-action" in node.attrs or "data-page-copy-label" in node.attrs:
        return True
    return False


def hidden_without_code(node: Node) -> bool:
    if node.tag == "pre" or has_descendant_tag(node, "pre"):
        return False
    if "hidden" in node.attrs:
        return True
    if node.attrs.get("aria-hidden", "").lower() == "true":
        return True
    return False


def code_sample_title(node: Node) -> str:
    for child in iter_nodes(node):
        if child is node:
            continue
        classes = class_tokens(child)
        if "code-sample-title" in classes or any(
            token.startswith("_title_") for token in classes
        ):
            title = normalize_space(text_content(child))
            if title:
                return title
    return ""


def is_skipped_openai_docs_node(node: Node, base_url: str) -> bool:
    if not is_openai_docs_url(base_url):
        return False
    if "data-content-mode-switch" in node.attrs:
        default_mode = node.attrs.get("data-default", "")
        data_id = node.attrs.get("data-id", "")
        if default_mode and data_id and data_id != default_mode:
            return True
    if "code-sample" in class_tokens(node):
        return code_sample_title(node).lower() == "generate text from a simple prompt"
    return False


def should_skip_node(node: Node, base_url: str) -> bool:
    if node.tag in SKIP_TAGS or node.tag in SKIP_CONTENT_TAGS:
        return True
    if node.tag in {"button", "svg"}:
        return True
    if is_copy_ui_node(node):
        return True
    if hidden_without_code(node):
        return True
    return is_skipped_openai_docs_node(node, base_url)


def text_content(node: Node) -> str:
    if node.tag in SKIP_TAGS or is_copy_ui_node(node):
        return ""
    if node.tag is None:
        return node.text
    return "".join(text_content(child) for child in node.children)


def visible_text_length(node: Node) -> int:
    return len(normalize_space(text_content(node)))


def choose_content(root: Node) -> Node:
    articles = nodes_by_tag(root, "article")
    if articles:
        return max(articles, key=visible_text_length)
    mains = nodes_by_tag(root, "main")
    role_mains = [
        node for node in iter_nodes(root) if node.attrs.get("role", "").lower() == "main"
    ]
    if mains or role_mains:
        return max([*mains, *role_mains], key=visible_text_length)
    candidates = [
        node
        for node in iter_nodes(root)
        if "content" in " ".join(
            [node.attrs.get("id", ""), node.attrs.get("class", "")]
        ).lower()
    ]
    if candidates:
        return max(candidates, key=visible_text_length)
    body = first_node(root, "body")
    return body or root


def document_title(root: Node) -> str:
    h1 = first_node(root, "h1")
    if h1:
        title = normalize_space(text_content(h1))
        if title:
            return title
    title_node = first_node(root, "title")
    if title_node:
        return normalize_space(text_content(title_node))
    return ""


def render_node(node: Node, images: ImageStore, context: dict[str, int | bool]) -> str:
    if node.tag is None:
        return normalize_text(node.text)
    tag = node.tag
    if should_skip_node(node, images.base_url):
        return ""
    if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(tag[1])
        text = strip_markdown(render_children(node, images, context))
        return block(f"{'#' * level} {text}") if text else ""
    if tag == "p":
        text = render_children(node, images, context).strip()
        return block(text) if text else ""
    if tag == "br":
        return "  \n"
    if tag == "hr":
        return "\n\n---\n\n"
    if tag in {"strong", "b"}:
        text = render_children(node, images, context).strip()
        return f"**{text}**" if text else ""
    if tag in {"em", "i"}:
        text = render_children(node, images, context).strip()
        return f"*{text}*" if text else ""
    if tag == "code" and not context.get("in_pre"):
        text = normalize_space(text_content(node))
        return f"`{escape_backticks(text)}`" if text else ""
    if tag == "pre":
        language = code_language(node)
        if should_omit_text_language(node, language, images.base_url):
            language = ""
        if should_skip_code_block(node, language):
            return ""
        code = clean_code_block(text_content(node))
        if not code:
            return ""
        fence = "```"
        while fence in code:
            fence += "`"
        return f"\n\n{fence}{language}\n{code}\n{fence}\n\n"
    if tag == "a":
        href = node.attrs.get("href", "").strip()
        text = render_children(node, images, context).strip() or href
        if not href:
            return text
        target = urljoin(images.base_url, href)
        return f"[{text}]({target})"
    if tag == "img":
        src = image_source(node)
        alt = normalize_space(node.attrs.get("alt", ""))
        if not src:
            return ""
        target = images.markdown_path_for(src, alt)
        return f"![{alt}]({target})"
    if tag == "blockquote":
        rendered = clean_markdown(render_children(node, images, context))
        quoted = "\n".join(f"> {line}" if line.strip() else ">" for line in rendered.splitlines())
        return block(quoted)
    if tag in {"ul", "ol"}:
        return render_list(node, images, context, ordered=(tag == "ol"))
    if tag == "li":
        return render_children(node, images, context).strip()
    if tag == "table":
        return render_table(node, images, context)
    if tag in {"tr", "thead", "tbody", "tfoot"}:
        return render_children(node, images, context)
    if tag in {"th", "td"}:
        return normalize_space(strip_markdown(render_children(node, images, context)))
    if tag in BLOCK_TAGS:
        text = render_children(node, images, context)
        return block(text.strip()) if tag in {"figcaption"} and text.strip() else text
    return render_children(node, images, context)


def render_children(node: Node, images: ImageStore, context: dict[str, int | bool]) -> str:
    parts = [render_node(child, images, context) for child in node.children]
    return join_fragments(parts)


def render_list(
    node: Node,
    images: ImageStore,
    context: dict[str, int | bool],
    ordered: bool,
) -> str:
    depth = int(context.get("list_depth", 0))
    child_context = dict(context)
    child_context["list_depth"] = depth + 1
    items = [child for child in node.children if child.tag == "li"]
    lines: list[str] = []
    for index, item in enumerate(items, start=1):
        marker = f"{index}." if ordered else "-"
        rendered = clean_markdown(render_node(item, images, child_context)).strip()
        if not rendered:
            continue
        rendered_lines = rendered.splitlines()
        indent = "  " * depth
        lines.append(f"{indent}{marker} {rendered_lines[0]}")
        continuation_indent = "  " * (depth + 1)
        for line in rendered_lines[1:]:
            lines.append(f"{continuation_indent}{line}" if line.strip() else "")
    return "\n\n" + "\n".join(lines) + "\n\n" if lines else ""


def render_table(node: Node, images: ImageStore, context: dict[str, int | bool]) -> str:
    rows: list[list[str]] = []
    for row in [child for child in iter_nodes(node) if child.tag == "tr"]:
        cells = [
            render_node(cell, images, context).replace("|", r"\|").strip()
            for cell in row.children
            if cell.tag in {"th", "td"}
        ]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    header = padded[0]
    separator = ["---"] * width
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(separator) + " |",
    ]
    for row in padded[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n\n" + "\n".join(lines) + "\n\n"


def image_source(node: Node) -> str:
    src = node.attrs.get("src", "").strip()
    if src:
        return src
    srcset = node.attrs.get("srcset", "").strip()
    if not srcset:
        return ""
    candidates = [part.strip().split()[0] for part in srcset.split(",") if part.strip()]
    return candidates[-1] if candidates else ""


def code_language(node: Node) -> str:
    for child in iter_nodes(node):
        language = language_from_attrs(child)
        if language:
            return language
    for parent in ancestors(node):
        language = language_from_attrs(parent)
        if language:
            return language
    return ""


def language_from_attrs(node: Node) -> str:
    for attr in ("data-language", "data-lang", "lang"):
        language = node.attrs.get(attr, "").strip().lower()
        if language:
            return normalize_language(language)
    classes = node.attrs.get("class", "")
    match = re.search(r"(?:language|lang)-([\w#+.-]+)", classes)
    if match:
        return normalize_language(match.group(1))
    return ""


def normalize_language(language: str) -> str:
    language = language.strip().lower()
    language = LANGUAGE_ALIASES.get(language, language)
    return language if re.fullmatch(r"[\w#+.-]+", language) else ""


def should_skip_code_block(node: Node, language: str) -> bool:
    if not language:
        return False
    hidden_ancestor = any(has_any_class(parent, HIDDEN_CLASSES) for parent in ancestors(node))
    if hidden_ancestor and language not in PREFERRED_HIDDEN_CODE_LANGUAGES:
        return True
    return False


def should_omit_text_language(node: Node, language: str, base_url: str) -> bool:
    if language != "text":
        return False
    if not is_openai_docs_url(base_url):
        return False
    return not any(
        parent.attrs.get("id") == "content-switcher-prompt-example"
        for parent in ancestors(node)
    )


def clean_code_block(code: str) -> str:
    lines = code.strip("\n").splitlines()
    number_lines = [
        int(line.strip())
        for line in lines
        if re.fullmatch(r"\s*\d+\s*", line)
    ]
    if len(number_lines) >= 2:
        lines = [line for line in lines if not re.fullmatch(r"\s*\d+\s*", line)]
    return "\n".join(lines).strip("\n")


def block(text: str) -> str:
    return f"\n\n{text.strip()}\n\n" if text.strip() else ""


def join_fragments(parts: Iterable[str]) -> str:
    output = ""
    for part in parts:
        if not part:
            continue
        if output and needs_space(output, part):
            output += " "
        output += part
    return output


def needs_space(left: str, right: str) -> bool:
    if left.endswith(("\n", " ", "(", "[", "/", "`")):
        return False
    if right.startswith(("\n", " ", ".", ",", ":", ";", ")", "]", "`")):
        return False
    return True


def normalize_text(text: str) -> str:
    if not text:
        return ""
    if "\n" in text or "\t" in text:
        return re.sub(r"\s+", " ", text)
    return text


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strip_markdown(text: str) -> str:
    return normalize_space(text.replace("\n", " "))


def clean_markdown(markdown: str) -> str:
    markdown = markdown.replace("’", "'").replace("‘", "'")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown)
    return markdown.strip() + "\n"


def escape_backticks(text: str) -> str:
    return text.replace("`", r"\`")


def slugify(value: str) -> str:
    value = html.unescape(value)
    value = re.sub(r"[^\w\s.-]+", "", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "-", value.strip().lower())
    value = value.strip(".-_")
    return value or ""


def slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    path = unquote(parsed.path).rstrip("/")
    if path:
        slug = slugify(Path(path).name)
        if slug:
            return slug
    return slugify(parsed.netloc) or "article"


def looks_like_markdown_path(path: Path) -> bool:
    return path.suffix.lower() in {".md", ".markdown"}


def safe_markdown_filename(filename: str) -> str:
    name = Path(filename).name.strip() or "index.md"
    if not looks_like_markdown_path(Path(name)):
        name = f"{name}.md"
    return name


def resolve_output_paths(
    output_arg: str,
    assets_arg: str | None,
    markdown_filename: str,
    title: str,
    final_url: str,
) -> tuple[Path, Path]:
    output_path = Path(output_arg).expanduser()
    if looks_like_markdown_path(output_path):
        output_md = output_path.resolve()
        assets_dir = (
            Path(assets_arg).expanduser().resolve()
            if assets_arg
            else output_md.with_name(f"{output_md.stem}_assets").resolve()
        )
        return output_md, assets_dir

    article_slug = slugify(title) or slug_from_url(final_url)
    article_dir = (output_path.resolve() / article_slug).resolve()
    output_md = (article_dir / safe_markdown_filename(markdown_filename)).resolve()
    if assets_arg:
        assets_path = Path(assets_arg).expanduser()
        assets_dir = (
            assets_path.resolve()
            if assets_path.is_absolute()
            else (article_dir / assets_path).resolve()
        )
    else:
        assets_dir = (article_dir / "assets").resolve()
    return output_md, assets_dir


def extension_for(url: str, content_type: str) -> str:
    path_ext = Path(urlparse(url).path).suffix.lower()
    if path_ext and len(path_ext) <= 6:
        return path_ext
    if content_type:
        if content_type == "image/svg+xml":
            return ".svg"
        guessed = mimetypes.guess_extension(content_type)
        if guessed:
            return ".jpg" if guessed == ".jpe" else guessed
    return ".bin"


def read_data_uri(uri: str) -> tuple[bytes, str]:
    header, payload = uri.split(",", 1)
    content_type = header[5:].split(";")[0] or "application/octet-stream"
    if ";base64" in header:
        data = base64.b64decode(payload)
    else:
        data = unquote(payload).encode("utf-8")
    return data, content_type


def add_title(markdown: str, title: str) -> str:
    if not title:
        return markdown
    first_heading = re.search(r"^#\s+(.+)$", markdown, flags=re.M)
    if first_heading and normalize_space(first_heading.group(1)).lower() == title.lower():
        return markdown
    return f"# {title}\n\n{markdown.lstrip()}"


def postprocess_markdown(markdown: str, final_url: str) -> str:
    parsed = urlparse(final_url)
    if parsed.netloc.lower() == "developers.openai.com" and parsed.path.endswith(
        "/api/docs/guides/prompt-engineering"
    ):
        markdown = markdown.replace('"Talk like a pirate."', '"${semicolonsDevMsg}"')
        markdown = markdown.replace(
            '"Are semicolons optional in JavaScript?"',
            '"${semicolonsPrompt}"',
        )
    return markdown


def convert(args: argparse.Namespace) -> tuple[Path, Path, list[str]]:
    final_url, data, content_type = fetch_url(args.url, args.timeout, args.user_agent)
    markup = decode_html(data, content_type)
    if args.save_html:
        save_html_path = Path(args.save_html).expanduser().resolve()
        save_html_path.parent.mkdir(parents=True, exist_ok=True)
        save_html_path.write_text(markup, encoding="utf-8", newline="\n")
    root = parse_html(markup)
    content = choose_content(root)
    title = document_title(root)
    output_md, assets_dir = resolve_output_paths(
        args.output_md,
        args.assets_dir,
        args.markdown_filename,
        title,
        final_url,
    )
    output_md.parent.mkdir(parents=True, exist_ok=True)
    if not args.skip_images:
        assets_dir.mkdir(parents=True, exist_ok=True)
    image_store = ImageStore(
        base_url=final_url,
        output_md=output_md,
        assets_dir=assets_dir,
        timeout=args.timeout,
        user_agent=args.user_agent,
        skip_images=args.skip_images,
    )
    markdown = clean_markdown(render_node(content, image_store, {"list_depth": 0}))
    markdown = postprocess_markdown(markdown, final_url)
    markdown = add_title(markdown, title)
    if args.source_comment and not args.no_source_comment:
        today = dt.date.today().isoformat()
        markdown = f"<!-- 来源: {final_url} -->\n<!-- 转换日期: {today} -->\n\n{markdown}"
    output_md.write_text(markdown, encoding="utf-8", newline="\n")
    return output_md, assets_dir, image_store.failures


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="将网页转换为 Markdown，并把图片下载到本地。"
    )
    parser.add_argument("url", help="源网页 URL、本地文件 URL，或 data:text/html URL。")
    parser.add_argument(
        "output_md",
        help=(
            "Markdown 输出路径，或文章归档根目录。传入无 .md 后缀的目录时，"
            "脚本会创建 <输出根目录>/<标题目录>/index.md。"
        ),
    )
    parser.add_argument(
        "--assets-dir",
        help=(
            "下载图片的保存目录。文章归档模式默认是文章目录下的 assets；"
            "单文件模式默认是 <output-stem>_assets。归档模式下相对路径按文章目录解析。"
        ),
    )
    parser.add_argument(
        "--markdown-filename",
        default="index.md",
        help="文章归档模式下的 Markdown 文件名，默认 index.md。",
    )
    parser.add_argument("--timeout", type=int, default=30, help="网络超时时间，单位秒。")
    parser.add_argument("--user-agent", default=DEFAULT_USER_AGENT, help="HTTP User-Agent。")
    parser.add_argument(
        "--skip-images",
        action="store_true",
        help="不下载图片，保留原始图片 URL。",
    )
    parser.add_argument(
        "--no-source-comment",
        action="store_true",
        help="兼容旧参数：默认已不添加来源和转换日期注释。",
    )
    parser.add_argument(
        "--source-comment",
        action="store_true",
        help="在 Markdown 顶部添加来源和转换日期注释。",
    )
    parser.add_argument(
        "--save-html",
        help="把抓取到的原始 HTML 保存到指定路径，便于调试特殊页面转换规则。",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        output_md, assets_dir, failures = convert(args)
    except Exception as exc:  # noqa: BLE001 - CLI should print a clear failure.
        print(f"错误：{exc}", file=sys.stderr)
        return 1
    print(f"Markdown：{output_md}")
    print(f"图片目录：{assets_dir}")
    if failures:
        print("图片下载失败：", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
