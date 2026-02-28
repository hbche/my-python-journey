# Skill vs Prompt

## Skill vs. Prompt：核心区别

我们以“餐厅”来类比 Skill 和 Prompt 之间的关系：

| 特性   | Prompt （提示词）                            | Skill （AI技能）                                               |
| ------ | -------------------------------------------- | -------------------------------------------------------------- |
| 定义   | 我们对 AI 下达的具体指令。                   | AI 被赋予的特定功能或外部工具。                                |
| 类比   | 顾客点的具体菜名和口味要求（“少盐、多辣”）。 | 厨房里的专业厨具或半成品菜包（“空气炸锅”、“洗好的切片土豆”）。 |
| 交互性 | 瞬时的、灵活的，随写随用。                   | 预设的、结构化的，通常涉及外部 API 或代码。                    |
| 复用性 | 较低，需要反复输入或保存。                   | 极高，一次配置，全局调用（如“搜索”、“绘图”）。                 |
| 深度   | 决定了 AI 的思考逻辑。                       | 拓展了 AI 的能力边界。                                         |

## 有了成熟的Skill，为什么还要学Prompt？

虽然现在的 Skill 已经能解决 80% 的通用需求，但剩下的 20% 定制化需求必须靠 Prompt 来驱动。

### Prompt 是 Skill 的“驱动引擎”

每一个成熟的 Skill 背后，往往都隐藏着一段复杂的 System Prompt（系统提示词）。

- 如果我们不会写 Prompt，我们就只能使用别人定义好的 Skill，而无法根据自己的业务逻辑创建属于自己的 Skill。
- 新手视角：学习 Prompt 是为了从“工具使用者”转变为“工具开发者”。

### 解决“最后一公里”的精准度

Skill 提供了通用的处理能力，但它不知道我们的个性化偏好。

- 例子：一个“翻译 Skill”能把英文翻成中文，但如果我们需要它“翻译成鲁迅的文风”，这就是 Prompt 的工作。
- 技巧：Skill 负责“能做”，Prompt 负责“做得怎么样”。

### 多 Skill 的调度与编排

在复杂的任务中，我们需要同时调用多个 Skill（比如先用搜索 Skill 查资料，再用绘图 Skill 出图）。

- 如何在这些步骤之间传递信息？
- 如何让 AI 在切换 Skill 时不丢失上下文？

这些都属于Prompt Engineering 中高级的“工作流编排”范畴。

## 2026年我们如何学习 Prompt

2026年我们不需要再学习那些过时的“格式咒语”（比如 Let's think step by step），因为这些技巧都被模型掌握了。
我们应该关注以下两点：

- 结构化 Prompt 设计：使用 Markdown、JSON 格式来定义任务。
- RAG与 Skill 的参数传递：学习如何通过 Prompt 告诉 AI：“请调用搜索引擎 Skill，但只提取其中关于价格的数据，并以表格形式输出。”

### 学习 Prompt 的参考资料

如果我们想系统地学习，以下是目前最权威、最“官方”的几个资源，它们比第三方网站更具深度且紧跟技术前沿：

1. 官方开发者文档
   - Google AI (Gemini 3)：[Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies)
     - 亮点：专门讲解了如何针对 Gemini 3 Flash 进行“结构化提示”，包括如何使用 XML 标签分隔指令和数据，以及如何处理超长上下文（Long Context）。
   - Anthropic (Claude): [Prompt Engineering Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)
     - 亮点：被公认为业界最详细的指南。它教你如何让 AI “先思考再回答”（Chain of Thought），以及如何通过 XML 标签（如 `<task>`）精确控制复杂输出。
   - OpenAI: Prompt Engineering Strategy
     - 亮点：侧重于策略和评估（Evals），教你如何科学地测试一个 Prompt 的好坏。

2. 官方互动实验课
   - Google Prompting Essentials (Coursera)
     - 亮点：这是 Google 官方在 Coursera 上推出的专项课程，不到 10 小时就能完成。它教的是一套 “5步提示法”，非常适合新手建立标准化的工作流。
   - DeepLearning.AI (Andrew Ng 联名系列)
     - 亮点：吴恩达教授与 OpenAI、Anthropic 合作的一系列免费短课（如 ChatGPT Prompt Engineering for Developers）。虽然是几年前开始的，但内容一直在随模型版本更新，是工程师入行的必修课。
   - [Anthropic's Interactive Tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
     - 亮点：这是 Anthropic 在 GitHub 上开源的一个互动教程，你可以直接在 Google Sheets 或其 Playground 里练习，从初级到高级都有。
3. 开源社区标杆
    - [Learn Prompting](https://learnprompting.org/)

推荐顺序：

```
先看 Anthropic 的文档：学会用 XML 标签和 Markdown 结构化我们的想法，这能瞬间让我们的 Prompt 从“聊天”变成“程序”。
    ↓
去 Google AI 使用 Gemini 3 Flash 实操：测试长文本处理能力，感受“大语境”下 Prompt 的变化。
    ↓
学习 Prompt Chaining（提示链）：不要试图写一个万能的 Prompt，学会把复杂任务拆解成多个 Skill 的串联。
```