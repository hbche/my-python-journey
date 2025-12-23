# 第 11 章 文本输入\输出和上下文管理

基于文本文件存储数据是最常见的数据存储方法，也是在程序运行之间保持状态的关键。

本章将分解与文本文件协作相关的两个核心组件：流和类路径对象。本章还将介绍各种打开
、阅读和写入文件的方式，以及如何使用文件系统，最后对常见的文件格式进行简要介绍。

## 11.1 标准输入和输出

### 11.1.1 重温 print()

print()函数接收一个赐福穿参数并将其输出到屏幕上。这很简单，但是 print()的功能并
不仅限于此。还可以使用 print()以多种方式快速灵活地输出多个值，甚至可以用它来写入
文件。

#### 1. 标准流

要想充分理解 print()的潜力，就必须理解流。当使用 print()时，你将字符串发送到标准
输出流，这是操作系统提供的一种特殊通信通道。标准输出流的行为就像一个队列：我们将
数据推送到流中，这些字符串就可以按顺序被其他程序或进程拾取。默认情况下，操作系统
将提供给 print()的所有字符串都发送到标准输出流。

操作系统还有一个标准错误流来显示错误消息。正常输出被发送到标准输出流，与错误相关
的输出则被发送到标准错误流。

```py
print("Normal message")
print("Scary error occurred")
```

假设用户想使用终端将所有程序的输出通过管道传输到文件中，使正常输出保存到一个文件
中，而使错误输出保存到另一个文件中。下面是 bash 中的示例：

```bash
python print_error.py > output.txt 2> error.txt
```

用户希望 output.txt 包含正常信息，而希望 error.txt 包含发生的可怕错误。但是因为
print()默认将消息发送到标准输出流，所以两种消息都被输出到 output.txt 中，而
error.txr 完全是空的。

要想将错误消息发送到错误流，就必须通过在 print()上使用 file 参数加以指定，如下所
示：

```py
import sys

print("Normal message")
print("Scary error occurred", file=sys.stderr)
```

首先导入 sys 模块，这样才能范文 sys.stderr，这就是标准错误流的句柄。通过在第二次
print()调用中指定参数 file=sys.stderr，即可将错误消息发送到表尊错误流。正常消息
仍被发送到标准输出流，因为默认参数是 file=sys.stdout。

复用之前的 shell 会话，用法一样，可以看到两种输出现在已被发送到预期的文件中。

正如参数名称 file 所暗示的那样，print()函数并不限于标准流。事实上，我们马上就会
看到它非常适用于将文本写入文件。

#### 2. 刷新

我们需要知道一个重要事实，标准流是作为缓冲区实现的：数据可以推送到缓冲区，其行为
类似于队列。数据将在那里等待，直至被终端或任何想要显示其内容的进程拾取。

通常最好让系统决定何时刷新标准流，而不是强制执行刷新。但是在某些情况下，我们可能
想要强制执行刷新。例如，我们可能想在已显示的行的末尾追加一些内容。

下面是个简单的进度指示器，它可以做到这一点。我们将使用 time.sleep()来指示正在运
行一些耗时的进程，例如下载。

```py
import time

print("Downloading", end="")
for n in range(20):
    print(".", end="", flush=True)
    time.sleep(0.1)
print("\nDownload completed!")
```

print()函数的 end 参数可以防止输出新行。该示例的重要部分是 flush 参数，如果忽略
它，那么在循环结束之前，用户将看不到任何东西，因为缓冲区在输出到终端之前会等待换
行符。但是通过强制刷新缓冲区，输出到终端的行会在每次循环迭代时更新。

#### 3. 输出多个值

print()函数可以接收多个数量的有序参数，每个参数都将使用 `__str__()`特殊方法转换
为字符串。这是一种与 f- 字符串格式化相比更加快速且简便的替代方法。

```py
number = 245
street = '8th Street'
city = 'San Francisco'
state = 'CA'
zip_code = 94103

print(f"{number} {street} {city} {street} {state} {zip_code}")
```

虽然这样是可行的，但是也可以在不使用 f-字符串的情况下完成这一任务，从而简化
print()语句：

```py
print(number, street, city, street, state, zip_code)
```

print()语句会将每个参数转换为一个字符串，然后将各部分连接在一起，每两部分之间有
一个空格（默认情况下）。在任何一种情况下，输出都是相同的：

```shell
245 8th Street San Francisco 8th Street CA 94103
```

我们也可以从字典中快速生成地址对应的房产价值表，如下所示：

```py
nearby_properties = {
    "N. Anywhere Ave.": {
        123: 156_852,
        124: 157_923,
        126: 163_812,
        127: 144_121,
        128: 166_356,
    },
    "N. Everywhere St.": {
        4567: 175_753,
        4568: 166_212,
        4569: 185_123,
    }
}
```

我们想输出一个表格，其中包含街道、号码和格式化的房产价值，每两列之间使用制表符
(\t)分隔。下面首先使用 f-字符串：

```py
for street, properties in nearby_properties.items():
    for address, value in properties.items():
        print(f"{street}\t{address}\t${value:,}")
```

f-字符串增加了不必要的复杂性。因为用制表符分隔每一列，所以可以再次利用 print()更
好地完成这一任务，如下所示：

```py
for street, properties in nearby_properties.items():
    for address, value in properties.items():
        print(street, address, f"${value:,}", sep="\t")
```

sep 参数允许我们定义每两个值之间使用什么字符作为分隔符。sep 默认是一个空格，如上
述示例所示，使用制表符(\t)作为分隔符。

这种方案更具可读性，另外，如果要用空格和竖线字符分隔列，只需修改 sep 参数即可：

```py
for street, properties in nearby_properties.items():
    for address, value in properties.items():
        print(street, address, f"${value:,}", sep="  |  ")
```

如果使用了 f-字符串，则需要更改分离时的字符。

