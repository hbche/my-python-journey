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
