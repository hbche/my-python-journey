# Prompt Learning By LLM

本系列记录通过 LLM 学习 Prompt Engineering 相关知识。

很多人学Prompt Engineering最大的误区是：

- 学几十个技巧
- 收藏几百个Prompt模板
- 背CoT、ReAct、ToT等名词

最后不会设计Prompt。

真正的Prompt Engineering，本质上是：

> **人与LLM之间的接口设计（Human-LLM Interface Design）**

类似于：

- API设计
- 前端组件设计
- 数据库Schema设计

Prompt不是一句话，而是一个系统。

---

## 第一阶段：什么是Prompt？

先从最底层开始。

### 如果把LLM当成一个人

假设你招了一个实习生。

你说：

> 帮我写代码。

他会懵。

因为：

- 写什么代码？
- 什么语言？
- 什么框架？
- 输出什么格式？
- 谁看？

信息不够。

---

如果你这样说：

```text
你是一名资深React工程师。

请使用React18 + TypeScript开发一个登录页面。

要求：

1. 使用函数组件
2. 使用Hooks
3. 使用Ant Design
4. 包含邮箱和密码输入框
5. 输出完整代码
```

结果立刻变好。

为什么？

因为你补充了：

- 角色
- 任务
- 约束
- 输出格式

---

所以：

## Prompt = 给模型的工作说明书

可以写成：

```text
Prompt = Context + Task + Constraint + Output
```

即：

```text
Prompt =
背景信息
+
任务目标
+
执行规则
+
输出格式
```

这是Prompt Engineering第一原则。

---

## 第二阶段：LLM到底在干什么？

理解Prompt之前必须理解LLM。

很多人认为：

```text
Prompt -> AI思考 -> 答案
```

实际上不是。

真实过程：

```text
Prompt
↓
Token化
↓
预测下一个Token
↓
预测下一个Token
↓
预测下一个Token
↓
...
```

本质：

> LLM是一个超大型概率预测器

它不知道对错。

它只知道：

```text
当前上下文下
哪个Token概率最高
```

例如：

```text
中国的首都是
```

下一词：

```text
北京
```

概率极高。

---

因此得到Prompt第二原则：

## Prompt的本质是控制概率分布

不是告诉模型：

```text
做什么
```

而是：

```text
让正确答案的概率变高
让错误答案的概率变低
```

这是Prompt Engineer最重要的认知升级。

---

## 第三阶段：Prompt由什么组成？

现代Prompt基本由6层构成。

```text
Prompt
├── Role
├── Context
├── Task
├── Constraint
├── Example
└── Output Format
```

下面逐个讲。

---

## 1 Role（角色）

例如：

```text
你是一名资深Java架构师
```

或者：

```text
你是一名国际化专家
```

作用：

让模型激活相关知识区域。

类似：

```text
切换专家模式
```

---

例如：

```text
解释微服务
```

和

```text
你是一名阿里P10架构师，请解释微服务
```

结果完全不同。

---

Role本质：

```text
缩小概率空间
```

---

## 2 Context（上下文）

例如：

```text
项目情况：

React18
TypeScript
Monorepo
pnpm workspace
```

这就是Context。

---

没有Context：

```text
如何国际化？
```

模型会给通用答案。

---

有Context：

```text
现有项目：

React18
TypeScript
Monorepo
Vite
pnpm workspace

需要改造历史项目国际化
```

答案立刻精准。

---

所以：

```text
垃圾输入
=
上下文不足
```

很多时候不是模型笨。

是Context太少。

---

## 3 Task（任务）

任务必须明确。

坏Prompt：

```text
帮我优化代码
```

好Prompt：

```text
找出性能瓶颈
并给出优化方案
```

更好：

```text
分析以下React组件：

1. 找出性能问题
2. 说明原因
3. 给出修改代码
4. 评估收益
```

---

Prompt原则：

```text
模糊任务
=
模糊结果
```

---

## 4 Constraint（约束）

约束是Prompt质量提升最快的方法。

例如：

```text
不要修改接口定义
不要修改数据库
不要引入第三方库
```

模型会自动收敛。

---

没有约束：

```text
天马行空
```

