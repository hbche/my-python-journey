# Skill说明书

## 目录结构

一个Skill 最少需要一个 `SKILL.md` 文件：

```
skill-name/
└── SKILL.md          # 必需
```

> 可选目录包括 `scripts/`、`references/`、`assets/`。

## SKILL.md 格式

`SKILL.md` 文件由 YAML frontmatter + Markdown 正文 组成。

### Frontmatter(前置元数据)

| 字段          | 是否必需 | 说明                                                                                                  |
| ------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| name          | ✅ 是     | 最多 64 字符，仅允许小写字母、数字和连字符，不能以连字符开头/结尾，不能有连续连字符，且必须与父目录名 | 一致 |
| description   | ✅ 是     | 最多 1024 字符，描述 Skill 的功能和使用场景，应包含帮助 Agent 识别任务的关键词                        |
| license       | ❌ 否     | 许可证名称或引用的许可证文件                                                                          |
| compatibility | ❌ 否     | 最多 500 字符，说明环境要求（如目标产品、系统包、网络访问等）                                         |
| metadata      | ❌ 否     | 任意键值对映射，用于存储额外属性                                                                      |
| allowed-tools | ❌ 否     | 空格分隔的预批准工具列表（实验性功能）                                                                |

完整示例：

``` md
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
license: Apache-2.0
compatibility: Requires git, docker, jq, and access to the internet
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Bash(jq:*) Read
---
```

> 大多数 skill 不需要 compatibility 字段。

### Body 正文

Frontmatter 之后的 Markdown 正文包含 Skill 的指令，没有格式限制。推荐包含：

- 分步骤指令
- 输入/输出 示例
- 常见边界情况

## 可选目录

| 目录          | 用途                                                                      |
| ------------- | ------------------------------------------------------------------------- |
| `scripts/`    | 可执行代码（Python、Bash、JavaScript 等），应自包含并有良好的错误提示     |
| `references/` | 额外文档（如 REFERENCE.md、FORMS.md、领域文件等），按需加载，保持文件精简 |
| `assets/`     | 静态资源（模板、图片、数据文件、Schema 等）                               |

## 渐进式披露

这是 Skills 的核心设计理念，分三层高效管理上下文：

1. 元数据（约 100 tokens）：启动时仅加载 name 和 description
2. 指令（建议 < 5000 tokens）：Skill 被激活时加载完整 SKILL.md 正文
3. 资源（按需）：`scripts/`、`references/`、`assets/` 中的文件仅在需要时加载

> 建议 `SKILL.md` 保持在 500 行以内，详细参考资料移至单独文件。

## 文件引用

引用其他文件时使用相对于 Skill 根目录的路径：

``` md
See [the reference guide](references/REFERENCE.md) for details.

Run the extraction script:
scripts/extract.py
```

保持文件引用在 `SKILL.md` 的一层深度内，避免深层嵌套引用链。

## 验证

使用 [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) 参考库验证 Skill:

``` bash
skills-ref validate ./my-skill
```

这会检查 frontmatter 是否有效并遵循所有命名规范。