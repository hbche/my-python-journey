from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:8080',
    'https': 'https://127.0.0.1:8080'
})

opener = build_opener(proxy_handler)
result = opener.open('https://www.baidu.com')
html = result.read().decode('utf-8')
print(html)