print()函数还有一个 end 函数，用来指定要附加到输出末尾的内容。默认情况下，这是一
个换行符(\n)，但是也可以像修改 sep 参数一样修改它。

一种常见的方法是设置 end="\t"，这将导致输出的下一行覆盖上一行。这在状态更新中特
别有用，例如进行进度提醒。

### 11.1.2 重温 input()

input()函数允许我们从终端（标准输入流）接收用户输入。和 print()函数不同，input()
函数没有额外的功能。

input()接收的唯一参数是 promp，这是一个可选字符串，输出到标准输出时不追加尾随换
行符(\n)。传递给 prompt 的值通常是一条消息，用于通知用户应该输入什么。该参数可以
是任何通过 `__str__()`方法转换为字符串的对象，和传递给 print()的有序参数相同。

## 11.2 流

要想处理任何数据文件，我们需要获得一个流（又称文件对象或类文件对象），其提供读取
和写入内存中的特定文件的方法。一般存在两种流：二进制流是所有流的基础，用来处理二
进制数据（0 和 1）；文本流则处理二进制文件的编码和解码。

普通的.txt 文件、Word 文档或我们拥有的任何其他文件都可以使用流来处理。我们已经使
用过标准输出(sys.stdout)、标准输入(sys.stdin)和标准错误(sys.stderr)的对象实际上
都是流。

可以使用内置的 open()函数来创建处理文件的流。这个函数的使用有很多需要注意的地方
，下面我们从它最简单的用法开始。

假定每个文件都和打开它的 Python 模块位于同一目录中。如果文件在计算机上的其他地方
，则需要一个路径，路径稍后将详细探讨。

要想读取名为 213AnywhereAve.txt 的文件，需要创建一个流。Python 在后台完美地创建
了文件流，所以只需要使用 open()函数，如下所示：

```py
house = open('213AnywhereAve.txt')
print(house.read())
house.close()
```

open()函数返回一个流对象 —— 具体来说，返回的是一个 TextIOWrapper 对象，用于处理
213AnywhereAve.txt 文件的内容。将这个流对象绑定到 house。

接下来，通过调用 house 的 read()方法将返回的字符串直接传递给 print()来输出读取到
的全部内容。

一旦完成了对文件的处理，就必须关闭这个流，以上代码的最后一行正式这么做的。重要的
是不要让垃圾回收器来关闭文件，因为这既不能保证有效，也不能在所有 Python 实现中确
保可移植。更重要的是，在写入文件时，直至调用 close()，Python 才能保证完成对文件
的变更。这意味着如果忘记在程序结束前调用 close()，所做的更改可能会部分或全部丢失
。

## 11.3 上下文管理器基础

上下文管理器是一种对象，当程序执行留下一段代码或上下文时，它能自动处理自己的清理
任务。此处的上下文由带有描述的 Python 代码提供。后续还会详细介绍上下文管理器的原
理和详细实现。

实际上在打开文件后，可以尝试执行更多的操作，而非仅仅输出文件内容。我们可能以多种
方式处理数据，比如将其存储到集合中，或者搜索特殊内容。出现错误和异常的可能性很大
。使用这种方法，如果成功打开文件，但是在阅读或使用文件时发生意外，那么 close()方
法将永远不会被调用。

为了解决这个问题，可以在一个 try 语句的 finally 子句中调用 close()，如下所示：

```py
house = open('213AnywhereAve.txt')
try:
    print(house.read())
finally:
    house.close()
```

如果 213AnywehereAve.txt 文件不存在，则出发 FileNotFoundError。如果能成功打开这
个文件，就可以尝试从 house 流中执行 read()。由于没有观察到任何意外，因此代码会自
动从这个 try 语句中穿过。又因为 close()调用在 finally 子句中，所以无论是否有错误
，它都将被调用。

但在实践中，应时刻记住调用 close()是完全不现实的，而且是一种痛苦。如果忘记了关闭
流，抑或程序在我们调用 close()之前终止了，则可能导致各种错误。

好在所有流对象都有上下文管理器，因此可以通过 with 语句完成自身清理。将这个
try-finally 语句封装到一行代码中，如下所示：

```py
with open('213AnywhereAve.txt') as house:
    print(house.read())
```

这同样可以打开 213AnywhereAve.txt 文件，将流绑定到 house，然后读取并输出文件中的
代码行。无须手动调用 house.close()，因为 Python 在后台能自动执行这条语句。

## 11.4 文件模式

open()函数可选地接收第二个参数 mode。该参数应为一个字符串，指示文件应该如何打开
，且定义了可以对流对象执行什么操作，如读取、写入等。如果没有传递 mode 参数
，Python 将使用 mode='r'，即以只读方式打开文件。

基于文本的文件有 8 种不同的文件模式，每种模式的行为都略有不同。基本模式如下：

- r: 打开文件进行读取
- w：打开文件进行写入，但首先需要截断（擦除）文件原有内容
- a：打开文件进行追加写入，即写入现有文件的末尾。
- x：创建一个文件并打开它进行写入

添加加号(+)标志能追加读取或写入，以模式中缺少的那个为准。其中最重要的用法是模式
r+，它允许我们在不擦除文件原有内容的情况下读取或写入文件。

| 功能           | r   | r+  | w   | w+  | a   | a+  | x   | x+  |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 允许去读       | √   | √   |     | √   |     | √   |     | √   |
| 允许写入       |     | √   | √   | √   | √   | √   | √   | √   |
| 可创建新文件   |     |     | √   | √   | √   | √   | √   | √   |
| 可打开现有文件 | √   | √   | √   | √   | √   | √   |     |     |
| 先擦除文件内容 |     |     | √   | √   |     |     |     |     |
| 允许搜索       | √   | √   | √   | √   |     | √\* | √   | √   |
| 初始位置在开头 | √   | √   | √   | √   |     |     | √   | √   |
| 初始位置在结尾 |     |     |     |     | √   | √   |     |     |

