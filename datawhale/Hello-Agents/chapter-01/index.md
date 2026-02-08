# 第一章 初始智能体

## 1.1 什么是智能体？


在人工智能领域，智能体被定义为任何能够通过**传感器（Sensors）**感知其所处**环境（Environment）**，并自主地通过**执行器（Actuators）**采取**行动（Action）**以达成特定目标的实体。

### 1.1.1 传感器视角下的智能体

传统智能体

| 类型                 | 解释说明                                                                                                          | 示例                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 简单反射智能体       | 由工程师明确设计的“条件 - 动作”规则                                                                               | 自动恒温器                 |
| 基于模型的反射智能体 | 在简单反射智能体的基础上增加了内部世界模型，让智能体有了初步“记忆”。 用于追踪和理解环境中无法被直接感知的那部分。 | 自动驾驶                   |
| 基于目标的智能体     | 能主动地、有预见性地选择能够导向某个特定未来状态的行动。                                                          | GPS导航系统                |
| 基于效能的智能体     | 在基于目标的智能体基础上，当出现多个目标时，增加权衡。                                                            | 更省油、时间最短的导航路径 |
| 学习型智能体         | 不依赖预设，通过与环境的交互自主学习。通过强化学习实现                                                            | -                          |

### 1.1.2 大语言模型驱动的新范式

传统智能体的能力基于工程师的显示编程与知识构建，其行为是确定且有边界的；而大语言模型驱动的智能体通过海量数据上的预训练，获得隐式的世界模型和强大的涌现力，使其能够以更灵活、更通用的方式应对复杂任务。

总而言之，我们正从开发专用自动化工具转向构建自主解决问题的系统。核心不再是写代码，而是引导一个通用的“大脑”去规划、行动和学习。

### 1.1.3 智能体的类型

1. 基于内部决策架构的分类
2. 基于时间和反应性的分类
   1. 反应式智能体
   2. 规划式智能体
   3. 混合式智能体
3. 基于知识表示的分类
   1. 符号主义AI：传统人工智能，基于人类语言的逻辑操作，将世界知识整理为规则库和知识图谱。依赖于一个完备的规则体系，任何未知的领域会使其失灵。
   2. 亚符号主义AI：利用大量神经元组成的网络，从海量数据中学习到的统计模式。神经网络和深度学习是其代表。在纯粹的逻辑推理任务上表现不佳，会产生看似合理却事实错误的幻觉。
   3. 神经符号主义AI：融合符号主义和亚符号主义，大语言模型是其代表。


## 1.2 智能体的构成和运行原理

### 1.2.1 任务环境定义

要理解智能体的运作，我们必须先理解它所处的**任务环境**。在人工智能领域，通常使用**PEAS 模型**来精确描述一个任务环境，即分析其**性能度量(Performance)**、**环境(Environment)**、**执行器(Actuators)**和**传感器(Sensors)** 。

### 1.2.2 智能体的运行机制

在定义了智能体所处的任务环境后，我们来探索其核心的运行机制。智能体并非一次性完成任务，而是通过一个持续的循环与环境进行交互，这个核心机制被称为 **智能体循环 (Agent Loop)**。

这个循环主要包含以下几个相互关联的阶段：

1. 感知
2. 思考
   1. 规划
   2. 工具选择
3. 行动

智能体的行动会引起**环境 (Environment) **的**状态变化 (State Change)**，环境随即会产生一个新的**观察 (Observation)** 作为结果反馈。这个新的观察又会在下一轮循环中被智能体的感知系统捕获，形成一个持续的“感知-思考-行动-观察”的闭环。智能体正是通过不断重复这一循环，逐步推进任务，从初始状态向目标状态演进。

### 1.2.3 智能体的感知与行动

在工程实践中，为了让 LLM 能够有效驱动这个循环，我们需要一套明确的**交互协议 (Interaction Protocol)** 来规范其与环境之间的信息交换。

在许多现代智能体框架中，这一协议体现在对智能体每一次输出的结构化定义上。智能体的输出不再是单一的自然语言回复，而是一段遵循特定格式的文本，其中明确地展示了其内部的推理过程与最终决策。

这个结构通常包含两个核心部分：

- Thought（思考）：这是智能体内部决策的“快照”。它以自然语言形式阐述了智能体如何分析当前情境、回顾上一步的观察结果、进行自我反思与问题分解，并最终规划出下一步的具体行动。
- Action（行动）：这是智能体基于思考后，决定对环境施加的具体操作，通常以函数调用的形式表示。

例如，一个正在规划旅行的智能体可能会生成如下格式化的输出：

``` bash
Thought: 用户想知道北京的天气。我需要调用天气查询工具。
Action: get_weather("北京")
```

这里的`Action`字段构成了对外部世界的指令。一个外部的**解析器 (Parser)** 会捕捉到这个指令，并调用相应的`get_weather`函数。

行动执行后，环境会返回一个结果。例如，`get_weather`函数可能返回一个包含详细天气数据的 JSON 对象。然而，原始的机器可读数据（如 JSON）通常包含 LLM 无需关注的冗余信息，且格式不符合其自然语言处理的习惯。

因此，感知系统的一个重要职责就是扮演传感器的角色：将这个原始输出处理并封装成一段简洁、清晰的自然语言文本，即观察。

``` bash
Observation: 北京当前天气为晴，气温25摄氏度，微风。
```

