from urllib.request import HTTPCookieProcessor, build_opener
import http.cookiejar

# 声明 CookieJar对象
cookie = http.cookiejar.CookieJar()
# 基于CookieJar实例初始化 HTTPCookieProcessor
handler = HTTPCookieProcessor(cookie)
# 基于 HTTPCookieProcessor 生成 opener
opener = build_opener(handler)
# 爬取指定网页
response = opener.open('https://www.baidu.com')

# 遍历 cookie 
for item in cookie:
    print(f"{item.name}={item.value}")