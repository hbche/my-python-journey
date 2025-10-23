from urllib.request import Request
from urllib.request import urlopen
import gzip
from io import BytesIO

url = 'https://www.python.org/'

try:
    request = Request(url)
    # 添加一些基本的请求头，避免被网站拒绝
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
    
    response = urlopen(request)
    
    # 检查响应是否被压缩
    if response.info().get('Content-Encoding') == 'gzip':
        buf = BytesIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        content = f.read().decode('utf-8')
    else:
        content = response.read().decode('utf-8')
    
    print(content)
    
except Exception as e:
    print(f"发生错误: {e}")