这段`Observation`文本会被反馈给智能体，作为下一轮循环的主要输入信息，供其进行新一轮的`Thought`和`Action`。

综上所述，通过这个由 Thought、Action、Observation 构成的严谨循环，LLM 智能体得以将内部的语言推理能力，与外部环境的真实信息和工具操作能力有效地结合起来。

## 1.3 动手试验：5分钟实现第一个智能体

### 1.3.1 准备工作

编写 python 程序演示智能体工作原理。

步骤：

1. 安装依赖
   
   1. requests: python 网络请求库
   2. tavily-python: 强大的AI搜索 API 客户端，用于获取实时的网络搜索结果
      1. tavily-python需要注册key
   3. openai: OpenAI官方提供的 Python SDK，用于调用GPT等大语言模型服务。
   ```bash
   pip install requests openai tavily-python
   ```
2. 准备指令模板: 驱动真实LLM的关键在于 **提示词工程 (Prompt Engineering)**。我们需要设计一个指令模板，告诉LLM它应该扮演什么角色、拥有哪些工具、以及如何格式化它的思想和行动。这是我们智能体的“说明书”，它将作为 `system_prompt` 传递给LLM。
   ``` bash
    AGENT_SYSTEM_PROMPT = """
    你是一个智能旅行助手。你的任务是分析用户的请求，并使用可用工具一步步地解决问题。

    # 可用工具:
    - `get_weather(city: str)`: 查询指定城市的实时天气。
    - `get_attraction(city: str, weather: str)`: 根据城市和天气搜索推荐的旅游景点。

    # 输出格式要求:
    你的每次回复必须严格遵循以下格式，包含一对Thought和Action：

    Thought: [你的思考过程和下一步计划]
    Action: [你要执行的具体行动]

    Action的格式必须是以下之一：
    1. 调用工具：function_name(arg_name="arg_value")
    2. 结束任务：Finish[最终答案]

    # 重要提示:
    - 每次只输出一对Thought-Action
    - Action必须在同一行，不要换行
    - 当收集到足够信息可以回答用户问题时，必须使用 Action: Finish[最终答案] 格式结束

    请开始吧！
    """
   ```
3. 查询真实天气
   ``` py
   import requests

   def get_weather(city: str) -> str:
       """
       通过调用 wttr.in API 查询真实的天气信息。
       """
       url = f"https://wttr.in/{city}?format=j1"
       # API 端点，我们请求JSON格式的数据
       try:
           # 发起网络请求
           response = requests.get(url)
           # 监查网络请求相应状态码是否为200（成功）
           response.raise_for_status()
           # 解析返回的JSON数据
           data = response.json()

           print(f"当前响应数据：{data}")

           # 获取当天天气情况
           current_condition = data['current_condition'][0]
           weather_desc = current_condition['weatherDesc'][0]['value']
           temp_c = current_condition['temp_C']

           return f"{city}当前的天气：{weather_desc}，气温{temp_c}摄氏度"
       except requests.exceptions.RequestException as e:
           # 处理网络错误
           return f"错误: 查询天气时遇到网络异常 - {e}"
       except (KeyError, IndexError) as e:
           # 处理数据解析错误
           return f"错误: 解析天气数据失败，可能是城市名称无效 - {e}"
   ```
4. 搜索并推荐旅游景点
   ``` py
   import os
   from tavily import TavilyClient
   def get_attraction(city: str, weather: str) -> str:
    """
    get_attraction: 根据城市和天气，使用 Tavily Search API 搜素并返回优化后的景点推荐。
    """

    # 根据Tavily API 初始化其客户端实例
    api_key = os.environ.get('TAVILY_API_KEY' )
    if not api_key:
        print("错误: 未配置TAVILY_API_KEY环境变量。")
    client = TavilyClient(api_key)
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"

    try:
        response = client.search(query=query, search_depth="basic", include_answer=True)

        if response.get('weather'):
            return response['answer']
        
        formatted_results = []
        for result in response.get('weather', []):
            formatted_results.append(f"- {result['title']}: {result['content']}")
        
        if not formatted_results:
            return "抱歉！没有找到相关的旅游景点推荐。"
        
        return f"根据搜索，为您找到以下信息：\n {'\n'.join(formatted_results)}"
    except Exception as e:
        return f'错误: 执行Tavily搜索时出现问题 - {e}'
   ```


### 1.3.2 接入大语言模型

当前，很多OpenAPI都遵循与 OpenAPI相似的接口规范。智能体的自主决策能力来源于 LLM。我们将实现一个通用的客户端 `OpenAICompatibleClient`，它可以连接到任何兼容 OpenAI 接口规范的 LLM 服务。

``` py
from openai import OpenAI

class OpenAICompatibleClient:
    """
    OpenAICompatibleClient: 一个用于调用任何兼容OpenAI接口的LLM服务的客户端。
    """

    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(api_key=api_key, base_url=base_url)

    def generate(self, prompt: str, system_prompt: str) -> str:
        """
        generate: 调用LLM API来生成回应
        """
        print("正在调用大语言模型")
        try:
            messages = [
                {'role': 'system', 'prompt': system_prompt},
                {'role': 'user', 'prompt': prompt}
            ]
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=False
            )
            answer = response.choices[0].message.content
            print("大语言模型响应成功")
            return answer
        except Exception as e:
            print(f"调用LLM API 时发生错误: {e}")
            return "错误: 调用语言模型服务时出错。"
```

### 1.3.3 执行行动循环

``` py

```