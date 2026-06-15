# 第1课：ReAct 与 Agent Prompt 究竟是什么？

如果说：

* Prompt Engineering 是编写函数
* Workflow 是编排函数
* Agent 是运行中的程序

那么：

> ReAct 就是 Agent 的“大脑运行机制”。

很多人把 ReAct、Agent、Tool Calling、Workflow 混在一起。

实际上这是四个不同层次的东西。

```text
Prompt
  ↓
ReAct
  ↓
Agent
  ↓
Multi-Agent
```

理解这个层次非常重要。

---

## 一、先理解 Agent 出现的原因

我们先看传统 LLM。

### 第一代

```text
用户
 ↓
LLM
 ↓
答案
```

例如：

```text
帮我解释什么是微服务
```

模型直接回答。

这是最简单模式。

---

这种模式有一个特点：

```text
一次输入
一次输出
```

也叫：

```text
Single Shot
```

---

但现实问题往往不是这样。

例如：

```text
帮我分析这个GitHub项目
```

模型需要：

```text
访问GitHub
↓
读取README
↓
查看代码
↓
分析架构
↓
输出结果
```

单次问答做不到。

---

于是出现：

```text
Tool Use
```

即：

```text
LLM
+
工具
```

例如：

```text
浏览器
搜索引擎
数据库
文件系统
API
```

---

但新的问题来了。

## 谁决定什么时候调用工具？

例如：

```text
查询天气
```

模型需要：

```text
调用天气API
```

---

而：

```text
解释TCP三次握手
```

不需要工具。

---

那么问题来了：

```text
什么时候调用工具？
调用哪个工具？
调用几次？
```

这就是Agent出现的原因。 ([Anthropic][1])

---

## 二、什么是 Agent？

Anthropic 对 Agent 和 Workflow 有一个非常经典的定义：

Workflow：

```text
开发者规定流程
```

Agent：

```text
模型自己决定流程
```

即：

Workflow：

```text
Step1
 ↓
Step2
 ↓
Step3
```

固定。

---

Agent：

```text
目标
 ↓
模型自主规划
 ↓
决定工具
 ↓
决定步骤
 ↓
完成任务
```

动态。 ([Anthropic][1])

---

例如：

用户：

```text
帮我调查OpenAI最新Agent产品
```

Workflow可能是：

```text
搜索
↓
总结
↓
输出
```

固定。

---

Agent可能是：

```text
搜索官网
↓
发现新发布会
↓
查看发布会
↓
发现论文
↓
读取论文
↓
总结
```

动态。

---

所以：

## Agent = LLM + Memory + Tool + Loop

最经典公式：

```text
Agent
=
LLM
+
Tools
+
Memory
+
Environment
+
Loop
```

其中：

```text
Loop
```

最重要。

因为Agent不是一次回答。

而是不断循环。

```text
思考
↓
行动
↓
观察
↓
继续思考
```

直到完成任务。 ([Reddit][2])

---

## 三、ReAct到底是什么？

ReAct来自经典论文：

《ReAct: Synergizing Reasoning and Acting》

名字拆开：

```text
Re
=
Reasoning

Act
=
Acting
```

即：

```text
推理
+
行动
```

---

论文之前有两个流派。

### 流派1

CoT

Chain of Thought

```text
思考
↓
思考
↓
思考
↓
答案
```

只会想。

不会行动。

---

例如：

```text
北京天气怎么样
```

模型无法获取实时天气。

---

### 流派2

Tool Use

```text
工具
↓
工具
↓
工具
```

只会调用工具。

缺少推理。

---

ReAct融合二者。

```text
Reason
↓
Action
↓
Observation
↓
Reason
↓
Action
↓
Observation
```

循环进行。 ([SurePrompts][3])

---

## 四、ReAct的核心循环

这是整个Agent世界最重要的图。

```text
Thought
 ↓
Action
 ↓
Observation
 ↓
Thought
 ↓
Action
 ↓
Observation
```

简称：

```text
T-A-O Loop
```

或者：

```text
R-A-O Loop
```

---

举个例子。

用户：

```text
OpenAI CEO是谁？
他最近有什么新闻？
```

---

Agent内部：

#### Thought

```text
我需要先找到CEO是谁
```

---

#### Action

```text
Search(OpenAI CEO)
```

---

#### Observation

```text
Sam Altman
```

---

#### Thought

```text
现在查询Sam Altman最新新闻
```

---

#### Action

```text
Search(Sam Altman latest news)
```

---

#### Observation

