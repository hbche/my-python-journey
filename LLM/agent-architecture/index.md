# Agent 架构

随着时间的演进，掌控LLM的方式也发生了变化，从最初优化 Prompt Engineering 来优化 LLM 的能力，转变为了 LLM + Tool + Memory + Loop 的架构，这就是现代 Agent 的雏形，接下来我们将进入 Agent 时代，进入 **Agent Architecture（Agent架构）**，学习内容包括：

1. Prompt Chaining（提示链）
2. Routing（路由）
3. Parallelization（并行执行）
4. Orchestrator-Worker（调度者-执行者）
5. Evaluator-Optimizer（评审-优化器）
6. Single Agent
7. Multi-Agent
8. Skill 与 MCP 在 Agent 中的设计方式

这一部分才是现代 OpenAI、Anthropic Agent 系统设计的核心。

[1]: https://www.anthropic.com/engineering/building-effective-agents?via=aitoolhunt&utm_source=chatgpt.com "Building Effective AI Agents"
[2]: https://www.reddit.com/r/AI_Agents/comments/1jtjfu5?utm_source=chatgpt.com "The 3 Rules Anthropic Uses to Build Effective Agents"
[3]: https://sureprompts.com/blog/react-prompting-guide?utm_source=chatgpt.com "ReAct Prompting Guide: Reasoning Plus Acting for AI Agents (2026) | SurePrompts"
[4]: https://platform.openai.com/docs/guides/reasoning-best-practices?utm_source=chatgpt.com "Reasoning best practices | OpenAI API"
