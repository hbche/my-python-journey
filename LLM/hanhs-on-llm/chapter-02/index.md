# 调用 LLM 的 API

## 基本概念

### Prompt

Prompt 最初是 NLP（自然语言处理）研究者为下游任务设计出来的一种任务专属的输入模板，类似于一种任务（例如：分类，聚类等）会对应一种 Prompt。在 ChatGPT 推出并获得大量应用之后，Prompt 开始被推广为给大模型的所有输入。即，我们每一次访问大模型的输入为一个 Prompt，而大模型给我们的返回结果则被称为 Completion。

### Temperature

LLM 生成是具有随机性的，在模型的顶层通过选取不同预测概率的预测结果来生成最后的结果。我们一般可以通过控制 Temperature 参数来控制 LLM 生成结果的随机性与创造性。

Temperature 一般取值在 0~1 之间，当取值较低接近0时，预测的随机性会较低，产生更保守、可预测的文本，不太可能生成意想不到或不寻常的词。当取值较高接近1时，预测的随机性会较高，所有词被选择的可能性更大，会产生更有创意、多样化的文本，更有可能生成不寻常或意想不到的词。

对于不同的问题与应用场景，我们可能需要设置不同的 Temperature。例如，在本教程搭建的个人知识库助手项目中，我们一般将 Temperature 设置为0，从而保证助手对知识库内容的稳定使用，规避错误内容、模型幻觉；在产品智能客服、科研论文写作等场景中，我们同样更需要稳定性而不是创造性；但在个性化 AI、创意营销文案生成等场景中，我们就更需要创意性，从而更倾向于将 Temperature 设置为较高的值。

### System Prompt

System Prompt 是随着 ChatGPT API 开放并逐步得到大量使用的一个新兴概念，事实上，它并不在大模型本身训练中得到体现，而是大模型服务方为提升用户体验所设置的一种策略。

具体来说，在使用 ChatGPT API 时，你可以设置两种 Prompt：一种是 System Prompt，该种 Prompt 内容会在整个会话过程中持久地影响模型的回复，且相比于普通 Prompt 具有更高的重要性；另一种是 User Prompt，这更偏向于咱们平时的 Prompt，即需要模型做出回复的输入。

## 调用 ChatGPT

[OpenAI python版本](https://github.com/openai/openai-python)

### ChatGPT

### 获取并配置 OpenAI API key

访问 [ChatGPT 官网](https://platform.openai.com/home)，创建 API_KEY

```py
import os
import openai
from dotenv import find_dotenv, load_dotenv

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取 .env 文件，并将其中的环境变量加载到当前的运行环境中
_ = load_dotenv(find_dotenv())

# 如果我们需要通过代理端口访问，我们需要如下配置
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "https://127.0.0.1:7890"

# 获取环境变量 OPENAI_API_KEY
openai.api_key = os.environ["OPENAI_API_KEY"]
```

### 调用 OpenAI 原生接口

我们可以通过阅读[官方文档](https://developers.openai.com/api/docs/guides/text)，通过与OpenAI的模型进行交互来完成文本生成。

```py
# 与 OpenAI 交互的主要API
response = client.responses.create(
    # 指定模型
    model="gpt-5.4",
    # 指定推理程度，effort-努力
    reasoning={"effort": "low"},
    # 指定指令：
    instructions="You are a helpful assistant.",
    # 输入
    input="Hello",
)

# # 等效于
# response = client.responses.create(
#     model="gpt-5.4",
#     reasoning={"effort": "low"},
#     input=[
#         {"role": "developer", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello"},
#     ],
# )
```

## 调用千问

### 获取并配置 API Key

### 调用 OpenAI 原生接口

```py
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
)

response = client.responses.create(model="qwen3.5-plus", input="你能做些什么？")

# 获取模型回复
print(response.output_text)
```

接下来，我们来封装一个函数，参数为 Prompt，返回对应的结果

```py
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())


def generage_qwen_client():
    """
    生成千问客户端
    """
    client = OpenAI(
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url="https://dashscope.aliyuncs.com/api/v2/apps/protocols/compatible-mode/v1",
    )

    return client


def get_response(prompt, model="qwen3.5-plus"):
    """
    根据Prompt生成文本
    """
    client = generage_qwen_client()
    response = client.responses.create(
        model=model,
        reasoning={"effort": "low"},
        instructions="你是一名贴心的个人助手",
        input=prompt,
    )

    return response.output_text
```

## LangChain 组件详解

[LangChain](https://github.com/langchain-ai/langchain) 是一个用于构建智能代理和基于大型语言模型（LLM）的应用程序框架。它能帮助我们轻松串联可互操作的组件和第三方集成，以简化 AI 应用的开发流程，同时随着底层技术的演进确保未来兼容性。

### 模型输入/输出

LangChain 中模型输入/输出模块是与各种大语言模型进行交互的基本组件，是大语言模型应用的核心元素。模型 I/O 允许您管理 prompt（提示），通过通用接口调用语言模型以及从模型输出中提取信息。

主要包含以下部分：Prompts、Language Models以及 Output Parsers。用户原始输入与模型和示例进行组合，然后输入给大语言模型，再根据大语言模型的返回结果进行输出或者结构化处理。

参照 [LangChain的ChatQwen 集成](https://docs.langchain.com/oss/python/integrations/chat/qwen)，编写基础案例：

```py
import os

from dotenv import find_dotenv, load_dotenv
from langchain_qwq import ChatQwen

_ = load_dotenv(find_dotenv())

# 实例化
llm = ChatQwen(
    model="qwen3.5-plus",
    max_tokens=3_000,
    timeout=None,
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    api_base="https://dashscope.aliyuncs.com/compatible-mode/v1",
    max_retries=2,
)

# 执行
messages = [
    (
        "system",
        "你是AI知识专家，负责讲解AI知识",
    ),
    ("human", "什么是神经网络"),
]

ai_msg = llm.invoke(messages)
print(ai_msg.content)
```

### 数据连接

如果能够让大模型在训练数据集的基础上，利用我们自有数据中的信息来回答我们的问题，那便能够得到更有用的答案。

LangChain 数据连接（Data connection）模块通过以下方式提供组件来加载、转换、存储和查询数据：Document loaders、Document transformers、Text embedding models、Vector stores 以及 Retrievers。

### 链(Chain)

虽然独立使用大型语言模型能够应对一些简单任务，但对于更加复杂的需求，可能需要将多个大型语言模型进行链式组合，或与其他组件进行链式调用。链允许将多个组件组合在一起，创建一个单一的、连贯的应用程序。

### 记忆(Memory)

### 代理(Agent)

### 回调(Callback)
