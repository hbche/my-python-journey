import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

_ = load_dotenv(find_dotenv())

client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

response = client.responses.create(model="qwen3.5-plus", input="你能做些什么？")

# 获取模型回复
print(response.output_text)
