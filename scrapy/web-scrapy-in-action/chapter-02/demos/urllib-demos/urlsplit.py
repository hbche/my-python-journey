from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?a=6#comment')
print(result)       # SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment')