# Agent时代第一课：Prompt Chaining（提示链）

如果说：

* Prompt Engineering 是写函数
* ReAct 是让模型思考和行动
* Agent 是具备自主能力的系统

那么：

> Prompt Chaining 是所有 Agent Architecture 的起点。

事实上，无论是 OpenAI 还是 Anthropic，目前都不建议开发者一开始就构建 Autonomous Agent（自主Agent）。

Anthropic 在《Building Effective Agents》中明确提出：

> 在大多数业务场景中，Workflow 往往比 Agent 更可靠、更可控、更容易调试。Agent 应该是最后选择，而不是第一选择。

因此：

```text
Agent学习路线

Prompt
 ↓
Prompt Chaining
 ↓
Workflow
 ↓
Tool Use
 ↓
Router
 ↓
Orchestrator
 ↓
Single Agent
 ↓
Multi Agent
```

Prompt Chaining 是整个体系的基础。

---

# 一、什么是 Prompt Chaining？

先看一个错误示例。

用户：

```text
帮我分析一个React项目，
输出架构文档，
生成国际化方案，
最后生成实施计划。
```

很多人会写：

```text
一个5000行超级Prompt
```

例如：

```text
分析项目...
生成架构...
生成国际化...
生成实施计划...
输出markdown...
```

这种叫：

```text
Monolithic Prompt
（单体Prompt）
```

类似：

```text
10000行God Class
```

软件工程里早就证明：

这种方案不可维护。

---

Prompt Chaining思想完全不同。

它会拆解任务。

```text
Prompt A
    ↓
Prompt B
    ↓
Prompt C
    ↓
Prompt D
```

例如：

```text
项目分析
 ↓
架构识别
 ↓
国际化设计
 ↓
实施计划
```

每一步只干一件事。

这就是：

> Prompt Chaining = 将复杂任务拆解为多个可验证的小步骤。

这是 Anthropic 官方推荐的第一种 Workflow Pattern。

---

# 二、为什么 Prompt Chaining 有效？

理解这个问题非常重要。

很多人以为：

```text
GPT-5
Claude
足够聪明
```

所以：

```text
直接一次问完
```

就行。

实际上不是。

---

假设让一个新人做事。

你说：

```text
帮我完成项目国际化
```

新人会懵。

---

但如果拆成：

```text
步骤1：
扫描项目

步骤2：
提取中文

步骤3：
生成locale

步骤4：
替换代码

步骤5：
生成报告
```

成功率立即提高。

---

原因在于：

LLM最擅长：

```text
局部推理
```

而不是：

```text
超长链路推理
```

---

OpenAI 官方文档对此有类似建议：

复杂任务应拆分为多个步骤，让模型逐步完成，而不是试图通过单个Prompt完成全部工作。

---

# 三、Prompt Chaining 本质是什么？

本质上：

```text
Prompt Chaining
=
Pipeline
```

类似后端数据处理流水线。

---

例如：

```text
原始日志
 ↓
解析
 ↓
清洗
 ↓
聚合
 ↓
统计
 ↓
报告
```

---

Agent Workflow也是一样。

```text
用户输入
 ↓
理解意图
 ↓
信息收集
 ↓
分析
 ↓
决策
 ↓
输出
```

---

所以：

Prompt Chaining本质不是Prompt技巧。

而是：

```text
任务分解技术
```

(Task Decomposition)

这是Agent Architecture最核心能力之一。

---

# 四、Prompt Chaining 的标准结构

Anthropic官方Workflow可以抽象为：

```text
Input
 ↓
Prompt1
 ↓
Intermediate Result
 ↓
Prompt2
 ↓
Intermediate Result
 ↓
Prompt3
 ↓
Output
```

例如：

```text
用户需求
 ↓
需求分析Prompt
 ↓
需求文档

需求文档
 ↓
架构设计Prompt
 ↓
架构方案

架构方案
 ↓
实施计划Prompt
 ↓
最终输出
```

---

注意：

这里出现了一个关键概念。

# Intermediate State

中间状态。

---

Agent系统其实是：

```text
状态机(State Machine)
```

每个Prompt：

```text
输入状态
 ↓
处理
 ↓
输出状态
```

---

例如：

```json
{
  "task":"国际化"
}
```

↓

```json
{
  "modules":[
     "login",
     "dashboard"
  ]
}
```

↓

```json
{
   "translations":[]
}
```

↓

```json
{
   "patches":[]
}
```

---

这就是现代Agent设计思想。

---

# 五、Prompt Chaining 的经典模式

Anthropic官方Workflow主要有几种模式。

Prompt Chaining是第一种。

---

## 模式1：Sequential Chain

顺序链

最简单。

```text
A
↓
B
↓
C
↓
D
```

例如：

