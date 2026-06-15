# 新风格的 Prompt Engineering

在使用ClaudeCode、Codex这类Agent的过程中，是否还需要按照PromptEngineering规范去写，是否还用到Few-shot pattern、Cot、Chain of Prompt 这些"技巧"？

这是一个非常好的问题，而且恰恰是 2025~2026 年 Prompt Engineering 领域最大的认知变化之一。

短答案：

> **需要，但用法已经发生了根本变化。**
>
> Claude Code、Codex、Cursor Agent、OpenAI Agent 时代，不是 Prompt Engineering 消失了，而是 Prompt Engineering 从「写提示词」升级成了「设计 Agent 行为」。

很多 2023 年的 Prompt 技巧已经降级为基础能力，而一些新的能力（Tool Design、Skill Design、Workflow Design）变成了核心竞争力。

---

# 第一层：Agent 时代还需要 Prompt Engineering 吗？

答案：

**100%需要。**

举个例子。

很多人觉得：

```text
Claude Code
↓
自己会思考
自己会写代码
自己会调用工具
```

所以：

```text
Prompt不重要了
```

这是错觉。

实际上：

Claude Code 内部仍然运行着大量 Prompt。

大致结构类似：

```text
System Prompt
    ↓
Tool Instructions
    ↓
Memory Context
    ↓
User Prompt
    ↓
Tool Result
    ↓
Next Prompt
```

整个 Agent Runtime 本质上就是：

```text
大量Prompt不断拼接
```

只是你看不见而已。

---

例如：

你输入：

```text
帮我把这个React项目国际化
```

Claude Code 内部可能经历：

```text
Prompt1:
分析项目结构

Prompt2:
识别中文硬编码

Prompt3:
生成locale

Prompt4:
修改代码

Prompt5:
验证结果
```

你只看到一句话。

实际上已经执行了很多 Prompt。

---

所以：

# Agent ≠ 不需要 Prompt

而是：

```text
Prompt
+
Tool
+
Memory
+
Loop
```

---

# 第二层：Few-shot 还重要吗？

答案：

重要。

但使用场景变了。

---

## 2023年

典型写法：

```text
输入：
你好

输出：
Hello

输入：
谢谢

输出：
Thank you

输入：
再见
```

这是 Few-shot。

---

## 2026年

模型本身已经非常强。

对于：

- GPT-5
- Claude Opus
- Claude Sonnet
- Codex

很多简单任务：

```text
Few-shot
=
收益很小
```

---

例如：

```text
翻译下面内容
```

已经不需要 Few-shot。

---

但是：

对于复杂格式任务：

```text
生成YARA规则

生成测试用例

生成SQL

生成代码Review报告
```

Few-shot仍然是效果提升最大的手段之一。

---

例如：

```text
以下是优秀Code Review示例

Example1:
...

Example2:
...

请按照同样风格Review
```

效果通常远超：

```text
请Review代码
```

---

所以：

现代Few-shot的定位是：

```text
不是教模型知识

而是教模型风格
教模型格式
教模型决策模式
```

---

# 第三层：CoT还重要吗？

这里变化最大。

---

## 2023年

经典技巧：

```text
Let's think step by step
```

或者：

```text
一步一步分析
```

---

当时能大幅提升准确率。

---

## 2025-2026

OpenAI官方已经多次强调：

对于现代推理模型：

- GPT-5
- o系列
- Claude推理模型

不要过度强制CoT。

原因：

模型本身已经会推理。

例如：

```text
计算复杂问题
```

你写：

```text
一步一步思考
```

收益很有限。

有时反而变差。

---

现代推荐方式：

不要写：

```text
请一步一步思考
```

而写：

```text
先分析需求
再给出方案
最后评估风险
```

即：

```text
描述任务结构
而非思维过程
```

---

所以：

### 老CoT

```text
告诉模型如何思考
```

---

### 新CoT

```text
告诉模型完成什么阶段
```

---

# 第四层：Chain of Prompt 还重要吗？

这个反而越来越重要。

甚至比以前重要。

---

以前：

```text
一个超级Prompt
```

5000字。

---

现在：

越来越多Agent采用：

```text
Prompt A
 ↓
Prompt B
 ↓
Prompt C
```

---

例如国际化项目。

第一步：

```text
扫描代码
```

---

第二步：

```text
提取中文
```

---

第三步：

```text
翻译
```

---

第四步：

```text
校验
```

---

第五步：

```text
回填
```

---

这就是：

```text
Prompt Chaining
```

或者：

```text
Prompt Workflow
```

---

实际上：

Anthropic 的很多 Agent Pattern 本质就是 Prompt Chaining。

---

# 第五层：ReAct Prompt 还需要写吗？

一般开发者：

基本不用。

---

2023年：

你会看到：

```text
Thought:
...

Action:
...

Observation:
...
```

这种Prompt。

---

现在：

Claude Code、Codex已经内置。

你不用自己写：

```text
Thought:
```

也不用写：

```text
Action:
```

---

因为Agent Runtime已经帮你做了。

---

但是：

ReAct思想仍然存在。

只是：

```text
显式ReAct Prompt
```

变成了：

```text
隐式Agent Loop
```

---

例如：

你写：

```text
分析项目并修复Bug
```

Claude Code内部其实在：

```text
Thought
↓
Read File

Observation
↓
Thought

Action
↓
Edit File

Observation
↓
Thought
```

只是你看不见。

---

# 第六层：真正重要的东西变了

如果把 Prompt Engineering 分代：

---

## 第一代 Prompt Engineer

关注：

```text
Role
Few-shot
CoT
Output Format
```

---

## 第二代 Prompt Engineer

关注：

```text
Prompt
+
RAG
```

---

## 第三代 Agent Engineer

关注：

```text
Tool Design
Skill Design
Workflow Design
Memory Design
Evaluation
```

---

例如：

同样一个Agent。

差距往往不是：

```text
Prompt写得好不好
```

而是：

```text
工具设计得好不好
```

---

举例：

国际化Agent。

方案A：

```text
一个超级Prompt
```

---

方案B：

```text
Skill1
扫描项目

Skill2
抽取中文

Skill3
翻译

Skill4
校验

Skill5
回填
```

---

几乎一定是方案B胜出。

---

# 第七层：对于你这种开发者最应该学什么？

结合你的背景（前端、架构、Monorepo、国际化改造、Claude Code）。

我建议学习优先级如下：

### 第一优先级

Prompt基础

- Role
- Context
- Constraint
- Output Format

必须会。

---

### 第二优先级

Agent Prompt

- Goal
- Tool Rules
- Planning Rules
- Stop Condition

---

### 第三优先级

Prompt Chaining

例如：

```text
Scan
 ↓
Extract
 ↓
Translate
 ↓
Validate
 ↓
Patch
```

---

### 第四优先级

Skill Design

例如：

```text
frontend-skill
translation-skill
i18n-skill
git-skill
```

---

### 第五优先级

Agent Architecture

Anthropic 当前最推荐的几个模式：

- Prompt Chaining
- Routing
- Parallelization
- Orchestrator-Worker
- Evaluator-Optimizer

这些已经比 Few-shot、CoT 更接近生产环境核心能力。

---

可以把整个演进过程记成一句话：

```text
2023：
研究如何写Prompt

2024：
研究如何组织Prompt

2025：
研究如何设计Workflow

2026：
研究如何设计Agent系统
```

而 Claude Code、Codex、OpenAI Agent 时代，真正拉开差距的往往已经不是一句 Prompt，而是整个 Agent Runtime（Prompt + Skill + Tool + Memory + Workflow）的设计。
