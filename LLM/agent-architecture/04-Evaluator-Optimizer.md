# Evaluator-Optimizer

你好。既然你已经梳理了从 2024 年到 2026 年的技术演进路径——从最初单纯依靠 **Prompt Engineering**，到融合 **RAG + MCP（Model Context Protocol）**，再到 **Agentic Architecture** 与 **Skill（微调与工具技能化）** 的全面控场——你一定深刻体会到：**靠单次、线性的 Prompt 注入去对付复杂的企业级业务，已经走到了尽头。**

在 Agent 时代，我们掌控大模型的方式，已经从“求着模型一次性写对”，变成了“构建一套让模型自我纠错、自我演进的工程架构”。

今天，我们就基于 **Anthropic 官方技术红皮书《Building Effective Agents》** 以及 **OpenAI Developer Platform** 的核心设计理念，深度拆解 Agent 时代的核心架构模式之一：**Evaluator-Optimizer（评估器-优化器）架构**。

---

## 一、 为什么在 Agent 时代需要 Evaluator-Optimizer？

在单次调用（Single-pass）模式下，无论你的 Prompt 写的有多长、多完美，大模型在面对复杂任务（如：写一段健壮的代码、输出一份严谨的财报、翻译法律条文）时，受限于**上下文窗口的注意力稀释**以及**Token生成的随机性**，其首发输出（First-shot）的合格率往往难以达到生产环境的要求。

Anthropic 在官方文档中明确指出：

> Evaluator-Optimizer 模式的核心逻辑是，将**生成（Generation）**与**评估（Evaluation）**职责解耦，通过多轮迭代的闭环反馈（Feedback Loop），用计算时间（Computational Cost）去换取更高的输出质量（Quality）。

这是一种典型的**思维链（Chain of Thought）在外层工程架构上的体现**。它不仅仅是一种“自动化测试”，它本身就是一个具备“反思与自我修正”能力的 Agent 系统。

---

## 二、 架构深度剖析（Architecture Blueprint）

根据 OpenAI 类似的设计范式，Evaluator-Optimizer 包含两个核心的角色，这两个角色在代码实现上，可以是两个采用不同 Prompt 的同一模型实例，也可以是两个完全不同规格的模型。

### 1. Generator / Optimizer（生成器/优化器）

- **职责**：负责接收任务输入，生成初代结果；并在后续循环中，**接收 Evaluator 返回的具象化反馈（Feedback），对原有输出进行定向修正和优化**。
- **设计要点**：必须具备“增量修改”的能力。它的 System Prompt 应该设计成接受 `(Task, Current_Output, Feedback)` 三元组，而不是每次都盲目地重写。

### 2. Evaluator（评估器/裁判）

- **职责**：对照严格的**业务准则（Rubrics）**或利用**自动化工具（如编译器、沙箱）**，对 Generator 的输出进行打分（Grading）并提供**具体、可执行的改进意见（Actionable Feedback）**。
- **设计要点**：Evaluator 是整个卡点系统的灵魂。如果 Evaluator 只会说 “回答得不好，请重写”，整个 Loop 就会陷入无效的死循环。它必须指出具体哪一行、哪个逻辑点违反了哪条规则。

---

## 三、 标准工作流（The Core Loop）

一个标准的 Evaluator-Optimizer Agent 工作流包含以下 4 个步骤，周而复始，直到触发终止条件：

```
[开始任务] ──> 1. Generate (产生/修正输出)
                    │
                    ▼
               2. Evaluate (对照 Rubrics 评估打分)
                    │
                    ├─> [满足阈值 / 达到最大迭代次数] ──> [Pass 退出]
                    │
                    ▼ (不满足)
               3. Feedback (产生具象化修改意见) ──循环回步骤 1

```

1. **Generate**：Generator 根据当前上下文，产生 initial_output。
2. **Evaluate**：Evaluator 对其进行质量扫描，输出一个结构化数据（例如 JSON），包含两个关键字段：`is_acceptable: boolean` 和 `feedback: string`。
3. **Check**：

- 如果 `is_acceptable == true`，或者达到了最大迭代上限（Max Iterations，通常设为 3~5 次以防止无限死循环和 Token 暴涨），流程终止，输出最终结果。
- 如果为 `false`，则进入下一步。

4. **Optimize**：Generator 吸收 `feedback`，重新进炉提炼，生成 refined_output，再次提交评估。

---

## 四、 核心落地细节：以“代码生成与测试卡点”为例

