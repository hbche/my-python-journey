---
name: webpage-to-markdown
description: 将指定网页链接，尤其是技术博客或官方文档页面，转换成本地 Markdown 归档。适用于用户要求把网页文档或博客保存到给定目录、按文章标题创建独立目录、下载页面图片到文章目录内的 assets 子目录，并将 Markdown 中的图片引用改写为本地相对路径的场景。
---

# 网页转 Markdown

## 概览

使用这个 skill 将网页文章、技术博客或官方文档归档为本地 Markdown，并把图片资源保存到本地。优先使用随附脚本完成稳定转换和图片链接重写；遇到页面结构特殊时，再检查生成结果并做少量清理。

## 快速开始

优先把用户给出的目标目录当作归档根目录运行转换脚本：

```bash
python scripts/webpage_to_markdown.py "https://example.com/docs/page" "posts"
```

默认情况下，脚本会先读取网页标题，然后创建：

```text
posts/<文章标题安全目录名>/
├── index.md
└── assets/
```

图片会保存到该文章目录内的 `assets/` 子目录，Markdown 图片链接会改写为类似 `assets/example.png` 的相对路径。后续迁移时直接复制整篇文章目录即可保持图片引用有效。

如果用户明确指定了 `.md` 输出文件，脚本保留单文件兼容模式：

```bash
python scripts/webpage_to_markdown.py "https://example.com/blog/post" "docs/post.md"
```

单文件模式下，默认图片目录仍是 Markdown 文件旁边的 `<markdown-stem>_assets/`。只有用户明确要求扁平文件结构时才使用这种模式。

如果用户指定了图片目录，使用 `--assets-dir`。在文章归档模式下，相对的 `--assets-dir` 会按文章目录解析：

```bash
python scripts/webpage_to_markdown.py "https://example.com/blog/post" "posts" --assets-dir "media"
```

如果沙箱中的网络请求失败，使用同一条命令申请必要的网络/权限提升后重试，不要改变转换流程。

## 工作流程

1. 确认用户提供了源网页 URL 和保存位置。若用户给的是 `posts/`、`docs/` 等目录，按归档根目录处理，不要把所有 Markdown 和图片直接平铺在该目录下。
2. 使用 URL 和归档根目录运行 `scripts/webpage_to_markdown.py`。脚本会根据网页标题创建文章目录、生成 `index.md`，并把图片放进文章目录内的 `assets/`。
3. 只有在用户明确指定 `.md` 文件路径或要求单文件输出时，才把第二个参数写成具体 Markdown 文件路径。
4. 当用户给出图片目录时，传入 `--assets-dir`；文章归档模式下优先使用文章目录内的相对子目录。
5. 打开生成的 Markdown 并检查：
   - 标题和第一段内容有意义。
   - 图片使用文章目录内的本地相对路径（如 `assets/...`），而不是远程 URL；无法下载的图片除外。
   - 代码块、标题、列表、表格和链接可读。
6. 如果页面主要依赖 JavaScript 渲染，或禁止直接抓取，先用浏览器/导出方式取得渲染后的 HTML，保存为临时 `.html` 文件，再让脚本处理该本地 HTML，或手动补充清理。
7. 向用户报告文章目录、Markdown 文件路径和图片目录。说明任何无法获取的图片或内容。

## 脚本参数

- `url`：必填，源网页 URL。支持 HTTP(S)、本地 HTML 路径、`file://` 和简单的 `data:text/html` 输入。
- `output_md`：必填，Markdown 输出路径或文章归档根目录。无 `.md`/`.markdown` 后缀时视为归档根目录，输出为 `<root>/<title-slug>/index.md`。
- `--assets-dir`：可选，图片输出目录。归档模式默认是文章目录内的 `assets/`；单文件模式默认是 `<output-md-stem>_assets`。归档模式下相对路径按文章目录解析。
- `--markdown-filename`：可选，归档模式下 Markdown 文件名，默认 `index.md`。
- `--timeout`：网络超时时间，单位秒，默认 `30`。
- `--user-agent`：覆盖默认的浏览器式 User-Agent。
- `--skip-images`：不下载图片，保留原始图片 URL。
- `--no-source-comment`：不在 Markdown 顶部添加 `Source:` 注释。

## 质量要求

- 优先使用官方 canonical URL，而不是带重定向、跟踪参数、打印样式或镜像的 URL，除非用户明确指定。
- 输出路径应保持在工作区或用户批准的目录内。
- 默认使用“文章目录 + index.md + assets/”的可迁移结构；不要把多篇文章和所有图片平铺在同一个目录中。
- 保留原文结构；除非用户要求摘要，否则不要总结内容。
- 不要虚构缺失图片。图片下载失败时，保留原始 URL 并向用户说明。
- 多页文档默认每页转换为一个 Markdown 文件；只有在用户明确要求时才合并成单个文件。

## 资源

- `scripts/webpage_to_markdown.py`：仅使用 Python 标准库的转换脚本。它会抓取网页、提取可能的 article/main 正文、将常见 HTML 结构转换为 Markdown、下载图片，并把图片链接改写为本地相对路径。
