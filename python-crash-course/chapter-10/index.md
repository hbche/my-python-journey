# 第 10 章 文件和异常

## 10.1 读取文件

要使用文本文件中的信息，首先需要将信息读取到内存中。既可以一次性读取文件的全部内
容，也可以逐行读取。

### 10.1.1 读取文件的全部内容

要使用文件的内容，需要将其路径告知 Python。路径(path)指的是文件或文件夹在系统中
的准确位置。Python 提供了 pathlib 模块，让我们能够更轻松地在各种操作系统中处理文
件和目录。提供特定功能的模块通常称为库(library)。

```python
from pathlib import Path

# 创建了一个表示文件pi_digits.txt的Path对象
path = Path('pi_digits.txt')
# 读取文件的全部内容
contents = path.read_text()
print(contents)
```

### 10.1.2 相对路径和绝对路径

根据我们组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。要让 Python
打开不与程序文件位于同一个目录中的文件，需要提供正确的路径。

在编程中，指定路径的方式有两种。首先，相对文件路径让 Python 到相对于当前运行的程
序所在目录的指定位置去查找。

其次，可以将文件在计算机中的准确位置告诉 Python，这样就不用管当前运行的程序存储
在什么地方了。这称为绝对文件路径。在相对路径行不通时，可使用绝对路径。

使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法是，要么将数据
文件存储在程序文件所在的目录中，要么将其存储在程序文件所在目录下的一个文件夹（如
text_files）中。

> 注意：在显示文件路径时，Windows 系统使用反斜杠(\\)而不是斜杠(/)。但是我们在代
> 码中应该始终使用斜杠，即便在 Windows 系统中也是如此。在与我们或其他用户的系统
> 交互时，pathlib 库会自动使用正确的路径表示方法。

### 10.1.3 访问文件中的各行

在使用文件时，经常需要检查其中的每一行：可能要在文件中查找特定的信息，或者以某种
方式修改文件中的文本。

我们可以使用 splitlines()方法将冗长的字符串转换为一系列行，再使用 for 循环以每次
一行的方式检查文件中的各行：

```python
from pathlib import Path

# 创建了一个表示文件pi_digits.txt的Path对象
path = Path('pi_digits.txt')
# 读取文件的全部内容
contents = path.read_text().rstrip()

# 将内容拆解成行，遍历输出
lines = contents.splitlines()
for line in lines:
    print(line)
```

### 10.1.4 使用文件的内容

将文件的内容读取到内存中后，就能以任意方式使用这些数据了。下面以简单的方式使用圆
周率的值。

```python
from pathlib import Path

path = Path('pi_digits.txt')
# 读取文件的内容
contents = path.read_text()
# 将读取的内容拆分长行列表
lines = contents.splitlines()

# 保存pi的值
pi_string = ''
# 遍历pi的内容，记录每行pi的值
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

> 注意：在读取文本文件时，Python 将其中的所有文本都解释为字符串。如果读取的是数
> ，并且要将其作为数值使用，就必须使用 int()函数将其转换为整数，或者使用 float()
> 函数将其转换为浮点数。

#### 10.1.5 包含 100 万位的大型文件

在可处理的数据量方面，Python 没有任何限制。只要系统的内存足够大，我们想处理多少
数据就可以处理多少数据。

### 10.1.6 圆周率中包含你的生日吗

我们可以检查圆周率中是否包含我们的生日：

```python
from pathlib import Path

path = Path('pi_million_digits.txt')
lines = path.read_text().strip().splitlines()

pi_string = ''
for line in lines:
    pi_string += line

birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")
```

## 10.2 写入文件

保存数据的最简单的方式之一是将其写入文件。通过将输出写入文件，即便关闭包含程序输
出的终端窗口，这些输出也依然存在：既可以在程序结束运行后查看这些输出，也可以与他
人共享输出文件，还可以编写程序来将这些输出读取到内存中并进行处理。

### 10.2.1 写入一行

定义一个文件的路径后，就可使用 write_text()将数据写入该文件了。

```python
# 写入文件
from pathlib import Path

# 生成写入文件的路径
path = Path('programing.txt')
# 向文件中写入内容，接收可选的encoding参数指定写入的编码
path.write_text("I love programing.")
# 会覆盖之前写入的内容
path.write_text("我热爱编程。", encoding='utf8')
```

> 注意：Python 只能将字符串写入文本文件。如果要将数值数据存储到文本文件中，必须
> 先使用函数 str()将其转换为字符串格式。

### 10.2.2 写入多行

write_text()方法会在幕后完成几项工作。首先，如果 path 变量对应的路径指向的文件不
存在，就创建它。其次，将字符串写入文件后，它会确保文件得以妥善地关闭。如果没有妥
善地关闭文件，可能会导致数据丢失或受损。

要将多行写入文件，需要先创建一个字符串（其中包含要写入文件的全部内容）​，再调用
write_text()并将这个字符串传递给它。

```python
# 写入多行数据
from pathlib import Path

