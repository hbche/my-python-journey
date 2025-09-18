# 第 4 章 项目结构和代码导入

## 4.1 设置代码仓库

至少需要创建以下文件：

- README.md，它是项目和目标的描述文件
- LICENSE.md，它是项目的许可证
- .gitignore，它是一个特殊文件，用于只是 Git 忽略哪些文件和目录
- 一个目录，它的名字与项目的名字相同

我们的 Python 代码应该放在一个单独的子目录中，而不是放在仓库的根目录中。

## 4.2 模块和包

模块就是一个 Python 文件

包是包含一个或多个模块的目录。该目录必须包含一个名为 `__init__.py` 的文件。`__init__.py` 文件很重要！如果它不存在，Python 将不知道相应的目录会构成一个包。

> 模块实际上是对象，而不仅仅是文件。

`__init__.py` 文件可以为空（通常为空），也可以用它在第一次导入包时运行某些代码。

如果我们在包中没有创建 `__init__.py` 文件，它将变成一个隐式的命名空间包。它的行为和常规包不同，两者是不可替换的。命名空间包允许将包分发为多个部分。

### 4.2.1 PEP8 和命名

包和模块需要使用清晰的名称来标识。

模块是以文件名命名的，包是以目录名命名的。

### 4.2.2 项目的目录结构

## 4.3 import 是如何工作的

## 4.4 导入操作的注意事项

声明模块：

```python
def open():
    """模拟开门"""
    print("Ahhhhhhhhh.")

def close():
    """模拟关门"""
    print("Thank you for making a simple door every happy.")
```

open() 和 close() 的命名空间是 smart_door。命名空间是对某些对象（如函数）的显示定义路径。

使用模块：

```python
import smart_door

smart_door.open()
smart_door.close()
```

### 4.4.1 从模块中导入函数

```python
from smart_door import open

open()
```

smart_door 命名空间和 close 函数都不可用，因为没有直接导入命名空间和函数。import 命名仍然运行了整个模块，但只导入了 open 函数。

```python
from smart_door import open, close

open()
close()
```

### 4.4.2 覆盖问题

如果从 smart_door 模块中导入了 open 函数，Python 内置的 open 函数将会被该函数覆盖，导致内部 open 函数失效。

```python
from smart_door import open, close

open()
close()

somefile = open('smart_door.py', 'r')
somefile.close()
```

Python 内部提供了 as 关键字给导入的函数指定别名。

```python
from smart_door import open as door_open, close as door_close

door_open()
door_close()

somefile = open('smart_door.py', 'r')
somefile.close()
```

### 4.4.3 包嵌套问题

包可以包含其他包。

```python
import omission.data.data_loader
```

Python 解释器会查找 omission 包，然后在 omission 包中查找 data 包，再在 data 包中查找 data_loader.py 模块。

虽然理想世界中的项目永远不会有过多的嵌套，但现实世界中的项目并不总是那么整洁。有时，想要避免深度嵌套结构是不可能的。为此，需要有另一种方法使导入语句清晰易懂。幸运的是，导入系统可以处理这个问题：

```python
from musicapp.player.data.library.song import play

play()
```

只需要在实际的导入语句中处理一次深度嵌套的命名空间，之后使用函数名 play()即可。

或者如果想要一点点命名空间，也可以这样做：

```python
from musicapp.player.data.library import song

song.player()
```

### 4.4.4 谨慎导入所有

```python
from smart_door import *
from gzip import *

open()
```

如果这样做，就可能完全不知道 open()、smart_door.open()和 gzip.open()都存在，并且它们在文件中争夺同一个名称！在这个例子中，函数 gzip.open()将会获胜，因为它是最后一个被导入的 open()版本。另外两个函数都被覆盖（这意味着实际上根本无法调用它们）​。

## 4.5 在项目中使用 import

现在创建一个 omission 的项目，项目的目录结构如下：

