# 什么是Skills

Skills（技能） 是一种轻量级、开放的格式，用于通过专业知识和工作流扩展 AI Agent 的能力。

核心结构： 一个 Skill 本质上是一个包含 SKILL.md 文件的文件夹。该文件包括元数据（至少有 name 和 description）以及告诉 Agent 如何执行特定任务的指令。还可以捆绑脚本、模板和参考资料。

```
my-skill/
├── SKILL.md          # 必需：指令 + 元数据
├── scripts/          # 可选：可执行代码
├── references/       # 可选：文档
└── assets/           # 可选：模板、资源 
```

## SKILL.md文档

每个 Skill 都一个 `SKILL.md` 文件开始，它包含 YAML frontmatter（前置元数据） 和 Markdown 指令两部分，下面是一个简单的示例：

``` mk
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
---

# PDF Processing

## When to use this skill
Use this skill when the user needs to work with PDF files...

## How to extract text
1. Use pdfplumber for text extraction...

## How to fill forms
...
```

### 必须的Frontmatter字段

在 `SKILL.md` 顶部必须包含以下 YAML frontmatter：

- `name`: 一个简短的标识符（如 `pdf-processing`）
- `description`: 描述何时使用该 Skill

### Markdown 正文

Frontmatter 之后的 Markdown 正文包含实际的指令内容，对结构或内容没有特定限制，可以自由编写。

## 工作原理：渐进式披露

1. 发现阶段
2. 激活阶段
3. 执行阶段

## 关键优势

- 自文档化: 任何人都可以阅读 `SKILL.md` 并理解其功能，便于审计和改进。
- 可扩展: 从纯文本指令到可执行代码、资产和模板，复杂度灵活可变。
- 可移植: Skills 只是文件，易于编辑、版本控制和共享。

## 参考文献

[What are skills](https://agentskills.io/what-are-skills)