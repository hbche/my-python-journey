# 在 Skills 中使用脚本

## 概述

Skills 可以指示 Agent 运行 shell 命令，并在 `scripts/` 目录中捆绑可复用的脚本。该页面涵盖三个方面：一次性命令、自包含脚本、以及为 Agent 使用设计脚本接口。

## 一次性命令（One-off Commands）

当现有包已经能满足需求时，可以直接在 SKILL.md 中引用，无需 scripts/ 目录。多种生态系统提供运行时自动解析依赖的工具：

## 从 SKILL.md 引用脚本

使用相对于 Skill 目录根的路径引用捆绑文件：

``` md
## Available scripts

- **`scripts/validate.sh`** — 验证配置文件
- **`scripts/process.py`** — 处理输入数据
```

然后指示 Agent 运行：

``` md
## Workflow

1. 运行验证脚本：
   bash scripts/validate.sh "$INPUT_FILE"

2. 处理结果：
   python3 scripts/process.py --input results.json
```

### 自包含脚本（Self-contained Scripts）

当需要可复用逻辑时，在 `scripts/` 中捆绑一个内联声明依赖的脚本，Agent 只需一条命令即可运行，无需单独的 `manifest` 文件或安装步骤。

有些语言还支持行内依赖声明，例如，我们在 `scrpits/` 下声明一个 `extract.py` 的脚本，内容如下：

``` py
# /// script
# dependencies = [
#   "beautifulsoup4",
# ]
# ///

from bs4 import BeautifulSoup

html = '<html><body><h1>Welcome</h1><p class="info">This is a test.</p></body></html>'
print(BeautifulSoup(html, "html.parser").select_one("p.info").get_text())
```

我们可以直接使用 [`uv`](https://docs.astral.sh/uv/) 执行这个脚本：

``` bash
uv run scripts/extract.py
```

输出：

```
This is a test.
```

`uv run` 将创建一个安装脚本所需依赖的隔离的环境，然后运行脚本。

-  PEP 508 锁定版本：`"beautifulsoup4>=4.12,<5"`
- 用 `uv lock --script` 创建锁文件实现完全可复现

## 为 Agent 的使用设计脚本（核心设计原则）

Agent 通过读取 stdout 和 stderr 来决定下一步操作，以下设计选择至关重要：

### 1. 避免交互式提示（硬性要求）

Agent 通过读取 stdout 和 stderr 来决定下一步操作，以下设计选择至关重要：

``` bash
# 错误：挂起等待输入
$ python scripts/deploy.py
Target environment: _

# 正确：清晰的错误和指引
$ python scripts/deploy.py
Error: --env is required. Options: development, staging, production.
Usage: python scripts/deploy.py --env staging --tag v1.2.3
```

### 2. 用 `--help` 文档化用法

`--help` 输出是 Agent 学习脚本接口的主要方式。包含简要描述、可用标志和使用示例，但保持简洁——输出会进入 Agent 的上下文窗口。

``` bash
Usage: scripts/process.py [OPTIONS] INPUT_FILE

Process input data and produce a summary report.

Options:
  --format FORMAT    Output format: json, csv, table (default: json)
  --output FILE      Write output to FILE instead of stdout
  --verbose          Print progress to stderr

Examples:
  scripts/process.py data.csv
  scripts/process.py --format csv --output report.csv data.csv
```

关键提示：`--help` 的输出要保持简洁，因为这些内容会进入 Agent 的上下文窗口，与 Agent 正在处理的所有其他内容共存。过于冗长的帮助信息会占用宝贵的上下文空间。

### 3. 编写有帮助的错误信息

不要写模糊的 "Error: invalid input"，而是要说明出了什么问题、期望什么、该怎么做：

``` bash
Error: --format must be one of: json, csv, table.
       Received: "xml"
```

### 4. 使用结构化输出

优先使用 JSON、CSV、TSV 等结构化格式，而非自由文本。结构化格式可被 Agent 和标准工具（`jq`、`cut`、`awk`）消费。

``` bash
# Whitespace-aligned — hard to parse programmatically
NAME          STATUS    CREATED
my-service    running   2025-01-15

# Delimited — unambiguous field boundaries
{"name": "my-service", "status": "running", "created": "2025-01-15"}
```

关键原则： 将数据发送到 stdout，将诊断信息发送到 stderr，让 Agent 获取干净、可解析的输出。

### 其他重要考虑

| 原则             | 说明                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| 幂等性           | Agent 可能重试命令，"不存在则创建"比"创建并在重复时失败"更安全                                                     |
| 输入约束         | 拒绝模糊输入并给出清晰错误，尽量使用枚举和封闭集合                                                                 |
| Dry-run 支持     | 对破坏性操作提供 --dry-run 标志，让 Agent 预览结果                                                                 |
| 有意义的退出码   | 对不同失败类型使用不同退出码，并在 --help 中文档化                                                                 |
| 安全默认值       | 破坏性操作应要求显式确认标志（--confirm、--force）                                                                 |
| 可预测的输出大小 | 许多 Agent 会自动截断超过阈值（如 10-30K 字符）的输出。默认输出摘要，支持 --offset 等标志让 Agent 按需请求更多信息 |


