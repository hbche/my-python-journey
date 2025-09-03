# 第 4 章 操作列表

## 4.1 遍历整个列表

使用 for 循环遍历列表：

```python
# 使用 for 循环遍历列表
magicians = []
magicians.append('alice')
magicians.append('david')
magicians.append('carolina')
for magician in magicians:  # for循环结构
    print(magician)         # 使用缩进表示for循环结构内部的逻辑
```

### 4.1.1 深入研究循环

### 4.1.2 在 for 循环中执行更多操作

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
```

在 for 循环中项包含多少行代码都可以。每行缩进都表示改行代码是 for 循环的一部分。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
```

### 4.1.3 在 for 循环结束后执行一些操作

在 for 循环后面，没有缩进的代码都不属于循环内的逻辑，只在循环结束后执行一次。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

print("Thank you, everyone. That was a great magic show!")
```

## 4.2 避免错误缩进

### 4.2.1 忘记缩进

位于 for 语句后面且属于循环组成部分的代码行，一定要缩进。

### 4.2.2 忘记缩进额外的代码行

虽然循环能够正常运行且不会出错，但是结果出人意料。

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}!\n")    # 只会对最后一位魔术师表示感谢
# Alice, that was a great trick!
# David, that was a great trick!
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina!
#
```

### 4.2.3 不必要的缩进

```python
message = "Hello Python world!"
    print(message)
#   File "\my-python-journey\python-crash-course\chapter-04\hello_world.py", line 2
#     print(message)
# IndentationError: unexpected indent
```

### 4.2.4 循环后不必要的缩进

```python
# 循环后不必要的缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

    print("Thank you, everyone. That was a great magic show!")      # 错误缩进，导致原本执行一次的语句，变为循环内部逻辑，随着循环一起执行
```

### 4.2.5 遗漏冒号

## 4.3 创建数值列表

### 4.3.1 使用 range() 函数

```python
# 使用 range 函数快速生成指定范围的数，第一个参数是起始索引，第二个参数是结束索引，生成范围不包含结束索引
for value in range(1, 5):
    print(value)
# 1
# 2
# 3
# 4
```

### 4.3.2 使用 range() 创建数值列表

要创建数值列表，可以使用 list()函数将 range()的结果直接转换为列表。

```python
# 使用 list() 函数将range()函数返回的结果转换成数值列表
numbers = list(range(1, 5))
print(numbers)                  # [1, 2, 3, 4]
```

使用 range() 函数还可指定第三个参数，用于指定生成范围的步长，即每隔多少取一个数
：

```python
# 使用 range() 函数的步长参数
numbers = list(range(2, 11, 2))
print(numbers)          # [2, 4, 6, 8, 10]
```

### 4.3.3 对数值列表进行简单的统计计算

最小值、最大值和总和

```python
# 对数值列表进行简单的统计计算
digits = list(range(1, 10))
digits.append(0)
print(min(digits))      # 最小值
print(max(digits))      # 最大值
print(sum(digits))      # 总和
```

### 4.3.4 列表推导式

列表推导式将 for 循环和创建新元素的代码合并成一行，并自动追加新元素，自动生成列
表。

```python
# 使用列表推导式生成平方数列表
squares = [value**2 for value in range(1, 11)]
print(squares)      # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 4.4 使用列表的一部分

在 Python 中处理列表的部分元素成为切片。

### 4.4.1 切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。

我们可以使用切片语法生成列表的任意子集。

```python
# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])         # ['charles', 'martina', 'michael']
```

如果没有指定第一个索引，Python 将自动从第一个元素开始：

```python

# 省略第一个索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])              # ['charles', 'martina', 'michael', 'florence']
```

要让切片终止于列表末尾，可省略切片的结尾索引：

```python
# 省略结尾索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])          # ['michael', 'florence', 'eli']
```

也可以使用负数索引：

```python
# 负数索引
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])          # ['michael', 'florence', 'eli']
```

类似 range 函数，切片语法也支持第三个参数，表示步长，即在范围索引内，每相隔多少索引取一个元素

```python
# 指定步长
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[::2])          # ['charles', 'michael', 'eli']
```

### 4.4.2 遍历切片

可使用 for 循环遍历切片。

```python
# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("There are the first three players on my team:")
for player in players[:3]:
    print(player.title())
```

### 4.4.3 复制列表

要复制列表，可以创建一个覆盖列表全部范围的切片。

```python
# 李泳切片复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)             # ['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friend_foods)         # ['pizza', 'falafel', 'carrot cake']
```

为了核实切片确实生成了一个新的列表，我们做如下修改：

```python
# 确认切片生成的列表是一个新的切片
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)         # ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\nMy friend's favorite foods are:")
print(friend_foods)     # ['pizza', 'falafel', 'carrot cake', 'ice cream']
```

## 元组

列表是可以修改的序列。而不可修改的列表成为元祖。

### 4.5.1 定义元组

元组看起来像列表一样，只不过使用圆括号标识。定义元组后，可以使用索引来访问元素。

```python
# 定义元组
dimensions = (200, 50)
print(dimensions[0])        # 200
print(dimensions[1])        # 50
```

如果尝试修改元组中的元素，将出发 Python 报错：

```python
# 修改元组中的元素
dimensions = (200, 50)
dimensions[0] = 100

# Traceback (most recent call last):
#   File "my-python-journey\python-crash-course\chapter-04\dimensions.py", line 8, in <module>
#     dimensions[0] = 100
#     ~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
```

只定义有一个元素的元组，为了与表达式区分，元组必须有个逗号：

```python
my_tuple = (200,)
```

### 3.5.2 遍历元组中的所有值

像列表一样，可以使用 for 循环遍历列表：

```python
# 使用 for 循环遍历元组
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
```

### 4.5.3 修改元组变量

虽然不能修改元组的元素，但是可以给表示元组的变量赋值：

```python
# 给元组变量赋值
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)        # 200 50

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)        # 400 100
```

## 4.6 设置代码格式

### 4.6.1 格式设置指南

### 4.6.2 缩进

### 4.6.3 行长

建议每行不超过 80 个字符。

### 4.6.4 空行

可使用空行分隔程序中的不同部分。

### 4.6.5 其他格式设置指南

更多格式设置指南见 PEP 8 (Python Enhancement Proposal, Python 增强提案)

## 4.7 小结

1. 遍历列表
2. 创建简单的数值列表
3. 切片
4. 元组
5. 代码格式设置
