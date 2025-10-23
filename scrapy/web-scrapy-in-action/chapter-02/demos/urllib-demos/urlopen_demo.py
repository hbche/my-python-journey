from urllib.request import urlopen

# 使用urlopen方法对网站进行爬取
response = urlopen('https://www.python.org')
# 打印响应对象类型
print(type(response))       # <class 'http.client.HTTPResponse'>
# # 对响应信息进行处理
# print(response.read().decode('utf-8'))
# 获取响应状态
print(response.status)      # 200
# 获取所有头部信息
print(response.getheaders())
# 获取指定头部信息
print(response.getheader('Content-Type'))   # text/html; charset=utf-8