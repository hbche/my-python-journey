import os

import httpx
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

# find_dotenv() 寻找并定位 .env 文件的路径
# load_dotenv() 读取 .env 文件，并将其中的环境变量加载到当前的运行环境中
_ = load_dotenv(find_dotenv())

# 如果我们需要通过代理端口访问，我们需要如下配置
os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

# # 获取环境变量 OPENAI_API_KEY
# openai.api_key = os.environ["OPENAI_API_KEY"]

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    http_client=httpx.Client(proxy=os.getenv("HTTP_PROXY")),
)

# try:
# 与 OpenAI 交互的主要API
response = client.responses.create(
    # 指定模型
    model="GPT-3.5 Turbo",
    # 指定推理程度，effort-努力
    reasoning={"effort": "low"},
    # 指定指令：
    instructions="我应该搜索什么才能找到AI领域的最新进展？",
    # 输入
    input="Hello",
)

print(response.output_text)
# except Exception as e:
#     print(f"发生错误${e}")

# # 等效于
# response = client.responses.create(
#     model="GPT-3.5 Turbo",
#     reasoning={"effort": "low"},
#     input=[
#         {"role": "developer", "content": "You are a helpful assistant."},
#         {"role": "user", "content": "Hello"},
#     ],
# )
