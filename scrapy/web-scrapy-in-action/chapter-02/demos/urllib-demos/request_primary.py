from urllib.request import urlopen, Request
from urllib import parse

# 请求路径
url = 'https://www.httpbin.org/post'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    'Host': 'www.httpbin.org'
}
# 请求参数
dict = {'name': 'hanin'}
# 将请求参数转换为 bytes 格式的二进制流
data = bytes(parse.urlencode(dict), encoding='utf-8')
# 创建请求实例
request = Request(url, data=data, headers=headers, method='POST')
# 发送请求
response = urlopen(request)
# 解析响应
print(response.read().decode('utf-8'))