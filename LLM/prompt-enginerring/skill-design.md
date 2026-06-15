# Skill 设计方法论

## 前言

因为很多人在 2024 年学习：

```text
Prompt Engineering
```

到了 2025~2026 年开始发现：

```text
Prompt越来越不重要
Skill越来越重要
```

实际上这里存在一个误区，“Prompt 不是不重要了，而是 Prompt Engineering 的重要性下降了，但 Prompt Design 的重要性反而上升了。”


很多人看到 Skill、Agent、MCP、Workflow 出现后，会得出一个错误结论：

```text
以前：
Prompt

现在：
Skill

所以Prompt过时了
```

这是一个典型的认知误区。

---

### 用软件架构类比最容易理解

假设有人说：

```text
有了微服务

所以函数设计不重要了
```

你会怎么想？

显然不对。

因为：

```text
微服务
↓
Service
↓
Class
↓
Function
```

微服务再高级：

最终还是函数在干活。

---

AI系统也是一样：

```text
Agent
↓
Workflow
↓
Skill
↓
Prompt
↓
Token
```

Skill再高级：

最终执行任务的还是Prompt。

---

### 第一层认知：Prompt没有消失

很多人认为：

```text
Skill
```

长这样：

```yaml
name: translate-skill
input:
  text
output:
  translatedText
```

然后结束。

实际上不是。

内部通常是：

```text
translate-skill
│
├─ Prompt
├─ Examples
├─ Rules
├─ Validation
└─ Output Schema
```

本质：

```text
Skill
=
Prompt的工程化封装
```

而不是Prompt的替代品。

---

## 第二层认知：Skill让Prompt从显性变成隐性

以前：

用户自己写Prompt：

```text
你是一名翻译专家

请翻译以下内容

要求：
...
```

---

现在：

用户调用：

```typescript
translateSkill.run()
```

---

Prompt去哪了？

藏进Skill里了。

---

所以：

```text
Prompt消失了吗？

没有
```

只是：

```text
从用户视角消失了
```

---

类似：

以前：

```javascript
fetch()
```

自己写HTTP。

现在：

```javascript
axios.get()
```

HTTP消失了吗？

没有。

只是封装了。

---

## 第三层认知：Skill质量取决于Prompt质量

举个真实例子。

假设你做：

```text
translation-skill
```

---

版本1：

```text
翻译下面内容
```

---

版本2：

```text
你是一名专业软件国际化翻译专家

规则：

1. 保留变量
2. 保留HTML
3. 保留占位符
4. 保留Markdown

示例：
...

输出JSON
```

---

同一个Skill：

效果可能差10倍。

---

所以：

Skill质量很大程度上来自：

```text
Prompt质量
```

---

## 真正发生变化的是Prompt Engineer的职责

2023年的Prompt Engineer：

主要工作：

```text
写Prompt
```

例如：

```text
写营销文案Prompt
写翻译Prompt
写总结Prompt
```

---

2026年的Prompt Engineer：

主要工作：

```text
设计Skill
设计Workflow
设计Agent
设计Tool Use
设计Evaluation
```

Prompt只是其中一部分。

---

变化类似于：

```text
前端工程师
↓
全栈工程师
```

不是前端没用了。

而是职责扩大了。

---

## Prompt Engineering正在分化

实际上现在已经出现两种Prompt Engineering。

---

### 第一种：Prompt Writing

提示词编写

例如：

```text
帮我写一个爆款小红书Prompt
```

这种门槛越来越低。

模型自己都能生成。

价值越来越低。

---

### 第二种：Prompt Architecture

提示词架构

例如：

```text
Prompt如何拆分

Prompt如何复用

Prompt如何测试

Prompt如何版本化

Prompt如何组合成Skill
```

价值越来越高。

---

未来企业更需要的是：

```text
Prompt Architect
```

而不是：

```text
Prompt Writer
```

---

## Skill时代最重要的能力

很多人以为：

```text
Skill Creator
```

主要能力是：

```text
会写MCP
会写Agent
会写Workflow
```

其实不是。

核心能力仍然是：

```text
能力抽象
边界设计
Prompt设计
Contract设计
```

---

举个国际化项目例子。

假设你设计：

```text
translation-skill
```

你需要思考：

#### 输入是什么

```typescript
interface Input {
  text: string;
  sourceLang: string;
  targetLang: string;
}
```

---

#### 输出是什么

```typescript
interface Output {
  translatedText: string;
}
```

---

#### Prompt怎么写

```text
保留变量
保留HTML
保留Markdown
保留占位符
```

---

#### 如何验证

```text
变量是否丢失
HTML是否损坏
JSON是否有效
```

---

#### 如何评估

```text
准确率
术语一致性
格式正确率
```

---

你会发现：

整个Skill里面最复杂的部分之一，

仍然是：

```text
Prompt Design
```

---

## 为什么很多Skill项目最后失败

我见过很多团队：

```text
Agent
Workflow
MCP
Graph
Supervisor
```

全都做了。

---

结果：

效果很差。

原因是什么？

打开一看：

