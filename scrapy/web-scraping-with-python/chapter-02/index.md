# 第 2 章 复杂 HTML 解析

## 2.1 不是一直都要用锤子

## 2.2 再端一碗 BeautifulSoup

通过访问 BeautifulSoup 对象上的标签来访问 html 内容，每次只能访问一个标签的内容
，能否有更快捷的方法呢？我们来看看 BeautifulSoup 中的 find_all(tag_name,
tag_attributes) 方法

```py
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

def get_html(url):
    """
    根据给定的url获取html资源
    """

    try:
        html = urlopen(url)
    except HTTPError:
        return None
    except URLError:
        return None
    else:
        return html


html = get_html('https://www.pythonscraping.com/pages/warandpeace.html')
if html != None:
        bs = BeautifulSoup(html, 'html.parser')
        name_list = bs.find_all('span', {'class': 'green'})
        for name in name_list:
            print(name.get_text())
```

上述代码将按照《战争与和平》中的人物出场顺序显示所有的人名。

调用 bs.find_all(tag_name, tag_attributes)方法可以获得页面中所有指定标签的内容，
不再只是第一个了。

获取人名列表之后，遍历列表中所有的名字，然后打印 name.get_text()，就可以把标签的
内容分开显示了。

> 什么时候使用 get_text()？什么是由应该保留标签？
>
> get_text()会清除我们正在处理的 html 文档中的所有标签，然后返回一个只包含文字的
> Unicode 字符串。假如我们正在处理一个包含许多超链接、段落和其他标签的大段文本时
> ，那么 get_text()会把这些超链接、段落和标签都清除掉，只剩下一串不带标签的文字
> 。
>
> 通常我们在准备打印、存储和操作最终数据时，应该字后才使用 get_text()。一般情况
> 下，我们应该尽可能地保留 HTML 文档的标签结构。

### 2.2.1 BeautifulSoup 的 find()和 find_all()

借助 find()和 find_all()，我们可以通过标签的不同属性轻松地过滤 HTML 页面，查找需
要的标签组或单个标签。

```py
find(tag, attributes, recursive, string, keywords)
find_all(tag, attributes, recursive, string, limit, keywords)
```

大部分场景下，我们只需要使用 tag 和 attributes 参数即可。但是，我们还是有必要了
解一下所有参数。

| 参数名     | 参数说明                                                                                                                     | 使用举例                                                                                                   |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| tag        | 可以传递一个标签的名称或多个标签名称组成的标签列表                                                                           | `find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])`                                                           |
| attributes | 字典类型，用来传递一个标签的若干属性和对应的属性值。                                                                         | `find_all('span', {'class': {'green', 'red'}})`                                                            |
| recursive  | 布尔类型，用来标识是否支持递归查找，查找子标签以及子标签的子标签。默认为 True                                                | True\False                                                                                                 |
| string     | 字符串类型，给出匹配内容，按照标签的内容去匹配，而不是标签的属性                                                             | `find_all(string="the prince")`                                                                            |
| limit      | 正整数，限制查找的数量，只作用于`find_all`，`find`其实等价于 limit=1 时的 `find_all`，如果想获取页面中按顺序出现的前几项结果 | -                                                                                                          |
| keywords   | 用于选择具有指定属性的标签 -                                                                                                 | `find_all(id='title', class_='text')`，返回在 class\_属性中包含单词 text 并且在 id 属性中包含 title 的标签 |

#### keyword 参数和 attributes 的注意事项

关键字 keywords 参数其实是冗余的。通过 keywords 参数指定的查询，可以通过其他形式
完成：

```py
bs.find_all(id="text")
bs.find_all(attrs={"id": "text"})
```

另外，用 keyword 偶尔会出现问题，尤其是在用 class 属性查找标签的时候，因为 class
是 Python 中受保护的关键字。也就是说，class 是 Python 语言的保留字，在 Python 程
序里是不能当作变量或参数名使用的。我们运行如下程序会报错：

```py
bs.find_all(class="green")
```

不过，我们可以用 BeautifulSoup 提供的有点臃肿的方案，在 class 后面增加一个下划线
：

```py
bs.find_all(class_="green")
```

另外，也可以用属性参数把 class 用引号抱起来：

```py
bs.find_all(attrs={'class': 'green'})
```