为了让你能直接写出代码，我们来看看在实际工程中，如何落地这一模式。假设我们要让 Agent 写一个满足严格类型安全和复杂业务逻辑的 Python 函数。

### 1. Evaluator 的 Rubrics（评分量表）设计

根据 OpenAI 关于 Trace Grading 的官方指南，评估器必须基于**明确、客观、不可二义性**的准则。在代码场景下，最佳实践是**混合评估器（Hybrid Evaluator）**：

- **硬卡点（Rule-based）**：运行 `pytest`、`mypy` 静态类型检查。这些工具的报错日志（Stderr）就是最完美的、毫无偏见的 Feedback。
- **软卡点（LLM-as-a-Judge）**：用大模型评估代码的圈复杂度、可读性、是否包含安全漏洞。

### 2. 核心 Prompt 模板（Anthropic 风格）

**Generator (Iteration 阶段的 Prompt):**

```markdown
You are an expert software engineer. Your task is to refine the code based on the implementation requirements and the feedback from the Evaluator.

<Requirements>
{{TASK_DESCRIPTION}}
</Requirements>

<Current_Code>
{{CURRENT_CODE}}
</Current_Code>

<Evaluator_Feedback>
{{FEEDBACK}}
</Evaluator_Feedback>

Analyze the feedback carefully. Fix all failing tests, type errors, or architectural issues mentioned. Output ONLY the complete revised python code inside a `python ` block.
```

**Evaluator (LLM 裁判阶段的 Prompt):**

```markdown
You are a strict Senior Code Reviewer. Evaluate the provided code against the requirements.

<Requirements>
{{TASK_DESCRIPTION}}
</Requirements>

<Code_To_Review>
{{CURRENT_CODE}}
</Code_To_Review>

<Execution_Logs>
{{TEST_RUN_STDOUT_STDERR}}
</Execution_Logs>

You must output a JSON object with the following schema:
{
"grade": "ACCEPTABLE" | "NEEDS_REVISION",
"critical_flaws": ["List of precise issues found, e.g., missing edge case handling for empty list"],
"actionable_feedback": "Specific, clear instructions for the generator to fix these issues. Do not be vague."
}
```

---

## 五、 资深工程师的避坑与优化指南 (Pro-Tips)

当你在 2026 年构建这种高级 Agent 时，你会发现很多纸面上的理论在生产环境中会遇到挑战。以下是来自一线落地的核心经验：

1. **防止“确认偏误（Confirmation Bias）”**

- _问题_：如果你让同一个 Agent 实例（共用一个上下文和 Session）先生成代码，再自己检查，它会倾向于认为自己是对的（Reflection 模式的弊端）。
- _解法_：**必须做上下文隔离**。Evaluator 的调用要干净，只把上一步的“生成结果”作为纯文本输入喂给它，不要让它看到 Generator 之前的“碎碎念（Thought 过程）”。

2. **防止“无限钟摆（Infinite Oscillations）”**

- _问题_：有时 Generator 修改了 A 问题，引出了 B 问题；下一轮修复了 B 问题，又带回了 A 问题。
- _解法_：系统必须维护一个状态机（State History）。如果连续两轮的 Score 没有提升，或者在两个相似的错误间摆动，Optimizer 必须引入“降级机制”：要么放大模型的 Temperature 增加随机性打破僵局，要么直接抛出异常触发 Human-in-the-loop（人工介入卡点）。

3. **成本与延迟的平衡（ROI Control）**

- _问题_：每多一轮 Loop，Token 消耗翻倍，用户等待延迟（TTFT/Latency）成倍增加。
- _解法_：参考 OpenAI 的模型蒸馏（Distillation）与混合路由策略。**Generator 可以选用速度快、成本低的推理模型（如 GPT-4o-mini 或 Claude 3.5 Haiku），而把高昂的算力留给关键的卡点裁判（如 GPT-4o 或 Claude 3.5 Sonnet）**。只有当小模型冲刺 2 次失败后，才动态将 Generator 升级替换为大模型。

---

## 总结

从 2024 年的“死磕 Prompt 话术”，到如今通过 **Evaluator-Optimizer 架构实现确定性的质量卡点**，我们对待 LLM 的态度已经完全走向了工程化。我们不再奢望模型每一次都能给出完美解答，而是通过建立一套**容错、监控、反馈、修正**的闭环流水线，把大模型的随机性牢牢锁在业务安全线之内。

对于这一套 Agent 架构在具体业务场景（例如：结构化 JSON 数据提取卡点、合规性文案审查）中的设计，你目前最希望先在哪个场景落地？
