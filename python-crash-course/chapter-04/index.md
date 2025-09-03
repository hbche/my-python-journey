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

### 4.4.1 切片
