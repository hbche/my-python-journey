# 第 2 章 基本库的使用

## 2.1 urllib 的使用

urllib 可以实现 HTTP 请求的发送，可以指定请求的 URL、请求头、请求体等信息。

urllib 库包含以下 4 个模块。

- request: 基本的 HTTP 请求模块，可以模拟请求的发送。
- error: 异常处理模块。
- parse: 工具模块。提供许多 URL 的处理方法
- robotparser: 主要用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，用得
  比较少。

### 2.1.1 发送请求

#### urlopen

urllib.request 模块提供了最基本的构造 HTTP 请求的方法，利用这个模块可以模拟浏览
器的请求发起过程，同时它还具有处理授权验证、重定向、浏览器 cookie 以及其他一些功
能。

以下写一个简单的爬虫程序，对 Python 官网进行爬取：

```python
from urllib.request import urlopen

# 使用urlopen方法对网站进行爬取
response = urlopen('https://www.python.org')
# 打印响应对象类型
print(type(response))       # <class 'http.client.HTTPResponse'>
# # 对响应信息进行处理
# print(response.read().decode('utf-8'))
```

response 是一个 HTTPResponse 类型的对象，主要包含
read、readinto、getheader、getheaders、fileno 等方法，以及
msg、versions、status、reason、debuglevel、closed 等属性。

调用 read() 方法可以得到响应的网页内容、调用 status 属性可以得到响应结果的状态码
。

```python
# 获取响应状态
print(response.status)      # 200
# 获取所有头部信息
print(response.getheaders())
# 获取指定头部信息
print(response.getheader('Content-Type'))   # text/html; charset=utf-8
```

利用 urlopen 方法，已经可以完成对简单网页的 GET 请求抓取。

以下是完整的 urlopen 方法的 API:

```python
urlopen(url, data=None, [timeout,]*, cafile=None, capath=None, cadefault=False, context=None)
```

1. data 参数

   data 参数是可选的。在添加该参数时，需要使用 bytes() 方法将参数转换为字节流编
   码格式的内容，即 bytes 类型。另外，如果传递了这个参数，那么它的请求方式不再是
   GET，而是 POST 了。

   ```python
   from urllib.request import urlopen
   from urllib import parse
   url = 'https://www.httpbin.org/post'
   data = bytes(parse.urlencode({'name': 'hanbin'}), encoding='utf-8')
   response = urlopen(url, data=data)
   print(response.read().decode('utf-8'))
   ```

   我们使用 urllib.parse 模块中的 urlencode 方法将字典参数转换为字符串，在通过
   bytes 方法将字符串转换成指定编码格式的二进制流，最后将该二进制流作为 urlopen
   方法的 data 参数进行传递。

2. timeout 参数

   time 参数是可选的。用于设置超时时间，单位为妙，意思是如果请求超出了设置的这个
   时间，还没有得到响应，就会抛出异常。如果不指定该参数，则会使用全局默认时间。
   这个参数支持 HTTP、HTTPS、FTP 请求。

   ```python
   from urllib.request import urlopen

   response = urlopen('https://www.httpbin.org/get', timeout=0.1)
   print(response.read())      # urllib.error.URLError: <urlopen error timed out>
   ```

   这里我们设置了请求超时时间为 0.1 妙。程序运行了 0.1 秒之后，服务器依然没有响
   应，于是抛出了 URLError 异常。该异常属于 urllib.error 模块，错误原因是超时。

   因此我们可以利用该异常跳过长时间未响应的网页抓取。

   ```python
   from urllib.request import urlopen
   from urllib.error import URLError
   import socket

   try:
       response = urlopen('https://www.httpbin.org/get', timeout=0.1)
   except URLError as e:
       if isinstance(e.reason, socket.timeout):
           print("TIME OUT")       # TIME OUT
   ```

