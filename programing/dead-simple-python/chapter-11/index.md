# 第 11 章 文本输入\输出和上下文管理

## 11.1 标准输入和输出

## 11.2 流

## 11.3 上下文管理器基础

## 11.4 文件模式

## 11.5 读取文件

## 11.6 流位置

## 11.7 写入文件

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
```
