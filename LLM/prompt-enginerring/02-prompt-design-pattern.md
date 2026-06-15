# Prompt 设计模式

如果说前面讲的：

```text
Role
Context
Task
Constraint
Example
Output
```

属于 **Prompt的语法（Syntax）**，

那么接下来讲的：

```text
Prompt Design Pattern
```

属于：

> Prompt的设计模式（Architecture）

就像软件开发一样：

```text
变量 -> 语法
函数 -> 语法
类 -> 语法

MVC
DDD
CQRS
微服务

→ 设计模式
```

Prompt也是一样。

真正的Prompt Engineer和普通用户的区别，不是会不会写Prompt，而是：

```text
是否知道什么时候该用什么模式
```

---

## 第一章：什么是Prompt Design Pattern

先用费曼学习法解释。

假设你要让新人完成任务。

你发现：

有些说话方式总是有效。

例如：

```text
先分析再回答
```

总比：

```text
直接回答
```

效果好。

于是你总结出：

```text
分析 -> 回答
```

是一种稳定模式。

---

再例如：

```text
给几个示例
再处理新问题
```

总比直接讲规则效果好。

于是又得到一种模式：

```text
Example Pattern
```

---

因此：

### Prompt Design Pattern

定义：

> 在特定场景下，经过大量实践验证，能够稳定提升LLM效果的Prompt组织方式。

类似：

```text
单例模式
工厂模式
观察者模式
```

之于软件工程。

---

### Prompt模式分类

业内常见模式大约30~50种。

但本质可以归纳成6大类：

```text
1 思考类模式
2 分解类模式
3 示例类模式
4 约束类模式
5 验证类模式
6 Agent类模式
```

---

## 第一大类：思考类模式

这是最重要的一类。

---

### Pattern 1：Chain of Thought

思维链模式

简称：

```text
CoT
```

---

坏Prompt：

```text
计算：

一个商店进货100元
加价20%
打九折

利润是多少？
```

---

模型容易错。

---

改成：

```text
请一步一步分析：

1. 先计算售价
2. 再计算折后价格
3. 再计算利润
```

---

结果：

```text
100 × 1.2 = 120

120 × 0.9 = 108

利润 = 8
```

准确率明显提升。

---

为什么？

因为LLM本质：

```text
预测Token
```

复杂推理时：

```text
答案
↓
距离太远
```

容易跳错。

---

CoT作用：

```text
问题
↓
中间步骤
↓
答案
```

缩短推理跨度。

---

适用：

```text
数学
逻辑
代码分析
架构设计
```

---

### Pattern 2：Self Ask

自问自答模式

---

例如：

```text
分析一个微服务架构是否合理。

请先提出需要分析的问题，
然后逐个回答这些问题，
最后给出结论。
```

模型会变成：

```text
问题1：

服务边界是否合理？

回答...

问题2：

数据库是否共享？

回答...
```

---

这是高级架构分析Prompt常用模式。

---

### Pattern 3：Tree of Thoughts

树状思维模式

简称：

```text
ToT
```

---

普通CoT：

```text
一路走到底
```

---

ToT：

```text
方案A
 ├─ A1
 ├─ A2

方案B
 ├─ B1
 ├─ B2

方案C
 ├─ C1
 ├─ C2
```

最后比较。

---

例如：

```text
设计国际化方案

请至少提出3种方案

分析：

成本
风险
收益

最后选择最佳方案
```

---

架构设计特别适合。

---

## 第二大类：分解类模式

Prompt工程核心思想：

> 不要解决问题，先拆问题。

---

### Pattern 4：Least-to-Most

由浅入深模式

---

例如：

不要：

```text
帮我开发国际化系统
```

---

而是：

```text
Step1
识别中文

Step2
抽取资源

Step3
翻译资源

Step4
生成语言包

Step5
代码回填
```

---

复杂任务成功率暴涨。

---

这其实就是：

```text
Workflow Thinking
```

---

### Pattern 5：Task Decomposition

任务分解模式

---

例如：

代码审查。

不要：

```text
Review这段代码
```

---

改成：

```text
从以下维度分析：

1 性能
2 可维护性
3 安全性
4 可测试性
5 规范性
```

---

结果质量提升巨大。

---

## 第三大类：示例类模式

---

### Pattern 6：Few-shot Pattern

最经典模式。

---

例如国际化翻译：

不要解释：

```text
保留变量
保留HTML
保留占位符
```

---

直接给例子：

```text
输入：

Hello {name}

输出：

你好 {name}

----------------

输入：

Click <a>here</a>

输出：

点击<a>这里</a>
```

---

模型立刻学会规则。

---

原则：

```text
少讲规则
多给例子
```

