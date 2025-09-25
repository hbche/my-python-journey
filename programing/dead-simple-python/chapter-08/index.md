# 第 8 章 错误和异常

## 8.1 Python 中的异常

异常：计算机正常处理的终端，通常由错误条件引起，可以由程序的另一部分处理。

以下给出一个猜数字的游戏来介绍 Python 中的异常：

```python
import random

def generate_puzzle(low=1, high=100):
    """创建一个生成随机数的函数，默认生成1~100之间的整数"""
    print(f"I'm thinking of a number between {low} and {high}.")
    return random.randint(low, high)

def make_guess(target):
    """根据随机生成的数字，获取用户输入，并判断是否猜对"""

    # 获取用户输入
    guess = int(input("Guess: "))

    # 判断用户输入数字是否是随机生成的数字
    # 如果用户猜对了，返回结果True
    if guess == target:
        return True

    # 如果没有猜对，需要给出提示，并返回结果False
    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    return False

def play(tries=8):
    """给定尝试次数，开始游戏"""

    # 生成随机数
    target = generate_puzzle()

    # 根据给定的次数进行游戏
    while tries > 0:
        # 如果猜对了就退出游戏
        if make_guess(target):
            print("You win!")
            return
        # 否则减少尝试次数，打印剩余尝试次数
        tries -= 1
        print(f"{tries} tries left.")

    print(f"Game over! The answer was {target}.")

if __name__ == "__main__":
    # 如果是主程序就执行
    play()
```

如果在游戏过程中，我们尝试输入非整数字符，程序就会报异常，以下是一种可能出现的情
况：

```bash
I'm thinking of a number between 1 and 100.
Guess: Hello
Traceback (most recent call last):
  File "\dead-simple-python\chapter-08\demos\number_guess.py", line 46, in <module>
    play()
    ~~~~^^
  File "\dead-simple-python\chapter-08\demos\number_guess.py", line 35, in play
    if make_guess(target):
       ~~~~~~~~~~^^^^^^^^
  File "\dead-simple-python\chapter-08\demos\number_guess.py", line 12, in make_guess
    guess = int(input("Guess: "))
ValueError: invalid literal for int() with base 10: 'Hello'
```

## 8.2 阅读异常信息

## 8.3 捕获异常：LBYL 和 EAFP

在许多编程语言中，通常的做法是在尝试将输入转换为整数之前测试它们。这称为“先看后
跳”(Look Before You Leap, LBYL)哲学。

Python 有着不同的做法，官方称之为“请求宽恕比请求许可更容易”(Easier to Ask
Forgiveness than Permission, EAFP)。我们不是组织错误，而是接受它们，并使用 try
语句来处理异常情况。

尝试将 make_guess() 函数重写为使用异常处理的形式：

```python
def make_guess(target):
    """根据随机生成的数字，获取用户输入，并判断是否猜对"""

    # 获取用户输入
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Enter an integer.")

    # 判断用户输入数字是否是随机生成的数字
    # 如果用户猜对了，返回结果True
    if guess == target:
        return True

    # 如果没有猜对，需要给出提示，并返回结果False
    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    return False
```

## 8.4 多异常处理

try 语句不仅可以处理某种异常，还可以在复合语句中处理多种异常。

为了演示这一点，创建一个简单的、可调用的 AverageCalculator 类，该类将接收一组输
入，并将他们计算他们的平均值。

```python
class AverageCalculator:

    def __init__(self):
        self.total = 0
        self.sum = 0

    def __call__(self, *values):
        """实现 __call__ 特殊方法，使得类变得可调用，用于计算参数的平均值"""
        if values:
            for value in values:
                self.total += 1
                self.sum += float(value)
        return self.sum / self.total
```

在使用这个 AverageCalculator 类时，有几种可能的异常会出现，但我们更愿意使用用户
界面代码来处理它们，以便显示异常信息。

