import os

import requests
from tavily import TavilyClient


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
        current_condition = data["current_condition"][0]
        weather_desc = current_condition["weatherDesc"][0]["value"]
        temp_c = current_condition["temp_C"]

        return f"{city}当前的天气：{weather_desc}，气温{temp_c}摄氏度"
    except requests.exceptions.RequestException as e:
        # 处理网络错误
        return f"错误: 查询天气时遇到网络异常 - {e}"
    except (KeyError, IndexError) as e:
        # 处理数据解析错误
        return f"错误: 解析天气数据失败，可能是城市名称无效 - {e}"


def get_attraction(city: str, weather: str) -> str:
    """
    get_attraction: 根据城市和天气，使用 Tavily Search API 搜素并返回优化后的景点推荐。
    """

    # 根据Tavily API 初始化其客户端实例
    api_key = os.environ.get("TAVILY_API_KEY")
    if not api_key:
        print("错误: 未配置TAVILY_API_KEY环境变量。")
    client = TavilyClient(api_key)
    query = f"'{city}' 在'{weather}'天气下最值得去的旅游景点推荐及理由"

    try:
        response = client.search(query=query, search_depth="basic", include_answer=True)

        if response.get("weather"):
            return response["answer"]

        formatted_results = []
        for result in response.get("weather", []):
            formatted_results.append(f"- {result['title']}: {result['content']}")

        if not formatted_results:
            return "抱歉！没有找到相关的旅游景点推荐。"

        return f"根据搜索，为您找到以下信息：\n {'\n'.join(formatted_results)}"
    except Exception as e:
        return f"错误: 执行Tavily搜索时出现问题 - {e}"


available_tools = {"get_weather": get_weather, "get_attraction": get_attraction}