---

### Pattern 7：Counter Example

反例模式

---

不仅告诉：

```text
正确是什么
```

还告诉：

```text
错误是什么
```

---

例如：

```text
正确：

你好 {name}

↓

Hello {name}
```

---

错误：

```text
Hello Robin
```

因为变量丢失。

---

模型边界会清晰很多。

---

## 第四大类：约束类模式

很多Prompt质量差：

不是能力问题。

是自由度太大。

---

### Pattern 8：Role Pattern

角色模式

---

例如：

```text
你是一名Google Staff Engineer
```

---

或者：

```text
你是一名国际化专家
```

---

作用：

```text
缩小搜索空间
```

---

### Pattern 9：Persona Pattern

人格模式

---

例如：

```text
用老师方式讲解

面向初学者
```

---

或者：

```text
像CTO一样评审方案
```

---

控制表达风格。

---

### Pattern 10：Output Schema Pattern

输出结构模式

---

不要：

```text
返回JSON
```

---

应该：

```json
{
  "risk": [],
  "benefit": [],
  "recommendation": ""
}
```

---

Prompt稳定性提升极大。

---

## 第五大类：验证类模式

这是很多人忽略的部分。

---

### Pattern 11：Reflection Pattern

反思模式

---

例如：

```text
完成回答后

检查：

1 是否遗漏需求
2 是否逻辑矛盾
3 是否存在错误
```

---

模型会二次修正。

---

### Pattern 12：Critic Pattern

批判者模式

---

例如：

```text
先生成方案

然后以架构委员会身份批判方案

最后重新优化方案
```

---

变成：

```text
Author
↓
Reviewer
↓
Fix
```

---

这已经接近真实工程流程。

---

### Pattern 13：Debate Pattern

辩论模式

---

例如：

```text
支持微服务的一方

反对微服务的一方

分别陈述观点

最后裁决
```

---

适合：

```text
技术选型
架构决策
产品决策
```

---

## 第六大类：Agent模式

这是2025~2026最重要的一类。

---

### Pattern 14：ReAct

Reason + Act

---

流程：

```text
思考
↓
行动
↓
观察
↓
继续思考
```

例如：

```text
发现项目中文
↓
读取文件
↓
分析内容
↓
继续处理
```

---

Agent几乎都基于这个模式。

---

### Pattern 15：Planner-Executor

规划者执行者模式

---

Agent最佳实践之一。

---

角色：

```text
Planner
```

负责：

```text
制定计划
```

---

角色：

```text
Executor
```

负责：

```text
执行任务
```

---

例如国际化：

```text
Planner

生成：

1 扫描项目
2 提取文本
3 翻译
4 校验
5 回填
```

---

然后：

```text
Executor
```

逐步执行。

---

### Pattern 16：Supervisor Pattern

监督者模式

这是企业级Agent最常见架构。

---

结构：

```text
Supervisor
│
├─ Frontend Skill
├─ Backend Skill
├─ Translation Skill
├─ QA Skill
└─ Git Skill
```

---

Supervisor负责：

```text
任务分配
结果汇总
错误重试
依赖管理
```

---

你之前提到的：

```text
国际化Skill
依赖
Frontend Skill
Translation Skill
```

本质就是：

```text
Supervisor Pattern
```

---

## 企业级Prompt设计模式体系

如果放到真实项目中，通常会组合使用：

```text
Role Pattern
+
Task Decomposition
+
Few-shot
+
CoT
+
Reflection
+
Output Schema
```

例如：

```text
你是一名国际化专家
(Role)

分析React项目
(Task)

按照步骤执行
(Decomposition)

参考以下示例
(Few-shot)

逐步思考
(CoT)

完成后自检
(Reflection)

最终输出JSON
(Output Schema)
```

这已经是工业级Prompt。

---

## 学习路线（建议顺序）

不要一次学30个模式。

按下面顺序掌握：

#### 第一阶段（必须掌握）

1. Role Pattern
2. Task Pattern
3. Constraint Pattern
4. Output Schema Pattern
5. Few-shot Pattern

掌握后已经超过80%的使用者。

---

#### 第二阶段（Prompt Engineer核心）

6. Chain of Thought
7. Task Decomposition
8. Least-to-Most
9. Reflection
10. Critic

掌握后可以设计复杂Prompt。

---

#### 第三阶段（Agent时代）

11. ReAct
12. Planner-Executor
13. Supervisor
14. Multi-Agent
15. Workflow Pattern

掌握后就不再是在写单个Prompt，而是在设计：

```text
Prompt
→ Skill
→ Tool
→ Agent
→ Workflow
→ MCP
```

这也是当前企业级 AI 系统的主流演进方向。
