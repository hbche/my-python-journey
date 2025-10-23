from urllib.parse import quote, unquote

keyword = '壁纸'
url = f"https://www.baidu.com/s?wd={keyword}"
quote_url = quote(url)          # https%3A//www.baidu.com/s%3Fwd%3D%E5%A3%81%E7%BA%B8
print(quote_url)
print(unquote(quote_url))       # https://www.baidu.com/s?wd=壁纸