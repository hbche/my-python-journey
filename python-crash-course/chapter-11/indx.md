# 第 11 章 测试代码

## 11.1 使用 pip 安装 pytest

pytest 是第三方包，非Python核心的库，需要独立安装。

### 11.1.1 更新 pip

Python 提供了一个名为 pip 的工具，可用来安装第三方包。因为 pip 帮我安装来自外部的包，所以更新频繁，我们需要先更新 pip。

``` bash
python -m pip install --upgrade pip
```

这个命令行的第一部分 `python -m pip` 让 Python 运行 pip 模块；第二部分 `install --upgrade` 让 Python 更新一个已安装的包；最后一部分 `pip` 指定要更新那个第三方包。

可使用下面的命令来更新系统中安装的任何包：
``` bash
python -m pip install --upgrade package_name
```

### 11.1.2 安装 pytest

将 pip 升级到最新版本后，就可以安装 pytest 了：

``` bash
python -m pip install --user pytest
```

此处指定的是 `--user` 而不是 `--upgrade` 参数，表明让 Python 只给当前用户安装指定的包。

可以使用下面的命令行安装众多的第三方包：

``` bash
python -m pip install --user package_name
```

## 11.2 测试函数

``` python
def get_formatted_name(first, last):
    """格式化姓名"""

    full_name = f"{first.title()} {last.title()}"
    return full_name
```

``` python 
from name_functions import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input('Please give me a last name: ')
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}")
```

### 11.2.1 单元测试和测试用例

软件的测试方法多种多样。一种最简单的测试是单元测试(unit test)，用于核实函数的某个方面没有问题。测试用例(test case)是一组单元测试，这些单元测试一道核实函数在各种情况下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情况的测试。全覆盖(full coverage)测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。对于大型项目，要进行全覆盖测试可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。

### 11.2.2 可通过的测试

使用pytest进行测试，会让单元测试编写起来非常简单。我们将编写一个测试函数，它会调用要测试的函数，并做出有关返回值的断言。如果断言正确，表示测试通过；如果断言不正确，表示测试未通过。


``` python
from name_functions import get_formatted_name

def test_first_last_name():
    """测试get_formatted_name"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

测试文件名很重要，必须以 **tet_** 开头。当我们运行 pytest 时，它将查找以 test_ 开头的文件，并运行其中的所有测试用例。

一般我们不会自己调用测试函数，而是由 pytest 替我们查找并运行它们。

**断言**是声称满足特定的条件：这里声称 formatted_name 的值为 'Janis Joplin'。

### 11.2.3 运行测试

如果直接运行文件test_name_function.py，将不会有任何输出，因为我们没有调用这个测试函数。相反，应该让pytest替我们运行这个测试文件。

为此，打开一个终端窗口，并切换到这个测试文件所在的文件夹。并运行 `pytest` 。

> 注意：如果出现一条消息，提示没有找到命令pytest，请执行命令python -m pytest。

``` bash
python -m pytest
```

输出：

``` bash
collected 1 item

test_name_functions.py .                                  [100%]

====================== 1 passed in 0.01s =======================

```

### 11.2.4 未通过的测试

我们来修改 get_formatted_name()，使其能够处理中间名。但同时故意让这个函数无法正确处理想 janis joplin 这样只有名和姓的场景。

``` python
def get_formatted_name(first, middle, last):
    """格式化姓名"""

    full_name = f"{first.title()} {middle.title()} {last.title()}"
    return full_name
```

运行 pytest 查看测试结果：

``` bash
collected 1 item

test_name_functions.py F                                  [100%]

=========================== FAILURES ===========================
_____________________ test_first_last_name _____________________

    def test_first_last_name():
        """测试get_formatted_name"""

        formatted_name = get_formatted_name('janis', 'joplin')
>       assert formatted_name == 'Janis Joplin'
E       AssertionError: assert 'Janis  Joplin' == 'Janis Joplin'
E
E         - Janis Joplin
E         + Janis  Joplin
E         ?      +

test_name_functions.py:7: AssertionError
=================== short test summary info ====================
FAILED test_name_functions.py::test_first_last_name - AssertionError: assert 'Janis  Joplin' == 'Janis Joplin'
====================== 1 failed in 0.06s =======================
```

### 11.2.5 在测试未通过时怎么办

在测试未通过时，该怎么办呢？如果检查的条件没错，那么测试通过意味着函数的行为是对的，而测试未通过意味着我们编写的新代码有错。
因此，在测试未通过时，不要修改测试。因为如果我们这样做，即便能让测试通过，像测试那样调用函数的代码也将突然崩溃。相反，应修
复导致测试不能通过的代码：检查刚刚对函数所做的修改，找出这些修改是如何导致函数行为不符合预期的。

``` python
def get_formatted_name(first, last, middle=''):
    """格式化姓名"""

    if middle:
        full_name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"
    return full_name
```

对函数 get_formatted_name() 进行优化后，再运行 pytest:

``` bash
collected 1 item

test_name_functions.py .                                  [100%]

====================== 1 passed in 0.01s =======================
```


### 10.2.6 添加新测试

确定get_formatted_name()又能正确地处理简单的姓名后，我们再编写一个测试，用于测试包含中间名的姓名。

``` python
from name_functions import get_formatted_name

def test_first_last_name():
    """测试get_formatted_name"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """测试get_formatted_name包含中间名的场景"""

    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Mozart Amadeus'
```

测试运行 pytest 的结果：

``` bash
===================== test session starts ======================
platform win32 -- Python 3.13.7, pytest-8.4.2, pluggy-1.6.0
rootdir: C:\Users\红红的海景房\Desktop\my-python-journey\python-crash-course\chapter-11
collected 2 items

test_name_functions.py ..                                 [100%]

====================== 2 passed in 0.02s =======================
```