√\*只允许读搜索

在流中，位置指示在文件中读取和写入的位置。如果模式支持，seek()方法允许更改此位置
。默认情况下，此位置在文件的开头或结尾。

还可以使用 mode 参数在默认的文本模式(t)和二进制模式(b)之间切换。但是现在，我们至
少要先明白使用哪种模式打开了文件。例如，mode='r+t'以读写文本模式打开文件，和
mode='r+'等效；而 mode='r+b'以读写二进制模式打开文件。

当使用读取模式(r 或 r+)打开文件时，文件必须已经存在。如果不存在，open()函数将引
发 FileNotFoundError。

创建模式(x 或 x+)恰恰相反，要求文件必须事先不存在。如果事先存在，open()函数将引
发 FileExistError。

写入模式(w 或 w+)和追加模式(a 或 a+)都没有这些问题。如果文件存在就打开，如果不存
在就创建。如果尝试写入仅为读取而打开的流(r)或从仅为写入而打开的流(w、a 或是 x)中
读取，则读取或写入操作将引发 io.UnsupportedOperation 错误。

如果想要体检检查流支持哪些操作，请在流上使用 readable()、writeable()或 eekable()
方法，如下所示：

```py
with open('213AnywhereAve.txt', 'r') as file:
    print(file.readable())      # print 'True'
    print(file.writable())      # print 'False'
    print(file.seekable())      # print 'True'
```

## 11.5 读取文件

要从文件中读取，首先需要获得一个流，并以可读模式(r、r+、w+、a+或 x+)打开这个流。
然后就可以通过如下 4 种方式之一进行查阅：read()、readline()、readlines()或迭代。

先准备后续使用读取方法读取的文件 78SomewhereRd.txt：

```txt
78 Somewhere Road, Anytown PA
Tiny 2-bed, 1-bath bungalow. Needs repairs.
Built in 1981; original kitchen and appliances.
Small backyard with old storage shed.
Built on ancient burial ground.
$431,998

```

### 11.5.1 read()方法

可以使用 read()方法读取 78SomewhereRd.txt 文件:

```py
with open('78SomewhereRd.txt', 'r') as house:
    contents = house.read()
    print(type(contents))
    print(contents)
```

默认情况下，read()将读取字符，直至到达文件末尾。可以使用 size 参数更改此行为，该
参数用于指定读取的最大字符数。例如，要从文件中读取最多 20 个字符（如果先到达文件
末尾，则读取的字符更少），如下所示：

```py
with open('78SomewhereRd.txt', 'r') as house:
    print(repr(house.read(20)))
```

### 11.5.2 readline()方法

readline()方法的行为和 read()基本相同，不同之处在于 readline()只读取到换行符，而
不是读取到文件末尾。可以用这个方法来读取文件的前两行。和以前一样，使用 repr()显
示原始字符串，如下所示：

```py
with open('78SomewhereRd.txt', 'r') as house:
    line1 = house.readline()
    line2 = house.readline()
    print(repr(line1))  # '78 Somewhere Road, Anytown PA\n'
    print(repr(line2))  # 'Tiny 2-bed, 1-bath bungalow. Needs repairs.\n'
```

house 流能记住在文件中的位置。因此，每次调用 readline()后，流的位置都被设置为下
一行的开头。运行上述代码后系那个输出我呢间的前两行，将其作为原始字符串输出，就能
看到换行符的字面量。

readline()方法还有一个 size 参数，size 是“最多读取的字符数上限”，而不是“读取多少
行”。

```py
with open('78SomewhereRd.txt', 'r') as house:
    print(repr(house.readline(2)))  # '78'
    print(repr(house.readline(2)))  # ' S'
    print(repr(house.readline(100)))    # 'omewhere Road, Anytown PA\n'
    print(repr(house.readline(2)))  # 'Ti'
    print(repr(house.readline(2)))  # 'ny'
    print(repr(house.readline()))   # ' 2-bed, 1-bath bungalow. Needs repairs.\n'
```

readline 会基础每次调用之后的位置，下次调用都基于上一次调用结束时的位置开始。

核心规则：

1. readling()始终按“行”读取
2. size 只是一个字符数量的“软限制”
3. 如果：
   1. 先遇到换行符\n -> 整行返回
   2. 先到达 size -> 返回“半行”
4. 不会为了凑够 size 去读取下一行，例如，readline(n)，最多读取到 n 个字符，如果
   遇到\n 提前结束。

> 注意：readline(size)中的 size 不是指行数，而是字符上限，且不一定返回完整的一行
> ，也可能返回半行。

不同行为对照表：

| 调用方式     | 行为说明                                              |
| ------------ | ----------------------------------------------------- |
| readline()   | 读取一整行（直到\n 或 EOF）                           |
| readline(-1) | 等价于 readline()                                     |
| readline(0)  | 直接返回空字符串 ''                                   |
| readline(n)  | 最多读 n 个字符，当 n 大于*行长度*时，遇到\n 提前结束 |

用途：

1. 流式处理超大文件（精细控制内存）
2. 网络流、管道、非规则文本
3. 自定义分块行解析器

```py
buffer = ''
while True:
    part = f.readline(64)
    if not part:
        break
    buffer += part
    if buffer.endswith('\n'):
        handle_line(buffer)
        buffer = ''
```

### 11.5.3 readlines()方法

可以使用 readlines()一次性将文件的所有行读取为字符串列表，如下所示：

```py
with open('78SomewhereRd.txt', 'r') as house:
    lines = house.readlines()
    for line in lines:
        print(line.strip())
```

文件的每一行都单独存储在一个字符串中，所有字符串都存储在列表 lines 中。读取完所
有行后，输出每一行，并对字符串对象使用 strip()方法已删除每个字符串末尾的换行符。
这将删除所有前导或尾随空白字符，包括换行符。

