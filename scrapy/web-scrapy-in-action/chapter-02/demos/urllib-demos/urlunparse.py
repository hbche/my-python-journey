from urllib.parse import urlunparse

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
result = urlunparse(data)
print(result)       # https://www.baidu.com/index.html;user?a=6#comment