```text
代码扫描
↓
提取中文
↓
翻译
↓
回填
```

---

特点：

```text
简单
稳定
容易调试
```

适合：

```text
任务有依赖关系
```

---

## 模式2：Conditional Chain

条件链

```text
        A
       / \
      /   \
     B     C
      \   /
       \ /
        D
```

---

例如：

```text
识别项目类型
```

如果：

```text
React
```

走：

```text
React I18N Flow
```

如果：

```text
Angular
```

走：

```text
Angular I18N Flow
```

---

这其实已经接近：

```text
Router
```

后面会专门讲。

---

## 模式3：Iterative Chain

迭代链

```text
生成
 ↓
评审
 ↓
修改
 ↓
评审
 ↓
修改
```

---

例如：

```text
生成翻译
 ↓
质量检查
 ↓
修正翻译
```

---

这已经接近：

```text
Evaluator-Optimizer Pattern
```

也是Anthropic推荐模式之一。

---

# 六、Prompt Chaining 与 ReAct 的区别

很多人混淆。

---

Prompt Chaining：

```text
开发者定义路径
```

例如：

```text
A
↓
B
↓
C
```

固定。

---

ReAct：

```text
模型决定路径
```

例如：

```text
Thought
↓
Action
↓
Observation
```

循环。

---

举例：

Prompt Chaining：

```text
扫描
↓
翻译
↓
回填
```

固定。

---

ReAct：

```text
发现问题
↓
搜索资料
↓
发现更多问题
↓
继续搜索
```

动态。

---

所以：

```text
Prompt Chaining
=
Workflow

ReAct
=
Reasoning Loop
```

这是两种完全不同架构。

---

# 七、工业级 Prompt Chaining

以你的国际化项目为例。

---

## Stage1

代码分析Agent

输入：

```text
项目源码
```

输出：

```json
{
  "framework":"React",
  "language":"TypeScript",
  "modules":[]
}
```

---

## Stage2

中文抽取Agent

输入：

```json
{
  "modules":[]
}
```

输出：

```json
{
  "hardcoded_strings":[]
}
```

---

## Stage3

翻译Agent

输入：

```json
{
  "hardcoded_strings":[]
}
```

输出：

```json
{
  "translations":[]
}
```

---

## Stage4

Patch Agent

输入：

```json
{
  "translations":[]
}
```

输出：

```json
{
  "patches":[]
}
```

---

## Stage5

Review Agent

输入：

```json
{
  "patches":[]
}
```

输出：

```json
{
  "approved":true
}
```

---

这已经是典型企业级AI Workflow。

注意：

这里甚至还没有Agent。

只有Workflow。

---

# 八、Prompt Chaining 的设计原则

这是实际开发最重要部分。

---

## 原则1：每个Prompt只做一件事

错误：

```text
分析+翻译+修复+测试
```

正确：

```text
一个Prompt
一个职责
```

类似：

```text
单一职责原则(SRP)
```

---

## 原则2：结构化输出

不要：

```text
自然语言
```

要：

```json
{
  "framework":"React"
}
```

因为：

下一步Prompt更容易消费。

---

## 原则3：中间结果可检查

例如：

```text
Step1结果
```

保存。

```text
Step2结果
```

保存。

---

这样：

```text
出错立即定位
```

---

## 原则4：失败可重试

例如：

```text
翻译失败
```

重新执行：

```text
Translation Step
```

而不是：

```text
整个流程重跑
```

---

# 九、为什么 Prompt Chaining 是 Agent 的基础？

因为后面所有Agent架构都建立在它之上。

例如：

## Router

实际上是：

```text
选择哪条Chain
```

---

## Orchestrator

实际上是：

```text
管理多个Chain
```

---

## Multi-Agent

实际上是：

```text
多个Chain协作
```

---

## OpenAI Deep Research

本质：

```text
Research Chain
 ↓
Reading Chain
 ↓
Reasoning Chain
 ↓
Writing Chain
```

---

Claude Code也是一样。

本质仍然是：

```text
Analyze
 ↓
Plan
 ↓
Edit
 ↓
Verify
```

多个Chain组合。

---

# 本课总结

先记住一句话：

> Prompt Chaining 不是 Prompt 技巧，而是 Agent 时代最基础的 Workflow Architecture。

核心思想：

```text
大任务
 ↓
任务分解
 ↓
多个Prompt
 ↓
状态传递
 ↓
最终结果
```

掌握 Prompt Chaining 后，下一课最自然的内容就是：

# Routing（路由模式）

因为当系统存在多个 Prompt Chain 时：

```text
用户请求
    ↓
应该走哪条Chain？
```

这就引出了 Agent Architecture 中第二个核心模式：

```text
Router Pattern
```

也是 Anthropic 官方 Workflow Patterns 的第二个关键组成部分。