readlines()方法有一个 hint 参数，是指“期望读取的字符总数上限”，而不是“行数” 或“
单行长度”，但是该值只是一个“参考值”，并非硬性限制。

核心规则：

1. 从当前位置开始，逐行读取
2. 累计已读取的字符数 total_chars
3. 一旦 total_chars >= hint
   1. 至少保证当前行完整读取
   2. 然后停止
4. 返回已读取的所有行，永远不会返回半行

不同行为对照表：

| 调用方式       | 行为说明                                                        |
| -------------- | --------------------------------------------------------------- |
| readlines(0)   | 不读取任何内容，返回空列表 `[]`                                 |
| readlines(-1)  | 当 hint 小于 0 时，等价于 readlines()，读取整个文件（直到 EOF） |
| readline(hint) | 累计读取 hint 个字符之后遇到第一个换行就停止                    |

使用场景：

1. 流式“分批”读取大文件（仍按行）
2. 与 `for line in f` 的关系

## 11.6 流位置

流位置表示“下一次读取或写入将发生的位置”。它是文件对象内部维护的一个偏移量，而不
是我们能直接看到的变量。

流位置三个核心特性：

1. 单一性：一个文件对象只有一个位置指针
2. 前进性：默认情况下，只能进不能退，除非我们显示地调用了`seek()`
3. 状态相关性：位置与打开模式(`r/w/a/x/+`)、文本/二进制模式、编码、缓冲策略强相
   关

### 11.6.1 tell()方法

tell() 获取当前位置。如果是二进制模式，返回字节偏移量；如果是文本模式，返回 _不
透明_ 的逻辑位置值，_返回不一定等于“字符数”_，因为 UTF-8 编码为多字节，换行符转
换(`\n` ↔ `\r\n`)都会导致文本模式下 tell()的返回值不一定等于字符数。

```py
with open('213AnywhereAve.txt', 'r') as house:
    print(repr(house.readline()))   # '78 Somewhere Road, Anytown PA\n'
    print(house.tell()) # 31
    print(repr(house.readline()))   # 'Cozy 2-bed, 1-bath bungalow. Full of potential.\n'
    print(house.tell()) # 80
```

### 11.6.2 seek()方法

seek()方法用于移动文件流的位置指针，返回新的位置值（与 `tell()` 一致）。其中
seek()有两个参数，offset 和 whence。

其中 offset 用于指定偏移量。单位取决于文件模式，如果在二进制模式下，单位为字节，
如果在文本模式下，单位为逻辑位置值，不是字符数。

whence 用于指定参考基准点。默认值为 0。表示以文件开头为偏移基准。

| whence | 常量        | 含义         |
| ------ | ----------- | ------------ |
| 0      | os.SEEK_SET | 从文件开头算 |
| 1      | os.SEEK_CUR | 从当前算     |
| 2      | os.SEEK_END | 从文件末尾算 |

其中 seek(0)常用于跳转到文件开头，seek(0, 2)用于跳转到文件结尾。

例如，重复输出第一行：

```py
with open('78SomewhereRd.txt', 'r') as house:
    for _ in range(3):
        print(house.readline().strip())
        house.seek(0)
```

输出如下：

```shell
78 Somewhere Road, Anytown PA
78 Somewhere Road, Anytown PA
78 Somewhere Road, Anytown PA
```

seek()方法也可以用来跳转到其他流位置，而不仅仅是开头或结尾。

```py
with open('78SomewhereRd.txt', 'r') as house:
    for n in range(10):
        house.seek(n)
        print(house.readline().strip())
```

## 11.7 写入文件

关于写入流，首先要记住的是，我们总是在覆盖，而不是插入！在追加内容到一个文件末尾
时，这并不重要，但是在其他情况下，这可能会导致混乱和不理想的结果。

### 11.7.1 write()方法

write()方法将给定的字符串从当前流位置开始写入文件，并返回一个整数来表示写入文件
的字符数量。但是请记住，这将覆盖从流位置到新数据末尾的所有数据。为防止数据意外弄
丢，一般先将文件读入内存，再修改内存中的文件数据，最后将它们写回同一文件。

```py
with open('78SomewhereRd.txt', 'r+') as real_estate_listing:
    contents = real_estate_listing.read()
```

首先以读写模式打开文件。这里不通过流直接修改文件内容，而是想文件数据作为字符串读
入内存，并绑定到 contents。然后通过处理这个字符串而不是流本身来修改描述：

```py
    contents.replace("Tiny", "Cozy")
    contents.replace("Needs repaires", "Full of potential")
    contents.replace("Small", "Compact")
    contents.replace("old storage shed", "datached workshop")
    contents.replace("Built on ancient burial ground.", "Unique atmosphere.")
```

以上代码使用 replace()字符串方法，将没有吸引力的单词和短语替换成了更有吸引力的单
词和短语。

一旦对字符串的新版本感到满意，就可以将其写回文件，如下所示：

```py
    real_estate_listing.seek(0)
    real_estate_listing.write(contents)
```

首先定位到文件的开头，因为我们想要使用 real_estate_listing.seek(0)覆盖那里的所有
内容。然后将新内容写入文件。任何碍眼的旧内容都将被覆盖。

剩下的问题就是新内容比旧内容短，所以一些旧数据还留在文件末尾。完成写入后，流位置
刚刚写入数据的末尾，可以利用这个位置清理旧数据的剩余部分，如下所示：

```py
    real_estate_listing.truncate()
```

默认情况下，truncate()方法将删除从当前流位置到文件末尾的所有内容，这是通过文件截
断到给定的字节数来实现的，该字节数可以作为参数传递。如果没有传入明确的截断长度
，truncate()将使用 tell()方法提供的值，该值对应当前流位置。