```text
获得新闻结果
```

---

#### Thought

```text
信息足够
开始总结
```

---

#### Final Answer

```text
输出答案
```

这就是ReAct。 ([SurePrompts][3])

---

## 五、ReAct Prompt 长什么样？

最经典模板：

```text
You are an intelligent agent.

For every task:

Thought:
Think about what to do.

Action:
Choose a tool.

Observation:
Observe the result.

Repeat until solved.

Finally provide Answer.
```

---

Few-shot版本：

```text
Question: xxx

Thought: ...
Action: Search(...)
Observation: ...

Thought: ...
Action: Lookup(...)
Observation: ...

Answer: ...
```

---

这也是很多早期Agent框架：

* LangChain
* AutoGPT
* BabyAGI

最初使用的Prompt结构。 ([SurePrompts][3])

---

## 六、现代Agent还用ReAct吗？

答案：

```text
用
但已经升级了
```

很多人以为ReAct过时。

实际上没有。

现代Agent几乎都保留ReAct思想。

例如：

* Claude Code
* Cursor Agent
* OpenAI Agent
* Codex Agent
* Aider

本质仍然是：

```text
思考
↓
调用工具
↓
获取反馈
↓
继续思考
```

只是Thought不一定显式展示给用户。 ([SurePrompts][3])

---

## 七、OpenAI 与 Anthropic 对 ReAct 的最新观点

这里有个重要认知升级。

很多教程还在教：

```text
Think Step By Step
```

但 OpenAI 对推理模型的建议已经发生变化。

对于现代推理模型：

```text
不要过度强制CoT
不要要求暴露全部思维链
重点描述任务和工具
```

因为模型内部已经具备推理能力。 ([OpenAI平台][4])

---

Anthropic近两年的观点也非常一致：

不要一上来就构建复杂Agent。

优先：

```text
Single LLM
↓
Workflow
↓
Agent
```

逐步升级。

因为Agent：

```text
成本更高
延迟更高
更难调试
```

只有在任务路径无法提前确定时，才真正需要Agent。 ([Anthropic][1])

---

## 八、Agent Prompt 的本质

很多人误认为：

```text
Agent Prompt
=
超长Prompt
```

错。

Agent Prompt的本质是：

```text
定义Agent的行为规则
```

类似：

```text
操作系统
```

---

一个完整Agent Prompt通常包含：

```text
Role
Goal
Constraints
Tools
Planning Rules
Memory Rules
Termination Rules
Output Rules
```

结构如下：

```text
# Role

你是一名高级软件架构师Agent

# Goal

完成用户指定的软件设计任务

# Tools

Search
ReadFile
WriteFile
Git

# Planning Rules

先规划
再执行

# Constraints

不要修改生产环境

# Memory Rules

记录关键决策

# Termination

目标完成后停止

# Output

Markdown
```

---

## 九、工程实践中的Agent Prompt

结合你的国际化项目。

Agent目标：

```text
把React项目国际化
```

Agent Prompt不会写：

```text
请国际化项目
```

而是：

```text
Role:
I18N Migration Agent

Goal:
完成React项目国际化改造

Tools:
FileSearch
ASTParser
Translator
PatchFile

Rules:
1. 优先分析项目结构
2. 自动发现中文硬编码
3. 提取翻译资源
4. 生成locale文件
5. 修改源代码
6. 输出变更报告

Stop Condition:
所有中文硬编码处理完成
```

然后Agent运行：

```text
Thought
↓
扫描目录

Action
↓
ReadFile

Observation
↓
发现中文

Thought
↓
提取中文

Action
↓
Translator

Observation
↓
得到翻译

Thought
↓
回填代码
```

这就是工业级Agent的真实工作方式。

---

## 十、现阶段最重要的认知

学习 ReAct 与 Agent Prompt 时，最容易犯的错误是：

```text
研究Prompt模板
```

而忽略：

```text
环境(Environment)
工具(Tools)
记忆(Memory)
循环(Loop)
评估(Eval)
```

实际上在2025~2026年，Agent性能提升最大的来源已经不是Prompt本身，而是：

```text
Tool Design
+
Skill Design
+
Workflow Design
+
Evaluation
```

Anthropic甚至明确提出：

> 成功的Agent系统通常由简单、可组合的模式构成，而不是复杂框架；很多场景应优先构建Workflow，而不是直接构建自主Agent。 ([Anthropic][1])

---

下一阶段如果继续深入，就应该进入 **Agent Architecture（Agent架构）**，包括：

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
