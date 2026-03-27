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
