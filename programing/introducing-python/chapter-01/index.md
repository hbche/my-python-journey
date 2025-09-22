# 第 1 章 初探 Python

## 1.1 谜题

## 1.2 小程序

元组示例：

```python
# 打印一个元祖

for countdown in 5, 4, 3, 2, 1, 'hey!':
    print(countdown)
```

列表示例：

```python
# 打印咒语
spells = [
    'Riddikulus!',
    'Wingardium Leviosa!',
    'Avada Kedavra!',
    'Expecto Patronum!',
    'Nox!',
    'Lumos!',
    ]
print(spells[3])
```

字典示例：

```python
# 打印 三个臭皮匠 的台词
quotes = {
    "Moe": "A wise guy, huh?",
    "Larry": "Ow!",
    "Curly": "Nyuk nyuk!",
    }
stooge = 'Curly'
print(stooge, "says:", quotes[stooge])
```

## 1.3 大程序

```python
import webbrowser
import json
from urllib.request import urlopen

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20250917: ")
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf-8')
print(text)
data = json.loads(text)

try:
    old_site = data['archived_snapshots']['closest']['url']
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)
```

下面来对上面的代码进行逐行分析:

1. 从 Python 标准库中导入模块 webbrowser
2. 从 Python 标准库中导入模块 json
3. 从 Python 标准库中导入模块 urllib.request 的 urlopen 函数
4. 空行，以免程序看起来太拥挤
5. 打印一些初始文本
6. 打印问题。询问 URL，读取用户输入，将其存储再变量 site 中
7. 打印另一个问题，这次要读取年、月和日，然后将其保存在变量 era 中
8. 构建字符串变量 url，让 Wayback Machine 查找指定站点当时的副本
9. 连接到 URL 的 web 服务器，请求特定的 web 服务器
10. 获取相应数据流，读取到变量 contents 中，二进制流
11. 将 contents 内容解码为 JSON 格式的字符串并赋值给变量 text
12. 将 text 转换成 data - Python 数据结构
13. 错误检查：尝试运行后面的 4 行代码，如果出现任何错误就执行程序的最后一行（位于 except 之后）
14. 如果能找到站点当时的副本，就从 3 级 Python 字典中提取 URL。注意，该行和接下来两行是缩进的。Python 由此知道接下来几行属于 try。
15. 打印提取出来的 URL
16. 打印后几行后面代码执行将出现什么后果
17. 在 web 浏览器中显示找到的页面
18. 如果前面四行出现任何错误，那么 Python 就直接跳转到这里。

以下是可能执行的一种情况：

```bash
python archive.py
Let's find an old website.
Type a website URL: exampleurl
Type a year, month, and day, like 20250917: 20151022
Found this copy:  http://web.archive.org/web/20220119205649/http://exampleurl/
It should appear in your browser now.
```

下面是依赖第三方库 requests 实现的更为简洁的版本：

```python
import requests
import webbrowser

print("Let's find an old website.")
site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20250917: ")
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"
response = requests.get(url)
data = response.json()
try:
    old_site = data['archived_snapshots']['closest']['url']
    print("Found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)
```

以下是一种可能执行的结果：

```bash
python archive_v2.py
Let's find an old website.
Type a website URL: bilibili.com
Type a year, month, and day, like 20250917: 20200101
Found this copy:  http://web.archive.org/web/20200101233400/https://www.bilibili.com/
It should appear in your browser now.
```

## 1.4 现实世界中的 Python

Python 身影：

- 终端命令行
- GUI
- 客户端 Web 和服务器端 Web
- 云服务
- 移动开发
- 嵌入式设备

## 1.5 Python 和其他语言

## 1.6 为什么选择 Python

## 1.7 为什么不选择 Python

## 1.8 Python2 和 Python3

## 1.9 安装 Python

## 1.10 运行 Python

### 1.10.1 使用交互式解释器

### 1.10.2 使用 Python 文件

### 1.10.3 在集成开发环境 IDE 中开发

## 1.11 Python 的禅意时刻

在终端命令行中输入 Python 进入 Python 交互式解释器；然后执行 `import this` 语句，随即输出的就是 Python 之禅。在输出结束后，执行 `exit()` 可退出 Python 交互式解释器模式，退回到终端模式。

```bash
python

Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
