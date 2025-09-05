# 第 7 章 用户输入和 while 循环

## 7.1 input() 函数的工作原理

input()函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python 将其赋给
一个变量，以便使用。

```python
# 用input()函数获取用户输入，并打印用户输入
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# Tell me something, and I will repeat it back to you: Hello everyone!
# Hello everyone!
```

input()函数接受一个参数，即要向用户显示的提示(prompt)，让用户知道该输入什么样的
信息。

### 7.1.1 编写清晰的提示

每当使用 input()函数时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信
息——能指出用户应该输入什么信息的任何提示都行。

通过在提示末尾添加一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何
处。

```python
# 给input() 函数指定参数，便于给用户提供清晰的提示
name = input("Please enter your name: ")
print(f"Hello, {name}!")
# Please enter your name: Robin
# Hello, Robin!
```

如果提示信息较长，可先将提示赋给一个变量，再将这个变量传递给 input()函数。

```python
# 对于提示信息较长的时候，可以先将提示信息存在一个变量中，在给input()函数传入该变量
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# If you share your name, we can personalize the messages you see.
# What is your first name? Robin

# Hello, Robin!
```

### 7.1.2 使用 int() 函数获取数值输入

在使用 input()函数时，Python 会将用户输入解读为字符串。在使用 input()函数时
，Python 会将用户输入解读为字符串。

```python
Type "help", "copyright", "credits" or "license" for more information.
>>> age = input("How old are you? ")
How old are you? 29
>>> age >= 18
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    age >= 18
TypeError: '>=' not supported between instances of 'str' and 'int'
```

为了解决这个问题，可使用函数 int()将输入的字符串转换为数值，确保能够成功地执行比
较操作：

```python
>>> age = int(input("How old are you? "))
How old are you? 29
>>> age >= 18
True
```

> 注意：在将数值输入用于计算和比较前，务必将其转换为数值表示。

### 7.1.3 求模运算

在处理数值信息时，求模运算符(%)是个很有用的工具，它将两个数相除并返回余数：

```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

如果一个数可被另一个数整除，余数就为 0，因此求模运算将返回 0。可利用这一点来判断
一个数是奇数还是偶数：

```python
# 利用求模运算判断用户输入的数是奇数还是偶数
number = input("Enter a number, i will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
```

## 7.2 while 循环简介

for 循环用于针对集合中的每个元素执行一个代码块，而 while 循环则不断地运行，直到
指定的条件不再满足为止。

### 7.2.1 使用 while 循环

可以使用 while 循环来数数。

```python
# 用while循环来输出1~5之间的数字
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

### 7.2.2 让用户选择何时退出

可以使用 while 循环让程序在用户愿意时不断地运行，如下面的程序 parrot.py 所示。我
们在其中定义了一个退出值，只要用户输入的不是这个值，程序就将一直运行：

```python
# 给while循环指定退出的条件，在符合退出条件时结束while循环
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':   # 避免quit被打印出来
        print(message)
```

### 7.2.3 使用标志

在要求满足很多条件才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活
动状态。这个变量称为标志(flag)，充当程序的交通信号灯。可以让程序在标志为 True 时
继续运行，并在任何事件导致标志的值为 False 时让程序停止运行。这样，在 while 语句
中就只需检查一个条件：标志的当前值是否为 True。然后将所有测试（是否发生了应将标
志设置为 False 的事件）都放在其他地方，从而让程序更整洁。

```python
# 使用标志控制循环
active = True
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end program. "
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

### 7.2.4 使用 break 退出循环

如果不管条件测试的结果如何，想立即退出 while 循环，不再运行循环中余下的代码，可
使用 break 语句。

```python
# 使用 break 结束循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}.")
```

> 注意：在所有 Python 循环中都可使用 break 语句。例如，可使用 break 语句来退出遍
> 历列表或字典的 for 循环。

### 7.2.5 在循环中使用 continue

要返回循环开头，并根据条件测试的结果决定是否继续执行循环，可使用 continue 语句，
它不像 break 语句那样不再执行余下的代码并退出整个循环，而是选择性地跳过某些循环
。

```python
# 使用 continue 跳过指定循环
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 != 0:
        continue

    print(current_number)
```

### 7.2.6 避免无限循环

每个 while 循环都必须有结束运行的途径，这样才不会没完没了地执行下去。

要避免编写无限循环，务必对每个 while 循环进行测试，确保它们按预期那样结束。如果
希望程序在用户输入特定值时结束，可运行程序并输入该值。如果程序在这种情况下没有结
束，请检查程序处理这个值的方式，确认程序至少有一个地方导致循环条件为 False 或导
致 break 语句得以执行。

## 7.3 使用 while 循环处理列表和字典
