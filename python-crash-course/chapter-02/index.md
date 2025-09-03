# 第 2 章 变量和简单的数据类型

## 2.1 运行 hello_world.py 是发生的情况

## 2.2 变量

```python hello_world.py
message = 'Hello Python world!'
print(message)
```

```python hello_world.py
message = 'Hello Python world!'
print(message)

message = 'Hello Python Crash Course world!'
print(message)
```

在程序中，可随时修改变量的值，

### 2.2.1 变量的命名和使用

- 变量名只能以字母、数字、下划线组成，只能以字符和下划线打头。
- 变量名不能包含空格
- 不要将 Python 关键字和函数名用作变量名
- 变量名应既简短又具有描述性
- 慎用小写字母 l 和大写字母 O

### 2.2.2 如何在使用变量时避免命名错误

### 2.2.3 变量是标签

## 2.3 字符串

### 2.3.1 使用方法修改字符串的大小写

```python
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
```

### 2.3.2 在字符串中使用变量

```python
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}")
```

### 2.3.3 使用制表符或换行符来添加空白

```python
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")
```

### 2.3.4 删除空白

```python
favorite_language = ' python   '
favorite_language.rstrip()  # ' python'
favorite_language.lstrip()  # 'python   '
favorite_language.strip()   # 'python'
favorite_language           # ' python   '
```

可以使用 lstrip() 删除字符串左侧空白，使用 rstrip() 删除字符串右侧空白，使用 strip() 删除两侧空白。

lstrip、rstrip 和 strip 方法不会改变调用字符串。

### 2.3.5 删除前缀

```python
we_read_url = 'https://weread.qq.com/'
we_read_url.remomvepreffix('https://')  # weread.qq.com
we_read_url                             # https://weread.qq.com/
```

`removeprefix` 可以删除字符串中指定的字符串前缀。`removesuffix` 可以删除字符串中指定的字符串后缀

### 2.3.6 如何在使用字符串时避免语法错误

## 2.4 数

### 2.4.1 整数

在 Python 中，可对整数(integer)执行加(+)减(-)乘(\*)除(/)运算。

```python
2 + 3       # 5
3 - 2       # 1
2 * 3       # 6
3 / 1       # 3.0
3 ** 2      # 9
3.0 ** 2    # 9.0
3 ** 2.0    # 9.0
```

整数进行除法运算返回的是浮点数。其余运算中如果存在一个数是浮点数，结果也是浮点数。

### 2.4.2 浮点数

```python
0.2 + 0.1       # 0.30000000000000004
3 * 0.3         # 0.30000000000000004
```

### 2.4.3 整数和浮点数

1. 将任意两个数相除，结果总是浮点数，即便这两个数都是整数且能整除
2. 在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数

### 2.4.4 数中的下划线

### 2.4.5 同时给多个变量赋值

可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。这种做法最常用于将一系列数赋给一组变量。可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。这种做法最常用于将一系列数赋给一组变量。

```python
x, y, z = 0, 1, 2
```

### 2.4.6 常量

```python
MAX_CONNECTIONS = 5000
```

## 2.5 注释

### 2.5.1 如何编写注释

```python
# 向大家问好
print("Hello Python People!")
```

### 2.5.2 该编写什么样的注释

编写注释的主要目的是阐述代码要做什么，以及是如何做的。

## 2.6 Python 之禅

```bash
import this
```

```
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

## 2.7 小结

1. 如何使用变量、变量命名规则
2. 字符串
3. 整数、浮点数
4. 注释
5. Python 之禅