```text
Skill内部Prompt：

请帮我翻译以下内容
```

结束。

---

于是：

```text
Agent很高级
Skill很高级
Workflow很高级
```

但底层能力很弱。

---

就像：

```text
微服务架构
```

做得再漂亮。

如果里面全是：

```java
public void process() {
}
```

一样没价值。

---

## 2026年更准确的技术栈

我更倾向于这样理解：

```text
Prompt
=
能力实现层

Skill
=
能力封装层

Workflow
=
能力编排层

Agent
=
能力决策层

MCP
=
能力接入层
```

关系是：

```text
MCP
 ↓
Agent
 ↓
Workflow
 ↓
Skill
 ↓
Prompt
 ↓
Model
```

---

所以真正正确的结论应该是：

❌ 错误说法：

```text
有了Skill之后
Prompt Engineering已经不重要了
```

✅ 更准确的说法：

```text
有了Skill之后

Prompt Writing的重要性下降了

Prompt Architecture的重要性上升了
```

以及：

```text
Prompt Engineer
↓
Skill Creator
↓
Agent Architect
```

这是一种能力升级关系，而不是替代关系。

对于你这种前端架构背景的人，如果未来想做 AI 应用架构，最值得投入的能力排序其实是：

```text
1 Prompt Design
2 Skill Design
3 Workflow Design
4 Agent Design
5 MCP Design
```

因为后面四层，最终都建立在第一层之上。一个设计糟糕的 Prompt，包装成 Skill 不会变成好 Skill；几十个差 Skill 组成的 Workflow，也不会变成好 Agent。


现在很多 AI 开发框架：

- Claude Skills
- OpenAI Agent
- LangGraph
- CrewAI
- AutoGen
- Semantic Kernel
- MCP Ecosystem

实际上都在围绕一个核心概念：

> Skill（技能）

展开。

如果说：

```text
Prompt = 函数内部实现
```

那么：

```text
Skill = 对外暴露的能力单元
```

---

# 第一章：什么是 Skill

先用费曼学习法解释。

假设你招了一个前端工程师。

你给他一个任务：

```text
给项目做国际化
```

他需要：

```text
扫描代码
↓
提取中文
↓
翻译
↓
生成语言包
↓
回填代码
↓
提交Git
```

你会发现：

这不是一个动作。

而是很多能力的组合。

---

在 AI 世界里也是一样。

例如：

```text
翻译能力
```

其实就是一个 Skill。

输入：

```json
{
  "source": "你好"
}
```

输出：

```json
{
  "target": "Hello"
}
```

---

所以：

# Skill定义

Skill 是：

> 一个可以被 AI 调用、复用、编排、组合的能力单元。

类似：

```text
软件开发

Function
Class
Service

AI开发

Prompt
Skill
Agent
```

对应关系：

```text
Prompt
↓
Skill
↓
Workflow
↓
Agent
↓
AI System
```

---

# 第二章：Skill 和 Prompt 的区别

很多新人会混淆。

实际上：

## Prompt

关注：

```text
怎么做
```

例如：

```text
你是一名翻译专家

请翻译下面内容
```

---

## Skill

关注：

```text
做什么
```

例如：

```yaml
skill:
  name: translation
```

---

软件工程类比：

```text
Prompt
=
函数实现

Skill
=
函数接口
```

例如：

```typescript
function translate(text: string): string;
```

调用方根本不关心内部 Prompt。

---

所以：

```text
Prompt是实现

Skill是抽象
```

---

# 第三章：Skill设计的五层架构

企业级Skill设计通常分五层。

```text
Skill
├── Identity
├── Contract
├── Workflow
├── Tool
└── Guardrail
```

这是核心模型。

---

# 第一层：Identity

Skill身份定义

---

例如：

```yaml
name: translation-skill

description: Translate Chinese text into target language
```

---

很多人写：

```yaml
name: skill1
```

这种设计是错误的。

---

Skill名称必须：

```text
明确
稳定
可搜索
可复用
```

例如：

```text
translation-skill
code-review-skill
i18n-extract-skill
react-refactor-skill
```

---

# 第二层：Contract

这是最重要的一层。

类似：

```typescript
interface Skill
```

---

例如：

```typescript
interface TranslationInput {
  text: string;
  sourceLanguage: string;
  targetLanguage: string;
}
```

---

输出：

```typescript
interface TranslationOutput {
  translatedText: string;
}
```

---

这叫：

# Skill Contract

---

原则：

```text
输入必须明确

输出必须明确
```

---

否则：

Agent无法协调。

---

# 第三层：Workflow

Skill内部流程。

---

很多人设计：

```text
一个Prompt
```

然后结束。

---

企业级Skill：

```text
Input
 ↓
Validate
 ↓
Reason
 ↓
Tool
 ↓
Review
 ↓
Output
```

---

例如翻译Skill：

```text
读取文本
↓
识别语言
↓
翻译
↓
术语校验
↓
格式校验
↓
输出
```

---

# 第四层：Tool

Skill并不一定靠Prompt。

可能调用：

