# 第 1 章 初见网络爬虫

## 1.1 网络连接

数据如何在网络中传输。

编写第一个网络爬虫：

```py
from urllib.request import urlopen

html = urlopen('https://pythonscraping.com/pages/page1.html')
print(html.read())
```

其中 urllib 是 Python 的标准库，包含了从网页请求数据，处理 cookie，甚至改变请求
头和用户代理这些元数据的函数。

## 1.2 BeautifulSoup 简介

openurl()函数只能请求远程 html 文件，但是无法解析 html 文件，我们将借助
BeautifulSoup 库帮助我们完成 html 解析。

### 1.2.1 安装 BeautifulSoup

BeautifulSoup 属于第三方库，因此需要单独安装。建议创建虚拟环境，在虚拟环境中安装
，避免全局安装冲突。

```bash
# 创建虚拟环境
python -m venv scraping_env
cd scraping_env
# 激活虚拟环境
 .\Scripts\activate.bat
# 安装依赖
python -m pip install beautifulsoup4
```

验证是否安装成功，我们在虚拟环境处于激活状态下，打开 python 交互式命令行，导入
BeautifulSoup：

```bash
from bs4 import BeautifuSoup
```

如果上述代码能够正常运行，说明我们在虚拟环境下安装 beautifulsoup4 成功了，接下来
可以使用该库解析 html 内容了。

### 1.2.2 运行 BeautifulSoup

beautifulsoup 库最常用的对象就是 BeautifulSoup。

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)    # <h1>An Interesting Title</h1>
print(type(bs)) # <class 'bs4.BeautifulSoup'>
```

输出结果：

```shell
<h1>An Interesting Title</h1>
<class 'bs4.BeautifulSoup'>
```

其中 bs 是一个 BeautifulSoup 对象。我们可以通过它访问我们解析之后的 html 内容。
除了传递 html 文字字符串，BeautifulSoup 还可以使用 urlopen()直接返回的文件对象作
为参数，而不需要调用 read()将其转换成字符串。

```py
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)    # <h1>An Interesting Title</h1>
print(type(bs)) # <class 'bs4.BeautifulSoup'>
```

BeautifulSoup 第一个参数是该对象所基于的 HTML 文本，第二个参数指定了我们希望
BeautifulSoup 用来创建该对象的解析器。

html.parser 是 Python3 中的一个解析器，不需要单独安装。另一个常用的解析器是
lxml，可以通过 pip 安装：

```bash
python -m pip install lxml
```

BeautifulSoup 使用 lxml 解析器时，还需要改变解析器参数：

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'lxml')
print(bs.h1)    # <h1>An Interesting Title</h1>
print(type(bs)) # <class 'bs4.BeautifulSoup'>
```

和 html.parser 相比，lxml 的有点在于解析“杂乱”或者包含错误语法的 HTML 代码的性能
更优一些。它可以容忍并修正一些问题，例如未闭合的标签、未正确嵌套的标签，以及缺失
的头标签或正文标签。lxml 比 html.parser 更快，但是考虑网络本身的速度总是我们最大
的瓶颈，在网页抓取中速度并不是一个必备的优势。

lxml 的一个缺点是它必须单独安装，并且它依赖于第三方的 C 语言库。

另一个常用的 HTML 解析器是 html5lib。和 lxml 一样，html5lib 也是一个具有容错性的
解析器，它甚至可以容忍语法更糟糕的 HTML。它也依赖于外部依赖，并且比 lxml 和
html.parser 都慢。

可以通过安装并将 html5lib 字符串传递给 BeautifulSoup 对象来使用它：

```py
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html, 'html5lib')
print(bs.h1)    # <h1>An Interesting Title</h1>
print(type(bs)) # <class 'bs4.BeautifulSoup'>
```

### 1.2.3 可靠的网络连接以及异常的处理

Web 是十分复杂的。网页数据格式不友好、网站服务器司机、目标数据的标签找不到，都是
很麻烦的事情。

如果 html 网页资源在服务器上不存在，urlopen 则会抛出 HTTPError 异常；如果服务器
不存在，urlopen 则抛出 URLError 异常。我们可以通过增加异常捕获来避免程序执行失败
：

```py
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html, 'html5lib')
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server cloud not be found!")
else:
    print(bs.h1)    # <h1>An Interesting Title</h1>
    print(type(bs)) # <class 'bs4.BeautifulSoup'>
```

即使从服务器成功获取网页，如果网页上的内容并非完全是我们期望的那样，仍然可能会出
现异常。每当我们调用 BeautifulSoup 对象里的一个标签时，增加一个检查条件以保证标
签确实存在是很聪明的做法。如果想要调用的标签不存在时，BeautifulSoup 就会返回
None 对象。不过，如果再调用这个 None 对象下面的子标签，就会发生 AttributeError
错误。

```py
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_title(url):
    """
    获取指定url对应的网页资源，并解析标题
    """

    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    try:
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title


title = get_title('http://pythonscraping.com/pages/page1.html')
if title == None:
    print("Title cloud not be found!")
else:
    print(title)
```

输出如下：

```shell
<h1>An Interesting Title</h1>
```