# 生成写入文件的路径
path = Path('programing.txt')
# 创建变量记录写入的多行数据
contents = 'I love programing.'
contents += '\n我热爱编程。'

# 以指定编码向文件中写入内容
path.write_text(contents, encoding='utf8')
```

> 注意：在对 path 对象调用 write_text()方法时，务必谨慎。如果指定的文件已存在
> ，write_text()将删除其内容，并将指定的内容写入其中。

## 10.3 异常

Python 使用称为异常(exception)的特殊对象来管理程序执行期间发生的错误。每当发生让
Python 不知所措的错误时，它都会创建一个异常对象。如果我们编写了处理该异常的代码
，程序将继续运行；如果我们未对异常进行处理，程序将停止，并显示一个 traceback，其
中包含有关异常的报告。

异常是使用 try-except 代码块处理的。try-except 代码块让 Python 执行指定的操作，
同时告诉 Python 在发生异常时应该怎么办。在使用 try-except 代码块时，即便出现异常
，程序也将继续运行：显示我们编写的友好的错误消息，而不是令用户迷惑的 traceback。

### 10.3.1 处理 ZeroDivisionError 异常

```python
print(5/0)
# Traceback (most recent call last):
#   File "\my-python-journey\python-crash-course\chapter-10\division_calculator.py", line 1, in <module>
#     print(5/0)
#           ~^~
# ZeroDivisionError: division by zero
```

### 10.3.2 使用 try-except 代码块

当我们认为可能发生错误时，可编写一个 try-except 代码块来处理可能引发的异常。我们
让 Python 尝试运行特定的代码，并告诉它如果这些代码引发了指定的异常，该怎么办。

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

再次运行，我们发现此时输出的是我们在 except 中写的逻辑。

如果 try-except 代码块后面还有其他代码，程序将继续运行，因为 Python 已经知道了如
何处理错误。

### 10.3.3 使用异常避免崩溃

如果在错误发生时，程序还有工作没有完成，妥善地处理错误就显得尤其重要。这种情况经
常出现在要求用户提供输入的程序中。如果程序能够妥善地处理无效输入，就能提示用户提
供有效输入，而不至于崩溃。

```python
print("Give me two numbers, adn I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("SecondNumber: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

这个程序没有采取任何处理错误的措施，因此在执行除数为 0 的除法运算时，它将崩溃。

### 10.3.4 else 代码块

通过将可能引发错误的代码放在 try-except 代码块中，可提高程序抵御错误的能力。因为
错误是执行除法运算的代码行导致的，所以需要将它放到 try-except 代码块中。这个示例
还包含一个 else 代码块，只有 try 代码块成功执行才需要继续执行的代码，都应放到
else 代码块中：

```python
print("Give me two numbers, adn I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("SecondNumber: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        # 只要try成功执行，没有出发except，else就会执行
        print(answer)
```

except 代码块告诉 Python，在出现 ZeroDivisionError 异常时该怎么办 ​。如果 try 代
码块因零除错误而失败，就打印一条友好的消息，告诉用户如何避免这种错误。程序会继续
运行，不会崩溃，并且用户也看不到 traceback。

只有可能引发异常的代码才需要放在 try 语句中。有时候，有一些仅在 try 代码块成功执
行时才需要运行的代码，这些代码应放在 else 代码块中。except 代码块告诉 Python，如
果在尝试运行 try 代码块中的代码时引发了指定的异常该怎么办。

### 10.3.5 处理 FileNotFoundError 异常

在使用文件时，一种常见的问题是找不到文件：要查找的文件可能在其他地方，文件名可能
不正确，或者这个文件根本就不存在。对于所有这些情况，都可使用 try-except 代码块来
处理。

```python
from pathlib import Path

path = Path('aliens.txt')
# 读取一个不存在的文件将触发Python的FileNotFoundError
contents = path.read_text(encoding='utf-8')         # FileNotFoundError: [Errno 2] No such file or directory: 'aliens.txt'
```

对文件读取部分的代码使用 try-except 代码块捕获异常处理：

```python
# 使用 try-except代码块捕获异常
from pathlib import Path

path = Path('aliens.txt')
# 读取一个不存在的文件将触发Python的FileNotFoundError
try:
    contents = path.read_text(encoding='utf-8')         # Sorry, the file aliens.txt does not exist.
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    print(contents)
```

### 10.3.6 分析文本

我们从古登堡计划中下载 《爱丽丝漫游奇境记》的 txt 格式，并编写程序分析这个文本文
件。

```python
from pathlib import Path

path = Path('alice.txt')

try:
    contents = path.read_text(encoding='utf8')
except FileNotFoundError:
    print(f"Sorry, the file {path} dose not exist.")
else:
    # 统计文件中大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")      # The file alice.txt has about 29564 words.
```

### 10.3.7 使用多个文件

编写程序统计多个文学作品的字数。

```python
from pathlib import Path

def count_words(file):
    """统计file对应的文件的字数"""

    path = Path(file)
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} dosen't exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")

bookds = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']
for book in bookds:
    count_words(book)

# The file alice.txt has 29564 words.
# The file little_women.txt has 24711 words.
# The file moby_dick.txt has 215838 words.
# The file siddhartha.txt has 42186 words.
```

### 10.3.8 静默失败

在上一个示例中，我们告诉用户有一个文件找不到。但并非每次捕获异常都需要告诉用户，
我们有时候希望程序在发生异常时保持静默，就像什么都没有发生一样继续运行。要让程序
静默失败，可像通常那样编写 try 代码块，但在 except 代码块中明确地告诉 Python 什
么都不要做。Python 有一个 pass 语句，可在代码块中使用它来让 Python 什么都不做

```python
from pathlib import Path

def count_words(file):
    """统计file对应的文件的字数"""

    path = Path(file)
    try:
        contents = path.read_text(encoding='utf8')
    except FileNotFoundError:
        # print(f"Sorry, the file {path} dosen't exist.")
        # 静默失败
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has {num_words} words.")

bookds = ['alice.txt', 'little_women.txt', 'moby _dick.txt', 'siddhartha.txt']
for book in bookds:
    count_words(book)

# The file alice.txt has 29564 words.
# The file little_women.txt has 24711 words.
# The file siddhartha.txt has 42186 words.
```

相比于上一个程序，这个程序唯一的不同之处是，except 代码块包含一条 pass 语句。现
在，当出现 FileNotFoundError 异常时，虽然仍将执行 except 代码块中的代码，但什么
都不会发生。当这种错误发生时，既不会出现 traceback，也没有任何输出。用户将看到存
在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到

pass 语句还充当了占位符，提醒我们在程序的某个地方什么都没有做，而且以后也许要在
这里做些什么。

### 10.3.9 决定报告哪些错误

该在什么情况下向用户报告错误？又该在什么情况下静默失败呢？如果用户知道要分析哪些
文件，他们可能希望在有文件未被分析时出现一条消息来告知原因。如果用户只想看到结果
，并不知道要分析哪些文件，可能就无须在有些文件不存在时告知他们。向用户显示他们不
想看到的信息可能会降低程序的可用性。Python 的错误处理结构让我们能够细致地控制与
用户共享错误信息的程度，要共享多少信息由我们决定。

编写得很好且经过恰当测试的代码不容易出现内部错误，如语法错误和逻辑错误，但只要程
序依赖于外部因素，如用户输入、是否存在指定的文件、是否有网络连接，就有可能出现异
常。凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多
少相关的信息。

## 10.4 存储数据

很多程序要求用户输入某种信息，比如让用户存储游戏首选项或提供要可视化的数据。不管
专注点是什么，程序都会把用户提供的信息存储在列表和字典等数据结构中。当用户关闭程
序时，几乎总是要保存他们提供的信息。一种简单的方式是使用模块 json 来存储数据。

模块 json 让我们能够将简单的 Python 数据结构转换为 JSON 格式的字符串，并在程序再
次运行时从文件中加载数据。我们还可以使用 json 在 Python 程序之间共享数据。更重要
的是，JSON 数据格式并不是 Python 专用的，这让我们能够将以 JSON 格式存储的数据与
使用其他编程语言的人共享。这是一种轻量级数据格式，不仅很有用，也易于学习。

### 10.4.1 使用 json.dumps() 和 json.loads()

json.dumps()函数接受一个实参，即要转换为 JSON 格式的数据。这个函数返回一个 JSON
格式的字符串，这样我们就可将其写入数据文件了。

```python
import json
from pathlib import Path

numbers = [1, 3, 5, 7, 9]
# 调用json.dumps转储内容，转换成json格式的字符串
contents = json.dumps(numbers)
path = Path('numbers.json')
# 将json字符串写入文件
path.write_text(contents)
```

json.loads()这个函数将一个 JSON 格式的字符串作为参数，并返回一个 Python 对象（这
里是一个列表）。

```python
from pathlib import Path
import json

path = Path('numbers.json')
# 将文件内容读到内存中
contents = path.read_text()
# 将内存中的数据转换成python的数据结构
numbers = json.loads(contents)
print(numbers)
```

### 10.4.2 保存和读取用户生成的数据

使用 json 保存用户生成的数据很有必要，因为如果不以某种方式进行存储，用户的信息就
会在程序停止运行时丢失。

```python
from pathlib import Path
import json

def greet_user():
    """
    问候用户，并指出其名字
    """
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

### 10.4.3 重构

我们经常会遇到这样的情况：虽然代码能够正确地运行，但还可以将其换分为一系列完成具体工作的函数来进行改进。这样的过程成为**重构**。重构让代码更清晰、更易于理解、更易于扩展。


``` python
from pathlib import Path
import json

def get_stored_username():
    """
    如果存储了用户名，就获取它
    """
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def greet_user():
    """
    问候用户，并指出其名字
    """
    path = Path('username.json')
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

## 10.5 小结

1. 读取文件
2. 写入文件
3. 解析json文件
4. 存储为json文件
5. 文件相关的异常处理
6. 文件统计