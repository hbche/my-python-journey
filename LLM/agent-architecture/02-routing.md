# 路由

回顾过去这两三年的技术演进，感触确实深刻。从 2024 年疯狂调试 System Prompt 的“提示词工程”时代，到 2025 年融入 RAG 与 MCP（Model Context Protocol）打破知识孤岛，再到如今 2026 年，我们全面进入了以 **Agent 架构**和 **Skill（技能原子化）** 为核心的时代。

正如你所说，Prompt Engineering 的定位已经变了。它不再是掌控 LLM 的**唯一手段**，而是退步为**控制系统流转、规范接口协议的“连接线”**。真正决定 AI 系统稳定性和天花板的，是底层的 **Agent Architecture（智能体架构）**。

根据 Anthropic 官方在《Building Effective Agents》中的定义，以及 OpenAI 针对 Assistants API 与 Swarm 框架的架构设计，现代 Agent 的核心流转模式可以浓缩为几种经典工作流（Workflows）。今天，我们就从整个 Agent 架构的“交通枢纽”—— **Routing（路由机制）** 开始讲起。

---

## 什么是 Routing（路由机制）？

在复杂的实际业务场景中，我们不可能只靠一个通用 Prompt 或一个巨大的模型去解决所有问题。这样不仅成本高、响应慢，而且极易触发大模型的“幻觉”或拒绝回答。

**Routing（路由）**，本质上是 **Agent 架构中的分流器和决策层**。它的核心职责是：**接收用户的输入（Input），判断其真实意图（Intent），并将其精准分发给最适合的处理模块（无论是特定的 Prompt 模板、子 Agent，还是传统的 API / 数据库）**。

### 为什么说它是 Agent 的基本功？

* **动态上下文控制**：只给下游模块注入其所需的背景知识，避免无关上下文的干扰。
* **成本与性能优化**：可以用轻量、低成本的小模型（如 Claude 3.5 Haiku / GPT-4o-mini）做高并发的路由决策，而将真正复杂的任务留给大模型（如 Claude 3.5 Sonnet / GPT-4o），实现 ROI 最大化。
* **系统确定性**：将模糊的自然语言转化为确定性的工程流转。

---

## Routing 的三大核心实现方案

参考 Anthropic 和 OpenAI 的生产级工程实践，目前主流的路由实现主要有以下三种方式。它们由浅入深，复杂度和精准度也依次递增。

### 1. Classification Routing（基于分类提示的路由）

这是最经典、最直接的路由方式。通过给模型定义清晰的分类标准，让模型直接输出目标路由的标签。

* **实现原理**：编写一个高内聚的 `System Prompt`，列出所有可选的下游通道（Channels），并要求模型**必须且只能**输出预设的 Key（如 JSON 格式或纯文本 Tag）。
* **官方推荐实践 (Anthropic)**：在 Prompt 中引入少量的 Few-Shot Examples（少样本提示），并明确定义“边界 case”（即 A 分类和 B 分类交叉时该怎么选）。
* **工程示例**：
```json
// 路由模型输出的结构化数据
{
  "intent": "technical_support",
  "confidence_score": 0.95,
  "next_step": "agent_code_interpreter"
}

```



### 2. Function Calling / Tool Choice Routing（基于工具调用的路由）

随着大模型底层对 Tool Use（工具调用）的内生优化，这种方式已成为当前 2026 年的行业标准。OpenAI 的 Function Calling 和 Anthropic 的 Tool Use 允许我们把下游的“处理模块”直接包装成“工具”。

* **实现原理**：你不需要在 Prompt 里长篇大论地教模型怎么分类，而是声明 3 个工具（比如 `search_database`、`execute_code`、`escalate_to_human`）。路由模型会通过语义理解，自动选择最匹配的工具并提取出所需的参数。
* **为什么更好**：
* **强类型约束**：模型输出的是 JSON 格式的工具参数，完美对接工程代码。
* **强制路由 (Tool Choice)**：可以通过参数（如 OpenAI 的 `tool_choice: {"type": "function", "function": {"name": "X"}}`）强行要求模型在特定场景下必须走某个路由。



### 3. Semantic / Vector Routing（语义向量路由）

在前两种方案中，每次路由都需要请求一次 LLM，存在一定的耗时（Latency）和 Token 成本。如果你的路由规则非常死、非常明确（比如标准的客服 FAQ 分流），可以使用**向量检索路由**。

* **实现原理**：提前将各类意图的典型用户问题转化为 Embedding（向量）存入向量数据库。当新输入进入时，计算其余弦相似度（Cosine Similarity），如果匹配度超过设定阈值（如 > 0.85），直接通过硬编码（Hard-coded）路由到对应模块，**完全不经过 LLM**；只有未匹配到时，才降级（Fallback）给 LLM 路由。
* **优点**：毫秒级响应，0 Token 成本。

---

## 生产环境中的高级路由设计模式

在设计复杂的 Agent（例如多 Agent 协作系统、大厂的 AI 助手）时，单层的路由是远远不够的。通常会结合以下两种高级模式：

### 🔄 动态双向路由 (Bidirectional Routing)

路由不是一锤子买卖。在 Anthropic 推荐的方案中，下游 Agent 处理完任务后，拥有反向路由（Fallback / Escalation）的权利。

* *场景*：路由把用户分发给了 `Agent_Invoice（发票处理专家）`。但用户聊着聊着突然说：“顺便帮我把账号注销了吧。”
* *机制*：`Agent_Invoice` 检测到超出了自己的 Skill 边界，会将请求重新路由回 `Main_Router` 或触发 `Escalation_Tool` 移交给账号专家。

### 📊 分层路由 (Hierarchical Routing)

当系统极其庞大，拥有数十个 Skill（技能）时，单一模型的上下文无法支撑庞大的工具列表（会导致模型注意力分散，选错工具）。

* *机制*：采用**总-分结构**。`Level-1 Router` 只负责粗拆意图（技术、财务、人事），路由到对应的子域后，再由 `Level-2 Sub-Router` 精细化分发到具体的 Skill 线程。

---

## 避坑指南：资深工程师的架构心得

在落地 Routing 架构时，有几个官方文档不会明说、但生产环境痛过才知道的工程细节：

1. **拒绝“既要又要”**：做路由决策的模型（Router），就让它**纯粹地做选择题**，不要让它在路由的同时去长篇大论地回答用户问题。路由请求的 `max_tokens` 应该设置得非常小（通常限制在几十个 Token 内输出 JSON 即可），以此提升吞吐量。
2. **严格的 Fallback 机制**：无论你的 Prompt 写得多完美，模型都有可能输出规划之外的标签。在工程代码层面，必须写好 `try-catch`。一旦路由解析失败，必须有兜底路由（例如转发给通用大模型或人工客服）。
3. **温度系数（Temperature）调校**：对于路由大模型，建议将 `temperature` 设置为 `0`。我们需要的是**高度的确定性和可重复性**，而不是创造力。

---

## 总结与下一步

**Routing 是整个 Agent 系统的骨架**。它将单一的、不可控的 LLM 转化为了一个有序、可控、可观测的软件架构。

理清了 Routing，我们就拿到了开启 Agent 时代大门的钥匙。在现代 Agent Architecture 中，通过路由分流后，接下来要面对的就是具体的“执行模式”了。

在下一个章节中，我们可以深入探讨在业界被广泛验证的另外两种核心流转模式：**Orchestrator-Workers（编排者-执行者模式）** 或是 **Evaluator-Optimizer（评估者-优化者模式，即经典的 Reflexion 反思流）**。你想先了解哪一个？