3. 其他参数

   除了 data 参数和 timeout 参数，urlopen 方法还有 context 参数，该参数必须是
   ssl.SSLContext 类型，用来指定 SSL 的设置。

   此外，cafile 和 capath 这两个参数分别用来指定 CA 整数和其路径，这两个在请求
   HTTPS 链接时会有用。

   cadefault 参数现已弃用，默认值为 False。

#### request

如果需要在请求中加入 Headers 等信息，就得利用更强大的 Request 类来构建请求了。

```python
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
```

下面我们可以看一下 Request 类的构造函数：

```python
class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
```

第一个参数 url 用于请求 URL，这是必传参数，其他都是可选参数。

第二个参数 data 如果要传数据，必须传 bytes 类型的。如果是数据字典，需要先用
urllib.parse 模块里面的 urlencode 方法进行编码。

第三个参数 headers 是一个字典，这就是请求头，在构造请求时，我们既可以通过
headers 参数直接构造此项，也可以通过请求实例的 add_header 方法添加。

添加请求头常见的方式就是通过修改 User-Agent 来伪装浏览器。默认的 User-Agent 是
Python-urllib，我们可以通过修改这个值来伪装浏览器。例如 Chrome 就是：

```python
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36
```

第四个参数 origin_req_host 指的是请求方的 host 名称或者 IP 地址。

第五个参数 unverifiable 表示请求是否是无法验证的，默认取值是 False，意思是用户没
有足够的权限来接收这个请求的结果。例如，请求一个 HTML 文档中的图片，但是没有自动
抓取图像的权限，这是 unverifiable 的值就是 True。

第六个参数 method 是一个字符串，用来指示请求使用的方法。例如 GET、POST 或 PUT 等
。

```python
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
```

#### 高级用法

对于一些高级设置，例如设置 Cookie、代理等，需要借助 Handler 处理。所有 Handler
都是基于 urllib.request 模块中的 BaseHandler 类扩展的。

以下是各种继承自 BaseHandler 的子类。

- HTTPDefaultErrorHandler 用于处理 HTTP 响应错误，所有错误都会抛出 HTTPError 类
  型的异常。
- HTTPRedirectHandler 用于处理重定向。
- HTTPCookieProcessor 用于处理 Cookie。
- ProxyHandler 用于设置代理，代理默认为空。
- HTTPPasswordMgr 用于管理密码，他维护着用户名密码的对照表。
- HTTPBasicAuthHandler 用于管理认证，如果一个链接在打开时需要认证，那么可以用这
  个类来解决认证问题。

如果我们需要使用一些高级的功能，就需要使用 Opener 类，urlopen 类封装了 Opener 的
细节。我们需要借助 Handler 类构建 Opener 类。