```text
搜索工具
数据库
Git
文件系统
浏览器
API
MCP
```

---

例如：

```text
Github Skill
```

内部：

```text
Prompt
+
GitHub API
```

---

例如：

```text
I18N Skill
```

内部：

```text
Prompt
+
AST Parser
+
Translation API
```

---

所以：

```text
Skill ≠ Prompt
```

而是：

```text
Skill = Prompt + Tool
```

---

# 第五层：Guardrail

守护规则。

这是Skill设计最容易忽略的部分。

---

例如：

国际化Skill。

要求：

```text
不能修改逻辑代码
不能修改变量名
不能修改接口定义
```

---

这些属于：

```text
Guardrail
```

---

作用：

```text
限制AI自由度
```

---

# 第四章：Skill设计七原则

这是最重要部分。

---

# 原则1：单一职责

类似SOLID。

---

错误：

```text
国际化Skill

负责：

提取
翻译
回填
提交Git
```

---

正确：

```text
extract-skill

translate-skill

patch-skill

git-skill
```

---

一个Skill只干一件事。

---

# 原则2：高内聚

Skill内部流程必须强相关。

---

例如：

```text
翻译
术语校验
语言识别
```

属于同一个Skill。

---

但：

```text
翻译
数据库迁移
```

不应该放一起。

---

# 原则3：低耦合

Skill之间：

通过Contract通信。

不要共享Prompt。

---

错误：

```text
SkillA知道SkillB内部逻辑
```

---

正确：

```text
SkillA
↓
JSON
↓
SkillB
```

---

# 原则4：幂等

同样输入：

```text
输入A

执行100次
```

结果应一致。

---

否则Agent无法重试。

---

# 原则5：可测试

必须可以：

```text
Input
↓
Output
```

独立验证。

---

例如：

```json
{
  "input": "你好"
}
```

---

期待：

```json
{
  "output": "Hello"
}
```

---

# 原则6：可观测

Skill必须输出：

```text
执行日志
执行步骤
执行结果
错误信息
```

---

否则无法调试。

---

# 原则7：可组合

最重要原则。

---

Skill必须能够：

```text
单独运行
```

同时：

```text
被Agent调用
```

---

例如：

```text
translate-skill
```

既能独立执行。

又能被：

```text
i18n-agent
```

调用。

---

# 第五章：Skill设计模式

这是Prompt Design Pattern的升级版。

---

## Pattern 1：Atomic Skill

原子技能

---

例如：

```text
translate
```

只负责翻译。

---

特点：

```text
简单
稳定
复用率高
```

---

## Pattern 2：Pipeline Skill

流水线技能

---

例如：

```text
scan
↓
extract
↓
translate
↓
patch
```

---

适合：

```text
国际化
代码生成
数据处理
```

---

## Pattern 3：Planner Skill

规划技能

---

负责：

```text
拆任务
生成计划
```

---

例如：

```text
分析项目

输出：

Step1
Step2
Step3
```

---

## Pattern 4：Reviewer Skill

审查技能

---

负责：

```text
找错误
找风险
找遗漏
```

---

类似：

```text
Code Review
```

---

## Pattern 5：Supervisor Skill

监督技能

企业级Agent核心。

---

结构：

```text
Supervisor
│
├─ Extract Skill
├─ Translate Skill
├─ Patch Skill
└─ Git Skill
```

---

负责：

```text
调度
重试
监控
汇总
```

---

# 第六章：国际化项目案例

你最近一直在研究国际化。

这个案例最典型。

---

错误设计：

```text
I18N Skill

负责全部工作
```

---

最终：

```text
5000行Prompt
```

没人维护。

---

正确设计：

```text
Frontend Scan Skill
```

负责：

```text
扫描React代码
识别中文
```

---

```text
Extraction Skill
```

负责：

```text
提取资源
```

---

```text
Translation Skill
```

负责：

```text
翻译
术语一致性
```

---

```text
Patch Skill
```

负责：

```text
回填代码
```

---

```text
Validation Skill
```

负责：

```text
验证编译
验证缺失翻译
```

---

```text
Git Skill
```

负责：

```text
Commit
PR
Merge
```

---

最后：

```text
Supervisor Agent
```

编排：

```text
Scan
 ↓
Extract
 ↓
Translate
 ↓
Patch
 ↓
Validate
 ↓
Git
```

---

# 第七章：2026 Skill设计成熟架构

现代企业级AI系统已经不是：

```text
Prompt
```

而是：

```text
Prompt
↓
Skill
↓
Tool
↓
Workflow
↓
Agent
↓
MCP
↓
AI Platform
```

对于你这种前端 + 架构背景的人，可以直接这样理解：

```text
Prompt = Function Body

Skill = Interface

Tool = SDK

Workflow = Service Layer

Agent = Application Layer

MCP = Micro Service

AI Platform = Distributed System
```

当你能设计：

```text
Skill Contract
Skill Boundary
Skill Workflow
Skill Composition
Skill Governance
```

时，你就已经从 Prompt Engineer 进入 AI Architect 的阶段了。
