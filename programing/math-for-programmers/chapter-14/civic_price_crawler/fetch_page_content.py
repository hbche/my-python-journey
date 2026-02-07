import datetime
import logging
import random
import re
import time

import bs4 as BeautifulSoup
import requests
from config import TARGET_SITES


def fetch_page_content(url, site_name, max_retries=3):
    """
    抓取网页内容，支持重试机制
    """
    headers = TARGET_SITES[site_name]["headers"]

    for attempt in range(max_retries):
        try:
            # 添加随机延迟，避免被反爬
            time.sleep(random.uniform(1, 3))

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # 检查编码
            if response.encoding == "ISO-8859-1":
                response.encoding = "utf-8"

            logging.info(f"成功抓取 {site_name} 页面: {url}")
            return response.text

        except requests.exceptions.RequestException as e:
            logging.warning(f"第{attempt + 1}次尝试失败: {e}")
            if attempt < max_retries - 1:
                time.sleep(random.uniform(2, 5))
            else:
                logging.error(f"抓取失败: {url}")
                return None

    return None


def parse_price_from_text(text):
    """
    从文本中提取价格信息
    支持多种价格格式：￥13.6万、13.6万元、136000元等
    """
    price_patterns = [
        r"￥\s*([\d\.]+)\s*万",  # ￥13.6万
        r"([\d\.]+)\s*万元",  # 13.6万元
        r"([\d\.]+)\s*万",  # 13.6万
        r"([\d,]+)\s*元",  # 136,000元
    ]

    for pattern in price_patterns:
        matches = re.findall(pattern, text)
        if matches:
            # 转换价格为浮点数（单位：万元）
            prices = []
            for match in matches:
                # 处理逗号分隔
                match = match.replace(",", "")
                try:
                    price = float(match)
                    # 如果匹配的是"万"格式但价格小于100，可能是万元单位
                    if "万" in pattern and price < 100:
                        prices.append(price)
                    elif "元" in pattern:
                        prices.append(price / 10000)
                except ValueError:
                    continue
            if prices:
                return sum(prices) / len(prices)  # 返回平均价格

    return None


def extract_car_info_from_html(html_content, site_name):
    """
    从HTML中提取车辆信息
    """
    soup = BeautifulSoup(html_content, "html.parser")
    car_data = []

    # 根据网站结构提取信息
    if site_name == "太平洋汽车":
        # 太平洋汽车的文章结构
        articles = soup.find_all("div", class_=re.compile(r"article|item"))
        for article in articles[:20]:  # 限制数量
            title_elem = article.find("h3") or article.find("a")
            content_elem = article.find("p") or article

            if title_elem and content_elem:
                title = title_elem.get_text(strip=True)
                content = content_elem.get_text(strip=True)

                # 检查是否包含思域和年份信息
                if any(
                    keyword in title.lower() or keyword in content.lower()
                    for keyword in ["思域", "civic"]
                ):
                    # 提取年份
                    year_match = re.search(r"(20\d{2})", title + content)
                    year = int(year_match.group(1)) if year_match else None

                    # 提取价格
                    price = parse_price_from_text(content)

                    if year and price and 2021 <= year <= 2025:
                        car_data.append(
                            {
                                "year": year,
                                "price": price,
                                "source": site_name,
                                "title": title[:100],  # 限制标题长度
                                "timestamp": datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                ),
                            }
                        )

    elif site_name == "汽车之家":
        # 汽车之家的问答结构
        qa_items = soup.find_all("div", class_=re.compile(r"question|answer"))
        for item in qa_items[:15]:
            text = item.get_text(strip=True)

            # 检查是否包含价格信息
            if "价格" in text and ("思域" in text or "civic" in text):
                # 提取年份
                year_match = re.search(r"(20\d{2})", text)
                year = int(year_match.group(1)) if year_match else None

                # 提取价格
                price = parse_price_from_text(text)

                if year and price and 2021 <= year <= 2025:
                    car_data.append(
                        {
                            "year": year,
                            "price": price,
                            "source": site_name,
                            "content": text[:200],  # 截取部分内容
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    )

    elif site_name == "第一车网":
        # 第一车网的列表结构
        car_items = soup.find_all("div", class_=re.compile(r"car-item|list-item"))
        for item in car_items[:10]:
            text = item.get_text(strip=True)

            # 检查是否包含思域信息
            if "思域" in text:
                # 提取年份和里程
                year_match = re.search(r"(\d{4})年", text)
                mileage_match = re.search(r"(\d+\.?\d*)\s*万公里", text)

                year = int(year_match.group(1)) if year_match else None
                mileage = float(mileage_match.group(1)) if mileage_match else None

                # 提取价格
                price = parse_price_from_text(text)

                if year and price and 2021 <= year <= 2025:
                    car_data.append(
                        {
                            "year": year,
                            "price": price,
                            "mileage": mileage,
                            "source": site_name,
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
                    )

    return car_data
