import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('civic_price_crawler.log'),
        logging.StreamHandler()
    ]
)

# 目标网站配置（基于搜索结果中的主要平台）
TARGET_SITES = {
    '太平洋汽车': {
        'base_url': 'https://www.pcauto.com.cn/',
        'search_path': '/x/search',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
        }
    },
    '汽车之家': {
        'base_url': 'https://www.autohome.com.cn',
        'search_path': '/ask/search',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Referer': 'https://www.autohome.com.cn/'
        }
    },
    '第一车网': {
        'base_url': 'https://so.iautos.cn',
        'search_path': '/search',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    }
}

# 搜索关键词配置
SEARCH_KEYWORDS = [
    "十一代思域 二手",
    "本田思域 2021 二手",
    "思域 2022 二手价格",
    "思域 2023 二手车",
    "思域 2024 二手市场",
    "思域 2025 回收价",
    "Civic 11代 二手"
]

# 车型年份范围
TARGET_YEARS = list(range(2021, 2026))  # 2021-2025年