一旦流离开 with 语句，流就会被刷新并关闭，以确保写入对文件的更改。

### 11.7.2 writelines()方法

readlines()将文件内容存储为字符串列表，writelines()则将字符串列表写入文件
。writelines()不会在提供给它的列表中的每个字符串末尾插入换行符。write()和
writelines()之间的唯一区别就是后者接收一个字符串列表而不是一个字符串，并且不返回
任何内容。

使用 writelines() 重写上面的示例：

```py
with open('78SomewhereRd.txt', 'r+') as real_estate_listing:
    contents = []
    for line in real_estate_listing:
        line = line.replace("Tiny", "Cozy")
        line = line.replace("Needs repairs", "Full of potential")
        line = line.replace("Small", "Compact")
        line = line.replace("old storage shed", "datached workshop")
        line = line.replace("Built on ancient burial ground.", "Unique atmosphere.")
        contents.append(line)

    real_estate_listing.seek(0)
    real_estate_listing.writelines(contents)
    real_estate_listing.truncate()
```

因为换行符被 readlines()读入且保留在每行的末尾，所以这些换行符被原样写入。如果删
除了它们，则不得不在调用 writelines()之前，再次手动将它们追加回去。

### 11.7.3 用 print() 写入文件

print() 默认使用 sys.stdout 流输出内容，但其实也可以通过流传递给 file 参数来覆盖
对应文件。其中一种特殊用途正是有条件地输出到终端或文件。在某些情况下，print()的
简单格式化功能使其称为 write() 的绝佳替代品。

用 print()写文件的方法和 write()及 writelines()相同：我们必须有一个可写的流，并
且必须非常注意流的位置。

```py
nearby_properties = {
    "N. Anywhere Ave.": {
        123: 156_852,
        124: 157_923,
        126: 163_821,
        127: 133_121,
        128: 166_356
    },
    "N. Everywhere St.": {
        4567: 175_753,
        4568: 166_212,
        4569: 185_123
    }
}

with open('listings.txt', 'w') as real_estate_listings:
    for street, properties in nearby_properties.items():
        for address, value in properties.items():
            print(street, address, f"${value:,}", sep=' | ', file=real_estate_listings)
```

### 11.7.4 行分隔符

在 Windows 操作系统中，行由回车符(\r)和换行符(\n)分隔，而 UNIX 操作系统仅使用换
行符(\n)。在处理多种语言的文件时，这种差异可能给我们带来巨大的痛苦。

另一方面，Python 流 已经在幕后抽象出这种差异。在使用 print() 、write()或
writelines()以文本模式写入流时，只能使用通用换行符，也就是将换行符(\n)作为行分隔
符。

## 11.8 上下文管理器的细节

到目前为止，我们每次打开文件时都使用 with 语句来启用上下文管理器，以确保流在不需
要时立即关闭。

和 Python 中的很多其他复合语句一样，with 语句也利用一些特殊方法来处理对象。这意
味着 with 语句不仅限于流，它几乎可以处理任何需要 try-finally 逻辑的情况。为了说
明这一点，本节将详细介绍 with 语句如何与流交互，然后把这些知识应用到自定义类中。

### 11.8.1 上下文管理器工作原理

一个对象要想成为上下文管理器，就必须实现两个特殊方法，`__enter__()`和
`__exit__()`。

流实现了这两个方法。`__exit__()`方法关闭流，因此用户无须手动关闭
。`__enter__()`方法负责在使用上下文管理器之前进行任何所需的设置。这个方法在流的
情况下没有做任何有趣的事情，正如我们稍后将在自定义上下文管理器的示例中看到的那样
，上下文管理器类更多地使用 `__enter__()`。

根据定义上下文管理器的 PEP343，with 复合语句大致等同于以下代码：

```py
VAR = EXPR
VAR.__enter__()
try:
    BLOCK
finally:
    VAR.__exit__()
```

传递给 with 语句的表达式用于初始化对象。在对象上先调用 `__enter__()`方法，以执行
在使用对象之前应该完成的各种任务。（同样，在流的情况下，这个方法什么也不做。）接
下来，在 try 子句的上下文中调用 with 语句的代码块。无论成功与否，都会调用
`__exir__()`方法，`__exit__()`通常对对象执行任何必要的清理任务。

回顾上述清单，如果不使用 with 语句，就得在 finally 中关闭文件流。

```py
real_estate_listing = open('213AnywhereAve.txt')
try:
    print(real_estate_listing.read())
finally:
    real_estate_listing.close()
```

因为像 real_estate_listings 这样的流就是上下文管理器，所以我们可以如下使用：

```py
real_estate_listing = open('213AnywhereAve.txt')

real_estate_listing.__enter__()
try:
    print(real_estate_listing.read())
finally:
    real_estate_listing.__exit__()
```

再次提醒，`__enter__()`什么都没有做，而是作为上下文管理器的惯例被调用。完成后
，`__exit__()`方法会关闭流。这个版本让人感觉更冗长，但由于这是使用上下文管理器的
特殊方法，因此逻辑可以完全在一个 with 语句中处理：

```py
with open('213AnywhereAve.txt') as real_estate_listing:
    print(real_estate_listing.read())
```

这种形式更容易记住和输入。这一切都是由上下文管理器实现的。

### 11.8.2 使用多个上下文管理器

可以在 width 语句中使用功能多个上下文管理器，这带来了各种可能性。例如，我们希望
同时读取两个文件，为此，也许需要将他们合并为一个文件或查找他们之间的差异。（为方
便起见，在这个示例中，实际上不会对这些文件做任何事情，只是打开他们。）

为了在一个 with 语句中打开多个流，可以使用逗号分隔头部声明中的多个 open()表达式
，如下所示：

```py
with open('213AnywhereAve.txt', 'r') as left, open('listings.txt', 'r') as right:
    print(left.read())
    print(right.read())
```