有约束：

```text
工程可落地
```

---

## 5 Example（示例）

这是Prompt Engineering里极其重要的部分。

叫：

```text
Few-shot Learning
```

例如：

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

模型会继续：

```text
Goodbye
```

---

因为：

模型非常擅长模仿模式。

不擅长猜规则。

---

所以有句话：

> Don't tell. Show.

不要解释规则。

直接给例子。

---

## 6 Output Format

很多Prompt失败原因：

输出格式不明确。

例如：

```text
返回JSON
```

远远不够。

---

应该：

```json
{
  "title": "",
  "summary": "",
  "risk": []
}
```

直接给Schema。

---

这会极大提高稳定性。

---

## 第四阶段：Prompt工程的核心技术栈

现在进入真正的Prompt Engineering。

现代Prompt技术大致分五代。

```text
Gen1 直接提问
Gen2 Few-shot
Gen3 Chain of Thought
Gen4 Agent/ReAct
Gen5 Tool Use + Workflow
```

---

### 第一代：Zero-shot

直接问。

```text
解释什么是Rust所有权
```

最简单。

---

### 第二代：Few-shot

给例子。

```text
例子1
例子2
例子3

现在处理新问题
```

---

### 第三代：CoT

Chain of Thought

思维链。

例如：

```text
请一步一步分析
```

本质：

让模型生成中间推理过程。

---

效果：

```text
复杂问题准确率大幅提升
```

---

### 第四代：ReAct

Reason + Act

模型：

```text
思考
↓
调用工具
↓
观察结果
↓
继续思考
```

这就是Agent基础。

---

### 第五代：Workflow

现在工业界主流。

不是：

```text
一个超级Prompt
```

而是：

```text
Prompt A
↓
Prompt B
↓
Prompt C
↓
Prompt D
```

组成工作流。

---

例如国际化项目：

```text
代码扫描Prompt
↓
字符串抽取Prompt
↓
翻译Prompt
↓
校验Prompt
↓
回填Prompt
```

这已经是AI Workflow。

不是单Prompt。

---

## 第五阶段：高级Prompt工程

开始接近专家层。

Prompt其实和软件架构越来越像。

---

### Prompt模块化

不要：

```text
5000行超级Prompt
```

要：

```text
Role Prompt
Task Prompt
Format Prompt
```

拆分。

---

类似：

```text
组件化
```

---

### Prompt版本管理

例如：

```text
prompt-v1
prompt-v2
prompt-v3
```

和代码一样管理。

---

### Prompt测试

建立测试集：

```text
100个输入
```

跑Prompt。

观察：

```text
准确率
格式正确率
幻觉率
```

---

这就是Prompt Evaluation。

---

## 第六阶段：未来Prompt Engineering会变成什么？

2023：

```text
写Prompt
```

2024：

```text
Prompt + RAG
```

2025：

```text
Prompt + Agent
```

2026开始越来越明显：

```text
Prompt
+
Skill
+
Tool
+
Workflow
+
Memory
+
MCP
```

形成完整AI系统。

---

对于有前端、架构、Monorepo背景的人，可以把Prompt Engineering理解成：

```text
Prompt = Interface

Skill = Function

Tool = SDK

MCP = Service

Agent = Runtime

Workflow = Orchestration

Memory = Database
```

那么一个复杂国际化系统就会变成：

```text
Frontend Skill
    ↓
I18N Extraction Skill
    ↓
Translation Skill
    ↓
Validation Skill
    ↓
Patch Skill
    ↓
Git Commit Skill
```

每个Skill内部都有自己的Prompt。

而Prompt只是整个系统中最底层的一层。

---

## 学习大纲

如果继续深入，下一步应该学习的是：

1. 什么是 Prompt Engineering？本质 + 组成部分 + 实战
2. Prompt 设计模式
3. Cot、Self-Consistency、Tree of Thoughts
4. ReAct 与 Agent Prompt
5. AI Workflow 架构设计
6. Prompt 测试与评估体系(Prompt Evals)
7. 企业级 Prompt 架构(大型AI应用如何组织数百个 Prompt)
8. Skill 设计方法论
9. MCP 设计方法论