```python
class AverageCalculator:

    def __init__(self):
        self.total = 0
        self.sum = 0

    def __call__(self, *values):
        """实现 __call__ 特殊方法，使得类变得可调用，用于计算参数的平均值"""
        if values:
            for value in values:
                self.total += 1
                self.sum += float(value)
        return self.sum / self.total

average = AverageCalculator()
values = input("Enter scores, seperated by spaces:\n").split()
try:
    print(f"Average is {average(*values)}.")
# 如果没有输入的值的话，total为空，在计算平均值的时候，分母为空，导致报错ZeroDivisionError
except ZeroDivisionError:
    print("Error: No values provided.")
# 如果输入的不是数值型的字符串，float在进行类型转换的时候会报 ValueError
except (ValueError, UnicodeError):
    print(f"Error: All inputs should be numeric.")
```

在 try 子句的套件中调用 average()，然后在 except 子句中捕获异常。

在 except 子句中处理 ValueError 和（冗余的）UnicodeError 。如果用户尝试输入非数
字内容，就可能出现这两种异常。通过在 except 之后指定一个元组，可以捕获任意异常并
以相同的方式处理它们——本例通过输出一条消息，指出某些输入不是数字。

在现实世界中，可以将 try 语句放在`__call__()`方法内部。虽然这个示例偏离了 Python
的惯用法，但它演示了一条更复杂的 try 语句。

## 8.5 当心 “尿布反模式”

空的 except 子句也会起作用。

```python
try:
    some_scary_funciotn()
except:
    print("An error occurred. Moving on!")
```

在这里，except 子句能够捕获所有的异常。这是 Python 中“极为邪恶”的反模式之一。无
论异常是否在预料之内，其都会被空的 except 子句捕获。

异常的作用是提醒我们，我们的程序现在处于异常状态，这意味着它无法继续沿着预期的正
确路径运行下去，因为会导致意外甚至灾难性的结果。在忽略每个错误之后，我们不知道这
些异常状态是什么，也不知道是是嗯么导致了异常。在抛弃了宝贵的异常信息，并强制程序
继续运行，就像什么都没有发生一样。

记住，一定要明确地捕获特定的异常类型！任何无法预见的异常都可能与需要解决的某些错
误相关。

## 8.6 抛出异常

当代码中存在无法自动恢复的问题时，也可以主动引抛出异常，例如，当调用函数的人传递
一个无法使用的参数时。

我们来写一个函数来演示这一点。

```python
def average(number_string):
    total = 0
    skip = 0
    values = 0
    for n in number_string.split():
        values += 1
        try:
            total += float(n)
        except ValueError:
            skip += 1

    if skip == values:
        raise ValueError("No valid number provided.")
    elif skip:
        print(f"<!> Skiped {skip} invalid values.")

    return total / values
```

抛出异常会导致函数立即退出，就像 return 语句一样。因此，如果没有值（例如当用户传
入一个空字符串时）​，则不需要担心最后的 return 语句是否运行。

用法如下所示：

```python
while True:
    line = input("Enter numbers (space delimated):\n")
    ave = average(line)
    print(ave)
```