这样就可以按照常规的方式使用 left 和 right 流了，而且在语句结束时，两个流都将自
动关闭。

### 11.8.3 实现上下文管理协议

上下文管理协议是用于 `__enter__()`和 `__exit__()`特殊方法的 Python 官方术语。任
何实现这两个特殊方法的对象都可以通过 with 语句进行上下文管理。上下文管理不仅适用
于流，还可以用来自动执行在使用对象之前及之后需要完成的任务。

请记住，我们只需要实现这些方法即可。如果不需要其中一个方法实际做任何事情，就不要
将任何功能写入不需要的方法。

下面以房屋展示为例说明这一点。在想潜在买家展示房屋之前，必须打开房门。看房结束离
开时，则必须锁上门。这种模式正好就是上下文管理器的应用场景。

首先，定义整个 House 类：

```py
class House():

    def __init__(self, address, house_key, **rooms):
        self.address = address
        self.__house_key = house_key
        self.__locked = True
        self._rooms = dict()
        for room, desc in rooms.items():
            self._rooms[room.replace("_", " ").lower()] = desc.lower()

    def unlock_house(self, house_key):
        if self.__house_key == house_key:
            self.__locked = False
            print("House unlocked.")
        else:
            raise RuntimeError("Wrong key! Cloud not unlock house.")

    def explore(self, room):
        if self.__locked:
            raise RuntimeError("Cannot explore a locked house.")

        try:
            return f"The {room.lower()} is {self._rooms[room.lower()]}."
        except KeyError as e:
            raise KeyError(f"No room {room}") from e

    def lock_house(self):
        self.__locked = True
        print("House locked!")
```

这个类完全依赖于前文中的概念。简言之，House 对象使用 address 作为键值，对每个房
间的关键字参数进行初始化。我们可能会注意到，在将房间名称存储到 self.\_rooms 字典
之前，初始化器会将关键字参数命中的下划线替换成空格，同时将房间名称和描述转换为小
写。这将使该类的用法在感觉上更加明显，而且不容易出错。

这个示例的最重要部分是 HouseSHowing 类，最终我们将通过分别实现 `__enter__()`和
`__exit__()`特殊方法来编写上下文管理器。

```py
class HouseShowing():

    def __init__(self, house, house_key):
        self.house = house
        self.house_key = house_key
```

HouseShowing 类的初始化器接收两个参数：House 实例和用来解锁房屋的键值。我们分别
编写 `__enter__()`和 `__exit__()`特殊实例方法，从而令 HouseShowing 成为上下文管
理器。

### 11.8.4 `__enter__()`方法

在展示 House 实例中的任何数据之前，必须先打开"房门"。如果要是错了，就无法进入，
所以继续展示也没有意义。由于此行为应该始终发生在使用任何其他 House 实例之前，因
此值得用 `__enter__()`特殊实例方法进行处理：

```py
class HouseShowing():

    def __init__(self, house, house_key):
        self.house = house
        self.house_key = house_key


    def __enter__(self):
        self.house.unlock_house(self.house_key)
        return self
```

可以尝试使用初始化 HouseShowing 时使用的秘钥来打开房门。请注意，此处没有执行任何
异常处理。始终允许因使用我们的类而产生的错误通过此方法冒泡，这样使用我们的类的其
他开发者就可以修复他们的代码。

重要的是，必须从 `__enter__()`方法返回示例，这样 with 语句才可以使用它。

用户应该能够直接使用该对象，而不必深入研究其属性。展示房间的主要目的是查看不同的
房间，因此需要编写一个方法：

```py
    def show(self, room):
        print(self.house.explore(room))
```

再次提醒，我们会注意到这里没有处理任何来自 house.explore()的可能异常，因为这都和
类的使用方法有关。

### 11.8.5 `__exit__()`方法

当看房结束离开时，必须把房门锁好。该行为由特殊实例方法 `__exit__()`处理：

```py
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("Sorry about that.")
        self.house.lock_house()
```

此方法必须接收除 self 外的 3 个参数。如果在 with 代码块中的任何地方引发异常，这
3 个参数将描述异常的类型(exc_type)、消息(exc_val)和回溯(exc_tb)。如果没有触发异
常，这 3 个参数都将为 None。

尽管 `__exit__()`必须接收这些参数，但是不需要让其真正做任何事情。如果需要在发生
某些异常时执行不同的关闭或清理操作，这些参数就很有用。在这个例子中，如果有任何例
外，就在锁门时向客户道歉。这里没有使用功能消息和回溯参数。如果没有例外，就只是把
门锁上。

重要的是 `_-exit__()`在引发或处理错误方面没有任何作用！它只是充当侦听器，侦听
with 代码块中发生的任何异常。在 `__exit__()`中，使用条件语句来处理作为参数传递的
异常。不能使用 try 语句，因为任何异常都不会直接通过 `__exit__()`冒泡。永远不应该
重新引发传入的异常，因为 with 代码块中发生的任何异常都将由负责的语句引发，并由调
用方处理。

再次提醒，`__exit__()`在处理异常方面没有任何作用。`__exit__()`方法应该处理的唯一
异常时 with 代码块中直接引发的那个异常。

### 11.8.6 使用自定义类

HouseShowing 类是一个上下文管理器，现在可以开始使用它了。

```py
house = House("123 Anywhere Street", house_key=1803,
              living_room="specious",
              office="bright",
              bedroom="cozy",
              bathroom="small",
              kitchen="modern")
```

在创建 House 实例时，将 house_key 定义为 1803，这是稍后定义 HouseShowing 时必须
提供的值。

在 with 语句的上下文中创建一个新的 HouseShowing，并将创建的 House 实例传递过来。
如果使用了错误的 house_key，则应该抛出一个异常：

```py
with HouseShowing(house, house_key=999) as showing:
    showing.show('Living Room')
    showing.show('bedroom')
    showing.show('porch')
```

