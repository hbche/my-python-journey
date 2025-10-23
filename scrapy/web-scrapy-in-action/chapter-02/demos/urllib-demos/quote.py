from urllib.parse import quote

keyword = '咖啡因'
url = f'https://www.baidu.com/s?wd={keyword}'
# 将 URL中的中文参数转换为URL编码，类似js中的 encodeURIComponent
print(quote(url))       # https%3A//www.baidu.com/s%3Fwd%3D%E5%92%96%E5%95%A1%E5%9B%A0