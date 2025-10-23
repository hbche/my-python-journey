from urllib.request import urlopen
from urllib import parse

url = 'https://www.httpbin.org/post'
data = bytes(parse.urlencode({'name': 'hanbin'}), encoding='utf-8')
response = urlopen(url, data=data)
print(response.getheader('Content-Type'))
print(response.read().decode('utf-8'))