由于 house_key 错误，房门将无法打开：

```shell
Traceback (most recent call last):
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 58, in <module>
    with HouseShowing(house, 999) as showing:
         ~~~~~~~~~~~~^^^^^^^^^^^^
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 40, in __enter__
    self.house.unlock_house(self.house_key)
    ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 16, in unlock_house
    raise RuntimeError("Wrong key! Cloud not unlock house.")
RuntimeError: Wrong key! Cloud not unlock house.
```

由于 house_key 错误，`shouwing.__enter__()`遇到异常。这很重要。我们需要向
house_key 传递正确的值。with 语句甚至没有尝试运行其代码块，一遇到异常就放弃了。

将更正后的值传递给 house_key：

```py
with HouseShowing(house, house_key=1803) as showing:
    showing.show('Living Room')
    showing.show('bedroom')
    showing.show('porch')
```

现在，房门可以打开了。子啊 with 代码块中，对 show()方法进行了 3 次调用。前两次可
以正常工作，因为绑定到 house 的 House 实例定义了那些房间，但是第三次将失败并出现
异常。让我们看一下输出：

```shell
House unlocked.
The living room is specious.
The bedroom is cozy.
Sorry about that.
House locked!
Traceback (most recent call last):
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 23, in explore
    return f"The {room.lower()} is {self._rooms[room.lower()]}."
                                    ~~~~~~~~~~~^^^^^^^^^^^^^^
KeyError: 'porch'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 61, in <module>
    showing.show('porch')
    ~~~~~~~~~~~~^^^^^^^^^
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 44, in show
    print(self.house.explore(room))
          ~~~~~~~~~~~~~~~~~~^^^^^^
  File "\my-python-journey\programing\dead-simple-python\chapter-11\demos\house_showing.py", line 25, in explore
    raise KeyError(f"No room {room}") from e
KeyError: 'No room porch'
```

with 语句在 HouseShowing 上调用了 `show.__enter__()`，后者有调用了
house.unlock_house()。然后，每次调用 with 语句中的 showing.show()时，都会输出所
请求房间的描述。

第三次调用请求查看门廊，但因为房子并没有门廊，所以调用失败并出现异常。相反
，`showing.__exit__()`被调用，且异常被传递给它。道歉的话被输出，然后
house.lock_house()被调用。

经过这一切之后，异常的回溯被输出。要解决代码中的问题，就需要放弃查看门廊的请求，
并改为请求一个确实存在的房间，比如厨房：

```py
with HouseShowing(house, 1803) as showing:
    showing.show('Living Room')
    showing.show('bedroom')
    showing.show('Kitchen')
```

输出以下内容：

```shell
The living room is specious.
The bedroom is cozy.
The kitchen is modern.
House locked!
```

没有错误。门被打开，显示所有请求的房间，然后门被再次上锁。因为没有出现异常，所以
`house.__exit__()` 不会输出之前道歉的话。

## 11.9 路径

到目前为止，所使用的文件和打开它们的模块都在同一目录中。而现实中，文件可能位于操
作系统的任何位置。这绝非小事，我们接下来将介绍文件路径。

首先，所有操作系统中的文件路径都不相同。UNIX 风格的系统，使用 POSIX 文件路径约定
，而 Windows 系统则使用完全不同的方案。其次，我们无法始终确定代码是在哪个目录中
运行的，因此，相对路径只能解决一部分问题。最后，不能假设重要目录的名称或位置，例
如用户的主目录。简言之，文件路径很难概括。

为了解决这些问题，Python 提供了两个模块：os 模块和 pathlib 模块。在 Python3.6 之
前，使用 os 模块及其子模块(os.path)是处理文件路径的标准方法。os 模块允许我们在任
何操作系统中以可移植的方式运行代码，但是作为一个整体，该模块非常复杂，且充满了冗
长和一些非常烦人的遗留代码。os 模块也被认为是某种“垃圾抽屉”，因为其中包含与操作
系统相关的各种函数和类。因此，我们很难知道应从 os 模块中使用什么，甚至不知道如何
使用。

pathlib 模块在 Python3.4 中引入，并在 Python3.6 中获得 open()的完全支持。它提供
了一种更简洁、更有条理性以及更加可预测的路径处理方式。更为重要的是，它已经取代了
os.path 的大部分内容并清晰地整合了 os 模块和另一个相关模块 glob 所提供的大部分文
件系统功能，支持按照 UNIX 规范找到符合特定模块的多个路径。

### 11.9.1 路径对象

pathlib 模块提供了几个代表文件系统路径的相关类，被成为类路径类 —— 从 Python3.6
开始它们都继承自 os.Pathlike 抽象类，是文件系统路径不可变表示。重要的是，类路径
对象不基于字符串，他们都是具有各种行为的独特对象，基于路径的各个部分以及这些部分
又如何组织在一起，可以抽象出很多逻辑。

pathlib 路径对象的优点之一就是能在幕后根据操作系统安定地处理所有不同操作系统约定
：当前目录(.)、父目录（..）、斜线（/或\\）等。

当前有两种类型的类路径对象：纯路径和具体路径

#### 纯路径

允许在不访问底层文件系统的情况下使用的路径成为纯路径。根据操作系统的不同，从
PurePath 类实例化一个对象将在后台自动创建一个 PurePosixPath 或 PureWindowsPath
对象。通常可以将此委托给 Python 来解决，尽管如果代码需要，也可自行实例化特定类型
的路径：

```py
from pathlib import PurePath

path = PurePath('../index.md')
with open(path, 'r', encoding='utf-8') as file:
    print(file.read())

# AttributeError: 'PureWindowsPath' object has no attribute 'touch'
path.touch()
```

可以将 PurePath 对象传递给 open()函数以打开../index.md。但是，无法通过路径对象本
身对文件系统进行交互。如果尝试使用 path.touch()进行操作，就会失败。

