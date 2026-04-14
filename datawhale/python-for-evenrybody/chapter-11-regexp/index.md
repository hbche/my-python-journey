# 第 11 章 正则表达式

> 什么是正则表达式？
>
> 正则表达式是一种用于判断一组字符串是否符合特定模式的方法。正则表达式的核心思想
> 在于，它不仅仅局限于匹配具体的字符，而是提供了一种近乎微型通配符编程表达式的机
> 制，能够灵活地定义和匹配复杂的文本模式。
>
> 总的来说，它用一套带”魔法符号“的字符串来描述[我要的字符串长什么样]，只要符合规
> 则，就算匹配成功。

正则表达式元字符速查指南

| 符号     | 含义                                                             |
| -------- | ---------------------------------------------------------------- |
| `^`      | 匹配字符串的起始位置的内容                                       |
| `$`      | 匹配字符串的结束位置的内容                                       |
| `.`      | 匹配除去换行符 `\n` 之外的任意一个字符                           |
| `\s`     | 匹配空格字符                                                     |
| `\S`     | 匹配任意非空格字符                                               |
| `*`      | 表示符号前的元素会匹配 0 次或多次                                |
| `+`      | 表示符号前的元素会匹配 1 次或多次                                |
| `?`      | 表示符号前的元素可选，并且最多匹配 1 次                          |
| `[]`     | 匹配多个字符，在方括号内部的所有字符都会被匹配                   |
| `[abc]`  | 匹配集合中任意一个字符，此处指匹配 `a`、`b`、`c`中的任意一个字符 |
| `[^xyz]` | 匹配不在集合中的任意一个字符                                     |
| [a-z0-9] | 支持连续区间（如：a-z、0-9）                                     |
| `()`     | 提取范围                                                         |

## 正则表达式的使用

1. 拿钥匙开武器库

   在 python 中，正则表达式并不像字符串、列表或字典那样直接内置于基础语言中。因此，
   我们需要在程序开头使用 import 语句，将正则表达式库引入到当前程序中。

   ```py
   # 在文件的最开头导入 re 模块
   import re
   ```

2. 两个常用武器库

   | 函数名称     | 作用                                             |
   | ------------ | ------------------------------------------------ |
   | `re.search`  | 匹配符合样式的第一个位置，返回包含匹配信息的对象 |
   | `re.findall` | 匹配字符串中的全部样式，返回组合列表             |

   `re.search`: 这是正则表达式库中的搜索功能，它会返回一个布尔值，告诉你是否匹配成
   功，就像是一个智能的查找工具。类似 js 中正则对象的 `test` 。

   `re.findall`: 像是提取功能，它比切片操作更强大，其核心思想是定位某段内容的起始和
   结束位置，并将其提取出来。

   下面是一个 demo，用于查找文档中`以 # 开头的行`：

   ```py
   hand = open('index.md', mode='r', encoding='utf-8')
   with hand:
       for line in hand:
           line = line.strip()
           if line.find('#') >= 0:
               print(line)
   ```

   下面改用正则表达式查找：

   ```py
   import re

   hand = open('index.md', mode='r', encoding='utf-8')
   with hand:
       for line in hand:
           line = line.strip()
           if re.search('^#', line):
               print(line)
   ```

   我们再看两个正则表达式的示例：

   正则表达式 `^X.*:` 表示以大写字母 X 开头，后跟任意数量的字符，最后以冒号结尾的行
   。其中 X 和冒号不是正则表达式的元字符，只有 `^`、`.`和`*`是正则表达式的元字符。

   正则表达式 `^X-\S+:` 表示以 `X-` 开头，后跟任意个非空格字符，最后以冒号结尾的字
   符串。

## 数据提取

- re.research(): 由字符串是否匹配正则表达式决定返回 True/False
- re.findall(): 将模胚的字符串提取出来

### 提取数字

```py
import re

prompt = 'My 2 favoriate numbers are 19 and 42'
# [0-9]表示单一的数字字符。我们在其后添加了一个加号(+)，这表示一个或多个数字字符。在表示一个或多个数字字符时，我们将使用正则表达库中的一个名为findall的函数。
# findall() 会返回匹配正则表达式的一个包含0个或多个子字符串的列表
match_str = re.findall('[0-9]+', prompt)
print(match_str)    # ['2', '19', '42']
```

### 贪婪匹配

```py
import re

prompt = 'From: Using the: character'
match_str = re.findall('^F.+:', prompt)
print(match_str)    # ['From: Using the:']
```

为什么不是"From:"？

重复字符（\* 和 +）会朝两个方向（贪心地）扩展，以匹配可能的最大字符串。

贪婪匹配的原则是：你会得到更大的匹配范围。（贪婪匹配会尽可能地扩大匹配范围，同时仍然满足整个表达式的匹配条件）

非贪婪匹配倾向于选择最短的匹配结果。

并非所有正则表达式重复代码都是贪婪的！
如果你加上一个 ? 字符，+ 和 \* 就会收敛一些……

```py
import re

prompt = 'From: Using the : character'
match_str = re.findall('^F.+?:', prompt)
print(match_str)    # ['From:']
```

在加号或星号之后，我们可以添加一个问号，表示匹配任意字符一次或多次但不要贪婪匹配。

### 提取邮箱

```py
import re

email = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
match_str = re.findall(r'\S+@\S+', email)
print(match_str)    # ['stephen.marquard@uct.ac.za']

email = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# 版本2：带括号精准提取，只提取括号里的部分
match_str = re.findall(r'From (\S+@\S+)', email)
print(match_str)    # ['stephen.marquard@uct.ac.za']
```

### 正则版提取邮箱主机名

```py
import re

email = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# 提取非空白字符
match_str = re.findall('@([^ ]*)', email)
print(match_str)    # ['uct.ac.za']
```

进一步限定，匹配以 From 开头的行：

```py
import re

email = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
match_str = re.findall('^From .*@([^ ]*)', email)
print(match_str)
```

### 提取垃圾邮件置信度的值

```py
import re

hand = open('mbox-short.txt')

numlist = list()
with hand:
    for line in hand:
        line = line.rstrip() #去掉行尾换行符
        #只匹配 X-DSPAM-Confidence: 0.1234 的行，并提取冒号后的数字（含小数点）
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        # #如果提取失败，跳过该行
        if len(stuff) != 1:
            continue
        num = float(stuff[0])
        numlist.append(num)
    print('Maximum: ', max(numlist))    # Maximum:  0.9907
```

### 转义字符

如果待匹配的字符串中出现 "$" "." "[]" 等特殊字符，那么会与正则表达式的特殊字符发生冲突。

使用 `\` 将字符串内的特殊字符进行转义，即告诉 Python：把这个字符当作普通字符处理。

如果你希望某个特殊正则表达式字符表现正常（多数情况下），需在其前面加上反斜杠"

```py
import re

prompt = 'We just received $10.00 for cookies.'
match_str = re.findall(r'\$([0-9.]+)\S', prompt)
print(match_str)    # ['10.0'
```

| 预定义 | 含义                         |
| ------ | ---------------------------- |
| \w     | 匹配数字、字母、下划线       |
| \W     | 匹配非数字、非字母、非下划线 |
| \s     | 匹配空白字符                 |
| \S     | 匹配非空白字符               |
| \d     | 匹配数字                     |
| \D     | 匹配非数字                   |
| \b     | 匹配单词边界                 |
| \B     | 匹配非单词边界               |
