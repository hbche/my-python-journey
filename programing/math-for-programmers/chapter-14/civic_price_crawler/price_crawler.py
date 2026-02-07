import logging
import random
import time
from config import TARGET_SITES, SEARCH_KEYWORDS
from fetch_page_content import fetch_page_content, extract_car_info_from_html

def crawl_civic_prices():
    """
    主抓取函数，整合多个数据源
    """
    all_car_data = []
    
    logging.info("开始抓取本田思域二手车价格数据...")
    
    for site_name, site_config in TARGET_SITES.items():
        logging.info(f"正在处理 {site_name}...")
        
        try:
            # 构建搜索URL
            base_url = site_config['base_url']
            
            # 对于每个搜索关键词
            for keyword in SEARCH_KEYWORDS:
                # 构建搜索URL（简化版，实际需要根据网站API调整）
                if site_name == '太平洋汽车':
                    search_url = f"{base_url}/x/4662/46628464.html"  # 使用搜索结果中的具体页面[2](@ref)
                elif site_name == '汽车之家':
                    search_url = f"{base_url}/ask/13917197.html"  # 使用搜索结果中的具体页面[4](@ref)
                elif site_name == '第一车网':
                    search_url = f"{base_url}/dali/bentian-pasds9v1epcatcpbnscac2/"  # 使用搜索结果中的具体页面[3](@ref)
                
                # 抓取页面内容
                html_content = fetch_page_content(search_url, site_name)
                
                if html_content:
                    # 提取车辆信息
                    car_data = extract_car_info_from_html(html_content, site_name)
                    all_car_data.extend(car_data)
                    
                    logging.info(f"从 {site_name} 提取到 {len(car_data)} 条数据")
                
                # 避免请求过快
                time.sleep(random.uniform(2, 4))
        
        except Exception as e:
            logging.error(f"处理 {site_name} 时出错: {e}")
            continue
    
    return all_car_data