```bash
omission-git/
└── omission/
     ├── __init__.py
     ├── __main__.py
     ├── app.py
     ├── common/
     │   ├── __init__.py
     │   ├── classproperty.py
     │   ├── constants.py
     │   └── game_enums.py
     ├── data/
     │   ├── __init__.py
     │   ├── data_loader.py
     │   ├── game_round_settings.py
     │   ├── scoreboard.py
     │   └── settings.py
```

### 4.5.1 绝对导入

### 4.5.2 相对导入

### 4.5.3 从同一个包中导入

## 4.6 入口点

导入或执行包时首先运行的部分称为入口点。

### 4.6.1 模块入口点

当导入一个模块或包时，它会被赋予一个特殊的变量 `__name__`。这个变量的值为模块或包的完全限定名称，也是导入系统看到的名称。例如，omission/common/game_enums.py 模块的完全限定名称是 omission.common.game_enums。但有一个例外：当一个模块或包被直接运行时，它的 `__name__` 被设置为值 `__main__`。

我们创建一个 testpkg 包，其中包含 awesome.py 模块。该模块中定义了一个函数 greet()：

```python
def greet():
    print("Hello, world!")

print("Awesome module was run.")
```

testpkg 目录中有一个 example.py 的模块，使用 python 命令直接运行它，example.py 的内容如下：

```python
from testpkg import awesome

print(__name__)             # __main__
print(awesome.__name__)     # testpkg.awesome
```

第一行输出来自 testpkg/awesome.py，它是由导入命令运行的。其余的输出来自 example.py 中的两个输出命令。

### 4.6.2 包入口点

请注意，omission 项目的顶级包中有一个名为`__main__`的文件。直接执行包时，将自动运行该文件，但该文件不会在导入包时运行。

所以当通过命令 `python -m omission` 执行 omission 包时，Python 首先运行`__init__.py` 模块，然后运行`__main__.py` 模块。如果包被导入，则只有`__init__.py` 模块会被执行。

如果在包中省略了`__main__.py`，则包不能被直接执行。

一个好的定义包的 `__main__.py` 文件如下所示：

```python
def main():
    # Code to start/run your package

if __name__ == "__main__":
    main()
```

所有启动包的逻辑都应该在 main()函数中。然后，if 语句检查`__main__.py` 模块的`__name__`变量的值。如果这个包正在被执行，则**name**的值为 "`__main__`" ，并且 if 语句中的代码（即对 main()函数的调用）将运行。如果`__main__.py` 只被导入，则它的完全限定名称将包含其包名（如 `omission.__main__`）​，调用将失败，代码不会运行。

### 4.6.3 控制包的导入

当想要改变可导入的内容及其使用方式时，包的`__init__.py`文件会很有用。这个文件最常见的用途是简化导入和控制导入所有（import \*）的行为。

1. 简化导入
2. 控制导入所有

### 4.6.4 程序的入口点

为了让 omission 项目更容易运行，我们在顶层包的外部创建了一个单独的脚本文件，名为 omission.py ，如下所示：

```python
from omission.__main__ import main
main()
```

## 4.7 Python 模块搜索路径

模块搜索路径（或导入路径）定义了 Python 在哪里查找包和模块，以及搜索的顺序。第一次启动 Python 解释器时，模块搜索路径将按正在执行的模块的目录、系统变量 PYTHONPATH、正在使用的 Python 实例的默认路径的顺序组装。

可以使用下面的命令来查看生成的模块搜索路径：

```bash
import sys
print(sys.path)
```

## 4.8 导入模块时到底发生了什么？

为了导入一个模块，Python 需要使用两个特殊对象：一个查找器和一个加载器。在某些情况下，可以使用导入器充当查找器和加载器。

查找器负责查找想要导入的模块。有很多地方可以查找模块—它们甚至不一定是文件—并且存在许多必须处理的特殊情况。Python 提供了几种类型的查找器来处理这些不同的情况，并且它给了每一个查找器查找给定名称的模块的机会。

首先，Python 使用元路径查找器，它们存储在 sys.meta_path 列表中。默认情况下，有以下 3 个元路径查找器。

- 内建导入器
- 冻结导入器
- 路径查找器