如果只打算在对 open()的调用中使用路径，或者不打算通过路径对象的方法直接和系统交
互，那么应该使用纯路径，这可以防止意外修改文件系统。

#### 具体路径

具体路径提供了和文件系统交互的方法。从 Path 类实例化对象将创建一个 PoxisPath 或
WindowsPath 对象，如下所示：

```py
from pathlib import Path

path = Path('../index.md')
with open(path, 'r', encoding="utf-8") as file:
    print(file.read())

# 当文件不存在时创建一个空文件
path.touch()
```

上面两个示例几乎相同，只是一个是 PurePath 对象一个是 Path 对象。因此仍然可以打开
路径，但是也可以使用 Path 对象上的方法直接和文件系统交互。例如，如果 index.md 不
存在，则可以通过 path.touch() 创建一个空文件。

如果我们明确地要将自己的实现耦合到一个特定的操作系统，请使用路径类的 Windows 或
Posix 形式；否则，使用 PurePath 或 Path。

### 11.9.2 路径组成

类路径对象由路径根据操作系统在后台连接为一体的部分组成。路径的写法有两种——相对路
径和绝对路径，它们都适用于所有 PurePath 和 Path 对象。

绝对路径是从文件系统的根目录开始的路径。文件的绝对路径始终以锚点开头并以一个名称
（完备文件名）结尾。这个名称由第一个非前导点之前的词干和通常位于该点之后的一个或
多个扩展名组成。如下所示：

```shell
/path/to/file.txt
```

此处的锚点是前导斜线(/)。文件名为 file.txt，词干为 file，扩展名为 .txt。

可以从类路径对象中检索这些部分。比如使用 PurePath.parts()方法，该方法返回一个部
件元组。或者将特定组件作为特性来访问。

如下所示为一个输出传递进来的路径的每个部分的函数。后文将使用该函数分别剖析
Windows 路径和 POSIX 路径。

```py
import pathlib

def path_parts(path):
    print(f"{path}\n")

    print(f"Drive: {path.drive}")
    print(f"Root: {path.root}")
    print(f"Anchor: {path.anchor}\n")

    print(f"Parent: {path.parent}\n")
    for index, parent in enumerate(path.parents):
        print(f"Parents [{index}]: {parent}")

    print(f"Name: {path.name}")
    print(f"Suffix: {path.suffix}")
    for i, suffix in enumerate(path.suffixes):
        print(f"Suffixes [{i}]: {suffix}")
    print(f"Stem: {path.stem}\n")

    print("------------------------\n")
```

#### Windows 路径组成

```py
path_parts(pathlib.PureWindowsPath('F:/my-python-journey/programing/dead-simple-python/chapter-11/index.md'))
```

输出如下：

```shell
F:\my-python-journey\programing\dead-simple-python\chapter-11\index.md

Drive: F:
Root: \
Anchor: F:\


Parents [0]: F:\my-python-journey\programing\dead-simple-python\chapter-11
Parents [1]: F:\my-python-journey\programing\dead-simple-python
Parents [2]: F:\my-python-journey\programing
Parents [3]: F:\my-python-journey
Parents [4]: F:\
Name: index.md
Suffix: .md
Suffixes [0]: .md
Stem: index

------------------------

```

#### POSIX 路径组成

```py
path_parts(pathlib.PurePosixPath('/usr/lib/x86_64-linux-gnu/libpython3.7m.so.1'))
```

输出如下所示：

```shell
/usr/lib/x86_64-linux-gnu/libpython3.7m.so.1

Drive:
Root: /
Anchor: /

Parent: /usr/lib/x86_64-linux-gnu

Parents [0]: /usr/lib/x86_64-linux-gnu
Parents [1]: /usr/lib
Parents [2]: /usr
Parents [3]: /
Name: libpython3.7m.so.1
Suffix: .1
Suffixes [0]: .7m
Suffixes [1]: .so
Suffixes [2]: .1
Stem: libpython3.7m.so

------------------------

```

这一示例演示了我们可能遇到的和文件扩展名相关的独特问题。虽然存在包含多个后缀的有
效扩展名，例如 .tar.gz（经由 GZ 压缩的 tarball），但是并非每个后缀都是文件扩展名
的一部分。例如，预期的文件名是 libpython3.7m，但是 pathlib 错误地将.7m 解析为后
缀之一，毕竟它包含前导点。同时，由于预期的文件扩展名(.so.1)实际上由两个后缀组成
，因此词干又错误地检测为 libpython3.7m.so，而后缀仅被检测为.1。在路径中查找文件
扩展名时，需要牢记一点。目前没有简单或明显的方式能够解决这个问题，必须根据代码的
需要逐一处理。简而言之，不要过分依赖 pathlib 对词干和后缀的辨别能力，它很可能以
非常恼人的方式让我们失望。

### 11.9.3 创建路径

可以通过将路径作为字符串传递给需要的类初始化器来定义路径。然后就可以将路径和
open()或任何其他文件操作函数一起使用了。例如，在 UNIX 系统中，可以使用如下所示的
代码访问 bash 历史记录。

```py
from pathlib import PosixPath

path = PosixPath('/home/jason/.bash_history')
```

在初始化类路径对象并将其绑定到 path 后，可以执行打开操作。有两种方法可以做到这一
点：将其传递给 open()，或者对 Path 对象使用 open()方法（不可用于 PurePath 对象）
。这里使用后者，如下所示：

```py
with path.open('r') as file:
    for line in file:
        continue
    print(line.strip())
```

在此示例中，尽管只需要文件的最后一行，也仍然遍历整个文件。循环结束时，名称 line
将绑定到读取的最后一行的字符串内容。除此之外，再没有更简单的方法从文件末尾进行读
取。

最后，输出这一行，并使用 strip() 方法清除尾部的换行符。