- 验证

  在访问某些网站的时候，例如 [ssr3.scrape.center](https://ssr3.scrape.center/)，
  可能弹出需要认证的窗口，遇到这种情况，就表示这个网站启用了基本身份认证，HTTP
  Basic Access Authentication，这是以中国登录验证方式，允许网页浏览器或其他客户
  端程序在请求网站时提供用户名和口令形式的身份认证。

  爬虫可以借助 HTTPBasicAuthHandler 模块完成，代码如下：

  ```python
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
  ```

- 代理

  添加代理：

  ```python
  from urllib.request import ProxyHandler, build_opener

  proxy_handler = ProxyHandler({
      'http': 'http://127.0.0.1:8080',
      'https': 'https://127.0.0.1:8080'
  })

  opener = build_opener(proxy_handler)
  result = opener.open('https://www.baidu.com')
  html = result.read().decode('utf-8')
  print(html)
  ```

- Cookie

  ```python
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
  ```

### 2.1.2 处理异常

urllib 库中的 error 模块定义了由 request 模块产生的异常。当出现问题时，request
模块便会抛出 error 模块中定义的异常。

#### URLError

URLError 类来自 urllib 库的 error 模块，继承自 OSError 类，是 error 异常模块的基
类，由 request 模块产生的异常都可以通过捕获这个类来处理。

它具有一个 reason，即返回错误的原因。

访问一个不存在的页面会报 URLError 错误：

```python
from urllib.request import urlopen
from urllib.error import URLError

try:
    response = urlopen('https://cuiqingcai.com/404')
except URLError as e:
    print(e.reason)
```

#### HTTPError

HTTPError 是 URLError 的子类，专门用来处理 HTTP 请求报错，例如认证请求失败等。它
有如下三个属性：

- code: 返回 HTTP 状态码
- reason
- headers: 返回请求头

```python
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

try:
    response = urlopen('https://cuiqingcai.com/404')
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(e.reason)
```

> 注意，由于 HTTPError 继承自 URLError，所以对于 URLError 的异常捕获需要放到
> HTTPError 的后面，否则 HTTPError 异常将无法被捕获

有时候，reason 返回的不一定是一个字符串，也可能是一个对象：

```python
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import socket

try:
    response = urlopen('https://cuiqingcai.com/404', timeout=0.01)
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except URLError as e:
    print(type(e.reason))       # <class 'TimeoutError'>
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')       # TIME OUT
```

#### 解析链接

urllib 库中提供了 parse 模块，这个模块定义了处理 URL 的标准接口，例如实现 URL 各
部分的抽取、合并以及链接转换。

- urlparse

  该方法可以实现 URL 的识别和分段：

  ```python
  from urllib.parse import urlparse
  result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
  print(type(result))     # <class 'urllib.parse.ParseResult'>
  print(result)           # ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
  ```

  urlparse 的 API 用法如下：

  ```python
  urlparse(urlstring, schema='', allow_fragments=True)
  ```

  urlparse 方法有 3 个参数：

  - urlstring: 这是必填项，即待解析的 URL。
  - schema: 这是默认的协议。如果待解析的 URL 没有带协议信息，就会将这个作为默认
    协议。
  - allowed_fragments: 是否忽略 fragment。如果此项被设置为 False，那么 fragment
    部分就会被忽略。

    如果忽略了 fragment，那么 fragment 将作为 path 的一部分存在

- urlunparse

  有了 urlprase 方法，响应就会有它的队里方法 urlunparse 方法，用于构造 URL。这个
  方法接受的参数是一个可迭代对象，其长度必须是 6。否则会抛出参数数量不足或者过多
  的问题。

  ```python
  from urllib.parse import urlunparse

  data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
  result = urlunparse(data)
  print(result)       # https://www.baidu.com/index.html;user?a=6#comment
  ```

- urlsplit

  这个方法与 urlparse 方法非常类似，只不过它不再单独解析 params 这一部分，params
  会被合并到 path 中。

  ```python
  from urllib.parse import urlsplit

  result = urlsplit('https://www.baidu.com/index.html;user?a=6#comment')
  print(result)       # SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment')
  ```

- urlunsplit

  与 urlunparse 非常相似，这也是将链接的各个部分组合成完整链接的方法，传入的参数
  也是一个可迭代对象，例如列表、元组等，唯一区别是这里参数的长度必须为 5.

  ```python
  from urllib.parse import urlunsplit

  data = ['https', 'www.baidu.com', 'index.html;user', 'a=6', 'comment']
  result = urlunsplit(data)
  print(result)       # https://www.baidu.com/index.html;user?a=6#comment
  ```

- urljoin

  urlunparse 和 urlunsplit 都可以完成链接的合并，但是前提是必须有特定长度的对象
  ，链接的每一部分都要清晰分开。我们还可以使用 urljoin 方法完成链接拼接。该方法
  接收一个字符串作为 base_url，将新的链接作为第二个参数。urljoin 方法会分析
  base_url 的 schema、netloc 和 path 这 3 个内容，并对新链接缺失的部分进行补充，
  最后返回结果。

  ```python
  from urllib.parse import urljoin

  print(urljoin('https://www.baidu.com', 'FAQ.html'))     # https://www.baidu.com/FAQ.html
  print(urljoin('https://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))      # https://www.baidu.com/FAQ.html
  print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.  html'))     # https://www.baidu.com/FAQ.html
  print(urljoin('https://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.  html?question=2'))      # https://cuiqingcai.com/FAQ.html?question=2
  print(urljoin('https://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.    php'))      # https://cuiqingcai.com/index.php
  print(urljoin('https://www.baidu.com', '?category=2#comment'))      # https://www.baidu.com?category=2#comment
  ```

  可以发现，base_url 提供了三项内容：schema、netloc 和 path。如果新的链接里不存
  在这三项，就予以补充；如果存在，就使用新的链接里面的对应部分覆盖 base_url 里对
  应的部分。

- urlencode

  urlencode 在构建 GET 请求参数的时候特别有用。

  ```python
  from urllib.parse import urlencode

  params = {
      'name': 'hanbin',
      'age': 25
  }
  base_url = 'https://www.baidu.com?'
  url = base_url + urlencode(params)
  print(url)      # https://www.baidu.com?name=hanbin&age=25
  ```

  urlencode 方法经常用于将字典结构的请求参数转换成 URL 的参数。

- parse_qs

  利用 parse_qs 方法，可以将一串 GET 请求参数转回字典：

  ```python
  from urllib.parse import parse_qs

  query = 'name=hanbin&age=25'
  url = 'https://www.baidu.com/index.html;user?name=hanbin'
  # 解析查询字符串 query
  print(parse_qs(query))      # {'name': ['hanbin'], 'age': ['25']}
  print(parse_qs(url))        # {'https://www.baidu.com/index.html;user?name': ['hanbin']}
  ```

- parse_qsl

  parse_sql 方法用于将参数转化为由元组组成的列表：

  ```python
  from urllib.parse import parse_qsl

  query = 'name=hanbin&age=25'
  # 以列表形式返回查询字符串的解析结果
  print(parse_qsl(query))     # [('name', 'hanbin'), ('age', '25')]
  ```

  parse_qsl 的运行结果是一个列表，列表的每一项都是一个元组，元组的第一个内容是参
  数名，第二个内容是参数值。

- quote

  该方法可以将内容转化为 URL 编码的格式。当 URL 中带有中文参数时，有可能导致乱码
  问题，此时 quote 方法可以将中文转换为 URL 编码。

  ```python
  from urllib.parse import quote

  keyword = '咖啡因'
  url = f'https://www.baidu.com/s?wd={keyword}'
  # 将 URL中的中文参数转换为URL编码，类似js中的 encodeURIComponent
  print(quote(url))       # https%3A//www.baidu.com/s%3Fwd%3D%E5%92%96%E5%95%A1%E5%9B%A0
  ```

- unquote

  unquote 的作用与 quote 相反，对经过 quote 编码的 URL 参数进行还原。

  ```python
  from urllib.parse import quote, unquote

  keyword = '壁纸'
  url = f"https://www.baidu.com/s?wd={keyword}"
  quote_url = quote(url)          # https%3A//www.baidu.com/s%3Fwd%3D%E5%A3%81%E7%BA%B8
  print(quote_url)
  print(unquote(quote_url))       # https://www.baidu.com/s?wd=壁纸
  ```

  上述是 urllib 库的 parse 模块中常用的解析方法。建议熟练掌握。

#### 分析 Robots 协议

利用 urllib 库的 robotparse 模块，可以分析网站的 Robots 协议。

- Robots 协议

  Robots 协议也称作爬虫协议、机器人协议，全名为网络爬虫排除标准，用来告诉爬虫和
  搜索引擎哪些页面可以抓取、哪些不可以。它通常是一个 robots.txt 文件，一般放在网
  站的根目录下。

  下面是一个 robots.txt 示例：

  ```txt
  User-agent: *
  Disabled: /
  Allow: /public/
  ```

  该爬虫文件限制了所有搜索爬虫只能爬取 public 目录。

  上述样例中的 User-agent 描述了爬虫的名称，这里将其设置为 \* ，代表 Robots 协议
  对所有爬取爬虫都有效，不做限制。我们也可以做如下限制：

  ```txt
  User-agent: Baiduspider
  ```

  这代表设置的规则对百度爬虫有效。如果有多条 User-agent 记录，则意味着有多个爬虫
  会收到爬取限制，但至少需要指定一条。

  Disallow 指定了不允许爬虫爬取的目录，上述案例设置为 /，代表不允许爬取所有页面
  。

  Allow 一般不会单独使用，会和 Disallow 一起用，用来排除某些限制。上例中我们设置
  为 /public/，结合 Disallow 的设置，表示所有页面都不允许爬取，但可以爬取 public
  目录。

  禁止所有爬虫访问所有目录的 robots.txt:

  ```txt
  User-agent: *
  Disallow: /
  ```

  允许所有爬虫爬取：

  ```txt
  User-agent: *
  Disallow:
  ```

- robotparser

  了解了 Robots 协议之后，就可以使用 robotparser 模块来解析 robots.txt 文件了。
  该模块提供了一个类 RobotFileParser，它可以根据某网站的 robots.txt 文件判断一个
  爬取爬虫是否有权爬取这个网站。

  声明如下：

  ```python
  urllib.robotparser.RobotFileParser
  ```

  下面是 RobotFileParser 类的常用方法：

  - set_url: 用来设置 robots.txt 文件的链接。如果在创建 RobotFileParser 对象时传
    入了链接，就不需要使用这个方法设置了。
  - read: 读取 robots.txt 文件并进行分析。注意，这个方法执行读取和分析操作，如果
    不调用这个方法，接下来的判断都会为 False，所以一定记得调用这个方法。
  - parse: 用来解析 robots.txt 文件，传入其中的参数是 robots.txt 文件中某些行的
    内容，它会按照 robots.txt 的语法规则来分析这些内容。
  - can_fetch: 该方法有两个参数，第一个是 User-Agent，第二个是要抓取的 URL。返回
    结果是 True 或 False，表示 User-Agent 只是的搜索引擎是否可以抓取这个 URL。
  - mtime: 返回上次抓取和分析 robots.txt 文件的时间，这对于长时间分析和抓取
    robots.txt 文件的搜索爬虫很有必要，可能需要定期检查以抓取最新的 robots.txt
    文件。
  - modified: 同样对长时间分析和抓取的搜索爬虫很有帮助，可以将当前时间设置为上次
    抓取和分析 robots.txt 文件的时间。

  ```python
  from urllib.robotparser import RobotFileParser
  robot_file_url = 'https://www.baidu.com/robots.txt'
  robot_parser = RobotFileParser(robot_file_url)
  robot_parser.read()
  print(robot_parser.can_fetch('Baiduspider', 'https://www.baidu.com'))       # True
  print(robot_parser.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))     # True
  print(robot_parser.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))       # False
  ```

## 2.2 requests 的使用

urllib 对于网页验证和 Cookie 设置时，需要创建根据指定的 Handler 对象创建 Opener
对象，另外实现 POST 和 PUT 等请求时的写法也比较繁琐，我们接下来学习封装程度更高
的请求库 —— requests。

### 2.2.1 准备工作

创建虚拟环境，安装 requests 库：

```bash
# 更新 pip 到最新版本
python -m pip install --upgrade pip
# 创建虚拟环境 requests-env
python -m venv requests-env
# 进入指定目录，激活虚拟环境
cd requests-env
.\requests-env\Scripts\activate
# 在虚拟环境内安装 requests
python -m pip install requests
```

查看 requests 安装版本：

```python
import requests

print(requests.__version__)
```

### 2.2.2 实例引入

urllib 库中的 urlopen 方法实际上是以 GET 方式请求网页，requests 库中相应的方法是
get 方法：

```python
import requests

r = requests.get('https://www.baidu.com')
print(type(r))      # <class 'requests.models.Response'>
print(r.status_code)        # 200
print(type(r.text))     # <class 'str'>
print(r.text[:100])
print(r.cookies)        # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
```

requests 库的其他请求类型：

```python
r = requests.get('https://www.httpbin.org/get')
r = requests.get('https://www.httpbin.org/post')
r = requests.get('https://www.httpbin.org/put')
r = requests.get('https://www.httpbin.org/delete')
r = requests.get('https://www.httpbin.org/patch')
```

### 2.2.3 GET 请求

#### 基本示例

```python
import requests

r = requests.get('https://www.httpbin.org/get')
print(r.text)

# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "www.httpbin.org",
#     "User-Agent": "python-requests/2.32.5",
#     "X-Amzn-Trace-Id": "Root=1-68f99b96-145bb040229c70b003c34d03"
#   },
#   "origin": "111.46.1.131",
#   "url": "https://www.httpbin.org/get"
# }
```

携带查询参数：

```python
import requests

data = {
    'name': 'robin',
    'age': 29
}

r = requests.get('https://www.httpbin.org/get', params=data)
print(r.text)

# {
#   "args": {
#     "age": "29",
#     "name": "robin"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Host": "www.httpbin.org",
#     "User-Agent": "python-requests/2.32.5",
#     "X-Amzn-Trace-Id": "Root=1-68f99bf2-2d2cff0f11e11b454338e210"
#   },
#   "origin": "111.46.1.131",
#   "url": "https://www.httpbin.org/get?name=robin&age=29"
# }
```

我们将 URL 参数以字典形式传递个 get 方法的 params 参数，requests 会帮我们自动构
造带 params 的 URL。

如果想获取 JSON 格式的响应信息，可直接调用响应对象上的 json() 方法：

```python
import requests

data = {
    'name': 'robin',
    'age': 29
}

r = requests.get('https://www.httpbin.org/get', params=data)
print(type(r.text))
print(r.json())
print(type(r.json()))

# <class 'str'>
# {'args': {'age': '29', 'name': 'robin'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'www.httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-68f99cd1-1f7bd1a721db783902e696e4'}, 'origin': '111.46.1.131', 'url': 'https://www.httpbin.org/get?name=robin&age=29'}
# <class 'dict'>
```

json 方法将返回结果转换成字典格式。

> 注意：如果响应数据返回的不是 json 格式的字符串时，调用 json 会出现解析错误，抛
> 出 json.decoder.JSONDecodeError 异常。

#### 抓取网页

```python
import requests
import re

r = requests.get('https://ssr1.scrape.center/')
# 创建正则表达式，匹配标题部分
pattern = re.compile('<h2.*?>(.*?)</h2>', re.S)
# 根据匹配模式找到所有符合匹配的字符串
titles = re.findall(pattern, r.text)
print(titles)
```

#### 抓取二进制数据

在上面，我们抓取的是网站的一个页面，实际上返回的是一个 HTML 文档。要想抓取图片、
音频、视频等文件，我们需要以二进制数据的形式进行抓取。

```python
import requests
import re

r = requests.get('https://ssr1.scrape.center/static/img/favicon.ico')
print(r.text)
print(r.content)
```

通过打印结果来看，r.text 中出现了乱码，r.content 的前面带有一个 b，代表这是
bytes 类型的数据。由于图片是二进制数据，所以前者在打印时会转换成 str 类型，也就
是图片直接转化为字符串，理所当然会出现乱码。

我们可以将刚才提取到的信息保存下来：

```python
import requests
import re

r = requests.get('https://ssr1.scrape.center/static/img/favicon.ico')
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
```

这里的 open 方法，其第一个参数是文件名称，第二个参数代表以二进制写的形式打开文件
，可以想文件里写入二进制数据。

同样的，我们也可以使用这种方式获取音频和视频文件。

#### 添加请求头

我们可以通过 headers 参数设置 Request Headers。

```python
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'
}
r = requests.get('https://ssr1.scrape.center', headers=headers)
print(r.text)
```
