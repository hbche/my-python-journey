from urllib.parse import urlunsplit

data = ['https', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
result = urlunsplit(data)
print(result)       # https://www.baidu.com/index.html;user?a=6#comment