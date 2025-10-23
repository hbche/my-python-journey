from urllib.request import HTTPPasswordMgrWithDefaultRealm, build_opener, HTTPBasicAuthHandler
from urllib.error import HTTPError

username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

# 首先实例化 HTTPPasswordMgrWithDefaultRealm对象
p = HTTPPasswordMgrWithDefaultRealm()
# 利用 add_password 添加用户名和密码
p.add_password(None, url, username, password)
# 借助 HTTPPasswordMgrWithDefaultRealm 对象实例化 HTTPBasicAuthHandler
auth_handler = HTTPBasicAuthHandler(p)
# 基于 HTTPBasicAuthHandler 构建 opener
opener = build_opener(auth_handler)

try:
    # 基于 opener 对象的 open 方法爬取网页
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except HTTPError as e:
    print(e.reason)