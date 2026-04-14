# 第 12 章 网络编程

## 网络编程基础

1. 所谓互联网的连接（其实是两台计算机的通信）：应用层---传输层---互联网层---链路层--WiFi/太网连接---数据在网络中多次运转---达到网络服务器（或者其他设备）
2. 数据再通过这类层级---运行网络应用程序---回到客户端---数据在网络中15次运转---显示在屏幕上。

其核心思想：编写一个python程序，通过传输层与另一台服务器上的应用程序进行通信，另一台服务器接收数据并返回响应。

1. 所谓传输端：假设存在一条从一端到另一端的理想通道（你这发出信息，对面可以接收到。对面同理）
2. 这种通信称为“两个应用程序之间的交互”。
3. 实际上一端是你的py程序，另一端是网络服务器。

- 这种通信类似于打电话，不过计算机在一秒之内进行数百次甚至数千次😎，我们把它称之为“socket”（套接字）

套接字的工作原理：与一个特定的网络服务器通信，要知道其名称，编号和地址，以及指定是哪个应用程序(对应其服务器上不同的接口---TCP/IP端口)

```py
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
```

mysock类似给你个接头而mysock.connect是你的接口，‘接口’中输入域名即完成。

## 使用 HTTP 协议的Python

设计HTTP之初是为了获取网页，它是一套规则，使得浏览器能够从网络上获取文档，本质上是一套标准化的形式.

1. 超文本核心：在任何文档中，存在着指向其他文档的链接（它的新颖之处在于在HTTP出现之前，已有方法从服务器中获得数据，但HTTP可以在文档中嵌入指向其他文档链接）
2. 通过发送所谓GET请求获取文档，随后接受文档内容，解析其内容，最后呈现给用户

3. 当你浏览网页时，点击了一个链接（其显示为蓝色）点击后即显示第二页。
4. 浏览器捕捉到了你的点击动作，识别到点击了某个元素，它就会解析当前页面的HTML的代码，以及确定要连接哪个Web服务器，使用哪个接口和需要获取哪个文档。
5. 浏览器通过套接字连接到端口---发送一个GET的请求---请求被发送到端口80---到达Web服务器---解析请求---最终以HTML的形式返回.

表面上你点击链接就看到了新的页面，实际上它已经完成了一期复杂的循环

使用 Python完成一个HTTP请求：

```py
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
```

1. 创建socket---打开一道通向计算机外部的大门
2. 输入服务器，连接端口80，并建立套接字---实现一个连接到服务器的套接字。
3. ‘mysock.send'---服务器已有，那么利用它传输或获取数据

## 字符、ASCII码和Unicode

宇宙之初，计算机本不懂什么是字母，它只懂数字。那么问题来了：数字和字母是如何搭上一条船的呢？

### ASCII编码

- 20世纪80年代科学家发明了一种称为“ASCII”（美国信息交换标准代码）的编码方式建立数字和字母之间的映射关系，将特定的数字与字母一一对应。
- ASCII有0-128个字符，我们通常用“ord”函数来查询字母对应的数字

- 早期我们将字符储存在一个字节的内存里，即八位内存
- `ord()` 方法能够获取简单的 ASCII 编码字符对应的数字
- 我们也可以用十进制二进制来表示数字

```py
print(ord('A')) # 65
print(ord('H')) # 72
print(ord('a')) # 97
print(ord('e')) # 101
print(ord('\n'))    # 10
```

- 不过ASCII只是其中一种表达方式，世界上字符集不同的表达方式导致了互相难以通信，就此人们发明了 “Unicode”编码 来解决这一问题 。
- Unicode涵盖数亿种不同的字符，数百种不同的字符集，成为一种通用编码。

### 多字节编码

为了表示计算机必须处理的广泛字符范围，我们使用多个字节来表示字符。

- UTF-16: 固定长度，2 字节
- UTF-32: 固定长度，4 字节
- UTF-8: 1~4字节
  - 向上兼容 ASCII 编码
  - ASCII 与 UTF-8 之间的自动检测
  - UTF-8 是推荐用于系统间数据交换的编码规范

- 实践证明人们找到了最好的数据传输编码方式---UTF-8（全球通用）

有编码就有解码，不过到底是ASCII还是UTF-8呢，这里有一套解码py操作。

### 使用 Python 完成字符与字节直接的转换

- 当我们与外部资源（如网络套接字）通信时，发送的是字节流，因此需要将 Python 3 字符串编码为指定的字符编码
- 当我们从外部资源读取数据时，必须根据字符集对其进行解码，才能使其在 Python 3 中正确表示为字符串

```py
while True:
    data = mysock.recv(512)
    if ( len(data) < 1) :
        break
    mystring = data.decode()
    print(mystring)
```

解码的过程就是将字节数据转化为Unicode，而编码就是将字符串转化为字节。

## 使用 urllib 的 Python

python一个将网络世界简单化的工具，所谓套接字仅用10行代码来获取网页，不好意思！一个名为urllib的库更是为我们自动完成这些任务！ 😮😏

由于 HTTP 协议极为常用，我们拥有一个库，可以代替我们处理所有套接字操作，并使网页的访问如同读取文件般简单。

```py
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief
```

### 使用方法

1. 导入库组件，调用 urllib.request.urlopen
2. 打开文件
3. 通过 for 逐行遍历数组
4. 通过解码获取字节的字符串版本

```py
import urllib.request, urllib.parse, urllib.error

word_map = dict()

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words = line.decode().split()
    for word in words:
        word_map[word] = word_map.get(word, 0) + 1

print(word_map)
```

我们可以就编写一个程序，下载一个网页，查找该网页中的所有链接，然后继续下载所有这些链接指向的网页，循环往复:

```py
import urllib.request
import re

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')

for line in fhand:
    line = line.decode().strip()
    print(line)
```

## 解析网页

### 如何解析HTML---网络爬虫

什么是网络爬虫

- 当程序或脚本伪装成浏览器，获取网页、查看这些网页、提取信息，并继续浏览更多网页时
- 搜索引擎会抓取网页——我们称之为“网络蜘蛛爬行”或“网络爬虫”。

### 为什么需要网络爬虫？

- 提取数据——特别是社交数据——谁链接到谁？
- 从某个不具备“导出功能”的系统中取回你自己的数据。
- 监控网站以获取新信息
- 抓取网页为搜索引擎建立数据库
- 网络爬虫重点在于解析返回的HTML的内容，然而浏览器获取HTML时可以容忍大量的语法错误，所以对我们试图修复并解析所有的链接具有很大的困扰。

### BeautifulSoup

- 你可以用复杂的方式进行字符串搜索
- 也可以使用名为 BeautifulSoup 的免费软件库。

以下代码：将数据导入BS库中，请求一个URL地址，打开并执行read操作

BS会处理所有杂乱的错误，然后就可以正常寻找你的标签，你的链接。

```py
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.bing.com/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
```