我们如果输入的都是非数值的字符串，会导致程序抛出 ValueError("No valid number
proviede.")异常，导致程序崩溃。

我们可以在上层捕捉这个异常，避免内部程序排除的错误导致整个程序崩溃。

```python
while True:
    try:
        line = input("Enter numbers (space delimated):\n")
        ave = average(line)
        print(ave)
    except ValueError:
        print("No valid numbers provided.")
```

当输入错误时，average()函数内部引发的异常在这里被捕获，适当的消息被输出。​（随后
便可以按 Ctrl+C 组合键退出。​）

## 8.7 使用异常

与 Python 中的其他所有对象一样，异常是可以直接使用和提取信息的对象。

这里用一个关于字典的示例展示如何使用异常：

```python
# 定义一个存储朋友名称到邮箱地址的字典
friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com",
}

def look_email(name):
    """通过名称从字典中查找邮箱地址"""
    try:
        return friend_emails[name]
    except KeyError as e:
        print(f"<No entry for friend {e}>")

# 同用户输入获取查找的名称
name = input("Enter name to look up: ")
# 查找邮箱地址
email = look_email(name)
# 打印邮箱地址
print(f"Email: {email}")
```

一种可能的输出：

```bash
Enter name to look up: anne
<No entry for friend 'anne'>
Email: None
```

### 8.7.1 异常和日志

KeyError 的不寻常之处在于，它的消息完全有错误的键组成。通常，软件会将错误记录到
文件或终端，以帮助程序员调试崩溃和错误。

我们接下来编写一个程序来演示这一点：

1. 日志配置

   ```python
   import logging
   from operator import add, sub, mul, truediv
   import sys
   ```

   logging 模块包含 Python 的内置日志记录工具。operator 模块包含用于对任意值执行
   数学运算的优化函数。sys 模块则提供了与解释器本身交互的工具。

   logging.basicConfig()函数允许我们配置日志级别，以及指定要将日志写入哪个文件等
   ：

   ```python
   logging.basicConfig(filename="log.txt", level=logging.INFO)
   ```

   这里有 5 个日志级别：DEBUG、INFO、WARNING、ERROR 和 CRITICAL。通常设置
   level=logging.INFO，可以让 logging 模块记录 INFO 及以上级别（WARNING、ERROR
   和 CRITICAL 级别）的所有日志消息。这意味着只有标记为 DEBUG 的日志消息会被忽略
   。

   通过参数 filename="log.txt"，可以指定日志应该写入一个名为 log.txt 的文件。如
   果想要将日志输出到控制台，可以将参数 filename 设置为空。

   以下是 calculator 函数：

   ```python
   def calculator(a, b, op):
       """进行加减乘除的算数计算"""
       a = float(a)
       b = float(b)
       match op:
           case '+':
               return add(a, b)
           case '-':
               return sub(a, b)
           case '*':
               return mul(a, b)
           case '/':
               return truediv(a, b)
           # 其余未支持的运算符将主动抛出一个 NotImplementedError 的错误
           case _:
               raise NotImplementedError(f"No operator {op}")
   ```

2. 输出异常日志

   接下来演示 calculator() 函数的使用方法，并列出所有的异常处理和日志记录代码。
   我们将按照错误类型进行拆解，分别讨论每一部分。调用 calculator() 函数的代码如
   下：

   ```python
   print("""CALCULATOR
       Use postfix notation
       Ctrl+C or Ctrl+D to quit.""")

   while True:
       try:
           equation = input(" ").split()
           result = calculator(*equation)
           print(result)
   ```

   我们在 while 循环的 try 子句中，尝试从用户哪里收集输入，并将它们传递给
   calculator() 函数。如果成功，就输出结果，循环重新开始。然后，有许多异常可能会
   发生，可在 except 子句中处理它们。代码如下：

   ```python
    except NotImplementedError as e:
        # 如果输入了一个除 + - * / 之外的操作符，将引发 NotImplementedError
        print(f"<!> Invalid operator.")
        logging.info(e)
    except ValueError as e:
        # 当输入非数字的字符，float转换将引发 ValueError
        print(f"<!> Expected format: <A> <B> <OP>")
        logging.info(e)
    except TypeError as e:
        # 如果向函数传递了太多或太少的参数，将引发 TypeError
        print(f"<!> Wrong number of arguments. Use: <A> <B> <OP>.")
        logging.info(e)
    except ZeroDivisionError as e:
        # 如果进行除法运算的第二个参数为0，将引发 ZeroDivisionError
        print(f"<!> Cannot divide by zero.")
        logging.info(e)
   ```

3. 查看并清理日志

   实际上，在生产软件中，永远不要将任何预期的异常写入文件，因为这会导致文件非常
   大且难以处理！因此，建议将所有的日志命令改为 logging.debug()，以 DEBUG 级别记
   录异常信息。这样，如果需要在调试期间浏览异常，只需要将日志配置更改为
   logging.basicConfig(level=logging.DEBUG, filename='log.txt') 即可。可以使用
   INFO 级别进行日志记录，从而规范调试信息。

### 8.7.2 冒泡

前面创建的日志方案中有一个非最优的部分：任何意外的异常都不会被记录。理想情况下，
没有预料到的任何异常都应该记录为 ERROR 级别，但仍然允许程序崩溃，这样代码就不会
试图在未处理的异常状态下继续运行了。

我们可以重新抛出所有已捕获的异常，这一行为在 Python 中被称为冒泡。由于异常在重新
抛出后没有再次被捕获，因此程序会崩溃。

我们可以保持前面添加的 try 子句不变，但在最后添加一个 except 子句。修改如下：

```python
    except Exception as e:
        logging.exception(e)
        raise
```

except 子句是按顺序执行的，这就是为什么这个新的 except 子句必须出现在当前 try 子
句的末尾。

可以使用特殊方法 logging.exception(e) 来记录错误消息和异常信息，级别为 ERROR。当
用户发送带有错误报告的日志文件时，开发者需要使用这些异常信息来查找和修复 bug。

raise 子句用于将错误重新抛出，同时也会抛出最后捕捉的异常。（也可以使用
`raise e`，但是在这种情况下，为了是代码和异常信息简介，建议使用简单的 raise。）
在这里冒泡错误是绝对必要的，否则浙江称为尿布反模式的一个例子。

### 8.7.3 异常链

当捕获一个异常后抛出另一个异常时，有可能丢失原始错误的上下文。为了避免出现这种情
况，Python 提供了异常链。通过这种方式，我们可以排除一个新的异常，而不会丢失已经
捕获的所有有用信息。这是在 Python3.0 中引入的。

下面来演示这个概念。我们编写一个程序用于查找著名地标所在的城市和州。首先定义字典
：

```python
# 定义地标字典
landmarks = {
    "Yellow Crane Tower": "Wuhan Hubei",              # 黄鹤楼
    "The Bund": "Shanghai Shanghai",                 # 外滩
    "Terracotta Army": "Xi'an Shaanxi",              # 秦始皇兵马俑
    "Great Wall": "Beijing Beijing",                 # 万里长城（北京段最有代表性）
    "Forbidden City": "Beijing Beijing",             # 故宫
    "Temple of Heaven": "Beijing Beijing",           # 天坛
    "Summer Palace": "Beijing Beijing",              # 颐和园
    "West Lake": "Hangzhou Zhejiang",                # 西湖
    "Potala Palace": "Lhasa Tibet",                  # 布达拉宫
    "Mogao Caves": "Dunhuang Gansu",                 # 莫高窟
}
```

定义函数用于在字典中查找地标及对应的城市。

```python
def lookup_landmark(landmark):
    try:
        location = landmarks[landmark]
        city, province = location.split()
    except KeyError as e:
        raise KeyError("Landmark not found.") from e
    print(f"{landmark} is in {city}, {province}")
```

在这个函数中，尝试在 landmarks 字典中查找地标。如果没有找到，就引发 KeyError，并
捕获这个异常，然后重新抛出更有用的异常信息。当抛出新的异常时，使用 `from e` 来指
定这个异常 e 是由捕获的异常引起的。这确保了异常信息会显示导致错误的原因：没有找
到城市或地标。

下面演示这个函数的用法：

```python
lookup_landmark('Yellow Crane Tower')
lookup_landmark('Mount Tai') # 查找 泰山
lookup_landmark('Li River') # 查找 漓江
```

以下是执行输出结果：

```bash
Yellow Crane Tower is in Wuhan, Hubei
Traceback (most recent call last):
  File "F:\my-python-journey\programing\dead-simple-python\chapter-08\demos\landmarks.py", line 18, in lookup_landmark
    location = landmarks[landmark]
               ~~~~~~~~~^^^^^^^^^^
KeyError: 'Mount Tai'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "F:\my-python-journey\programing\dead-simple-python\chapter-08\demos\landmarks.py", line 25, in <module>
    lookup_landmark('Mount Tai') # 查找 泰山
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "F:\my-python-journey\programing\dead-simple-python\chapter-08\demos\landmarks.py", line 21, in lookup_landmark
    raise KeyError("Landmark not found.") from e
KeyError: 'Landmark not found.'
```

这个异常信息的上方是一个通知，用于说明这个异常是由另一个异常引起的。

在更上层的异常中，我们找到了问题所在：Python 在 landmarks 字典中找不到 Mount Tai
这个地标。

即便没有添加 `raise KeyError from e`，Python 也会包含上下文，这两个异常信息之间
会有一条更加晦涩且不太有用的消息：

```bash
During handling of the above exception, another exception occurred:
```

可以使用 `raise e from None` 显示地禁用异常链。

## 8.8 else 和 finally

到目前为止，所有的异常处理示例都依赖于 try 语句和 except 子句，这使得代码的其余
部分在任何情况下都可以运行，除非调用 return 语句或利用 raise 语句的终端行为来退
出函数。

try 语句还有两个可选的子句：else 子句在没有异常时运行；finally 子句在任何情况下
都会运行，但是运行方式有些令人惊讶。

### 8.8.1 else: 如果所有功能能正常运行

我们应该使用 else 子句来处理那些只有在没有 except 子句捕获任何异常时才运行的代码
段。

```python
import math

def average_string(number_string):
    try:
        numbers = [float(n) for n in number_string.split()]
    except ValueError:
        total = math.nan
        values = 1
    else:
        total = sum(numbers)
        values = len(numbers)

    # 使用 try 子句处理 values 为 0 的情况
    try:
        average = total / values
    except ZeroDivisionError:
        average = math.inf

    return average

while True:
    number_string = input("Enter space-delimited list of numbers:\n ")
    print(average_string(number_string))
```

### 8.8.2 finally：在所有语句之后

不管怎样，finally 子句总是会运行！这一点没有任何例外：及时是 raise 或 return 也
不能阻止 finally 子句的运行。这就是 finally 子句与 try 语句后面的普通代码的区别
所在。

因为这一点，finally 子句特别适用于编写不管怎样都需要运行的清理代码。

这里有一个函数，它从文件中读取数字，每行一个数字，并计算平均值。在这种情况下，如
果文件包含非数字数据或找不到文件，最后引发异常。

在这个例子中，手动打开和关闭文件，在生产环境中，也可以使用上下文管理器来代替：

```python
# 从文件夹中读取数据并计算平均值，演示 finally 子句

def average_file(path):
    file = open(path, 'r')

    try:
        numbers = [float(n) for n in file.readlines()]
    # except FileNotFoundError:
    except ValueError as e:
        # 防止文件中存在非数值类型的字符
        raise ValueError("File contains non-numberic values.") from e
    else:
        try:
            return sum(numbers) / len(numbers)
        except ZeroDivisionError as e:
            # 防止文件为空，导致分母为0
            raise ValueError("Empty file.") from e
    finally:
        print("Closing file.")
        file.close()

# print(average_file('numbers_good.txt'))
# print(average_file('numbers_bad.txt'))
# print(average_file('numbers_empty.txt'))
print(average_file('nonexistent.txt'))
```

我们依次执行测试，发现 `print(average_file('nonexistent.txt'))` 不会打印
`Closing File.`。因为这个异常来自 `file.open()` 调用，该调用发生在 try 子句之前
。finally 子句只有在它连接的 try 子句被执行时才会运行，由于控制流从未到达 try 子
句，因此 finally 子句从未被调用。这样也没问题，因为没有必要尝试关闭一个从未打开
的文件。

## 8.9 创建异常

Python 拥有相当对的异常。具体可以查询官方文档。

所有的错误类型的异常类都继承自 Exception 类，而 Exception 类又继承自
BaseException 类。这种双重继承关系的存在是为了让我们可以捕获所有的错误异常，而不
会同时对不是错误的特殊异常做出反应，比如 KeyboardInterrupt，它继承自
BaseException 类而不是 Exception 类。

自定义异常类可以继承我们喜欢的任何异常类，但应避免继承 BaseException 类，因为这
个类不是为自定义异常类而设计的。有时候，最好继承与我们正在创建的异常类最接近的异
常类。然而，如果不知道该继承哪个类，可以集成 Exception 类。

大多数时候，只有在复杂的项目中才需要自定义异常，一般不需要我们自定义异常类。

## 8.10 异常一览

下面加药介绍常见的异常类。有 4 个基类，所有其他异常类都继承自这 4 个基类。当我们
需要捕获所有异常类别时，通常可以使用这 4 个基类。

- BaseException: 是所有异常类的基类。不要直接继承自这个类，因为根据设计它不应该
  被这样使用。
- Exception: 是所有错误类型异常的基类。
- ArithmeticError: 是与算术相关的错误类型异常的基类。
- LookupError: 是与在集合中查找值相关的任何错误类型异常的基类。

> 还有一个 BufferError: 与 Python 背后的内存错误有关。但是没有其他异常从这个异常
> 继承，我们也不应该继承这个类。

## 8.11 小结

本章讲解了如何以及何时使用异常和错误处理。语法本身归结为
try、except、else、finally 和 raise 语句的结构。
