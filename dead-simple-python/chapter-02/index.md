# 第 2 章 Python 开发环境

## 2.1 安装 Python

### 2.1.1 在 Windows 系统中安装 Python

去 Python 官方网站下载 Python Windows 版本对应架构（如 x86）的安装包安装即可。

### 2.1.2 在 macOS 系统中安装 Python

```bash
brew install python
```

### 2.1.3 在 Linux 系统中安装 Python

在 Unbuntu、Debian 中安装：

```bash
sudo apt install python3 python3-pip python3-venv
```

在 Fedora、REHL 或 CentOS 中安装：

```bash
sudo dnf python3 python3-pip
```

在 ArchLinux 中安装：

```bash
sudo pacman -S python python-pip
```

### 2.1.4 通过源代码构建 Python

## 2.2 认识 Python 解释器

### 2.2.1 交互式会话

解释器的交互式会话允许我们实时输入和运行代码，并查看结果。我们可以打开命令行终端
，输入 python 来进入交互式会话，以下是我的直接结果：

```bash
Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

可以使用 `exit()` 函数退出交互式会话。

### 2.2.2 运行 Python 文件

我们可以在文本或代码编辑器中编写脚本和程序，使用 Python 解释器 运行 Python 文件
。

```bash
python myfile.py
```

## 2.3 包和虚拟环境

一个包是指一组代码，这与大多数其他编程语言中的库类似。

一个虚拟环境是一个沙盒，我们可以在其中安装特定项目所需的 Python 包，避免项目之间
的包存在冲突。为每个项目创建不同的沙盒，并且只在其中安装所需的包，一切都井井有条
。

### 2.3.1 创建虚拟环境

每个虚拟环境都位于专用目录中。通常以相应文件夹命名为 env 或 venv。

对于每个项目，我们通常会在项目文件夹内创建一个专用的虚拟环境。Python 提供了一个
名为 venv 的工具来实现这一点。

我们可以执行以下命令来创建一个名为 venv 的虚拟环境：

```bash
python -m venv venv
```

其中第一个 venv 指的是 Python 调用 venv 包生成虚拟环境，第二个 venv 是这个生成的
虚拟环境的名称叫 venv，可以为任意的名称，建议 xx_venv 这种以 venv 结尾的命名。

### 2.3.2 激活虚拟环境

为了使用虚拟环境，我们需要先激活它。

在类 UNIX 系统中，运行以下命令：

```bash
source ./venv/bin/activate
```

在 Windows 系统中，则运行以下命令：

```cmd
.\venv\Scripts\activate
```

现在我们正在使用我们的虚拟环境了。我们可以在命令行提示符的开头看到 venv，这表明
我们正在使用名为 venv 的虚拟环境。

我们在虚拟环境中安装的任何包都只能在虚拟环境中使用。

### 2.3.3 退出虚拟环境

类 UNIX 系统：

```bash
deactivate
```

在 Windows 系统中，使用以下命令：

```cmd
deactivate
```

## 2.4 pip 介绍

Python 的包管理器是 pip，它通常使包的安装变得轻而易举，特别是在虚拟环境中。

### 2.4.1 系统范围内的包

在进行任何 Python 开发时，我们都应该在虚拟环境中工作。这确保不会搞乱系统中其他程
序的包。

### 2.4.2 安装包

我们可以运行以下命令来安装包：

```bash
python -m pip install package_name
```

如果需要指定包版本，我们可以这样执行：

```bash
python -m pip install package_name==x.x.x
```

此处报名和版本号之间使用双等于号连接，我们还可以用运算符 >= 来表示 "至少这个版本
或更高版本"。

如果我们在类 UNIX 系统中，我们可能需要使用双引号将包名和版本包裹起来，因为 `>`
在 shell 中另有含义。

```bash
python -m pip install "PySide6>=6.1.2"
```

### 2.4.3 requirements.txt

我们可以通过配置 requirements.txt 文件为我们的项目开发节省更多的时间。这个文件列
出了我们项目所需要的包。在创建一个虚拟环境时，通过这个文件，我们和其他用户可以使
用一个命令安装所有需要的包。

在创建这个文件时，将一个包的名称和版本卸载同一行。如下示例：

```txt
PySide2>=5.11.1
appdirs
```

现在，任何人都可以使用下面的命令一次性安装所有这些包：

```bash
python -m pip install -r .\requirements.txt
```

### 2.4.4 更新包

我们也可以使用 pip 更新已更新的包。例如，要将 PySide6 更细到最新版本，可以运行下
面的命令：

```bash
python -m pip install --upgrade PySide6
```

如果我们有一个 requirements.txt 文件，我们也可以一次性升级所有需要的包：

```bash
pythom -m pip install --upgrade -r .\requirements.txt
```

### 2.4.5 卸载包

我们可以使用下面的命令卸载包：

```bash
python -m pip unstall package
```

这里有个小问题。安装一个包时，它所依赖的包也会被安装，我们称之为依赖项。卸载一个
包时，它的依赖项不会被卸载，所以我们可能需要手动卸载它们。这可能会变得棘手，因为
多个包可能共享依赖项，所以我们可能会破坏另一个包。

在这里，虚拟环境的优势就体现出来了。一旦我们陷入这种困境，我们可以删除虚拟环境，
再创建一个新的虚拟环境，然后只安装所需要的包即可。

### 2.4.6 搜索包

使用 pip 自身进行搜索：

```bash
python -m pip search web scraping
```

输出：

```bash
ERROR: XMLRPC request failed [code: -32500]
RuntimeError: PyPI no longer supports 'pip search' (or XML-RPC search). Please use https://pypi.org/search (via a browser) instead. See https://warehouse.pypa.io/api-reference/xml-rpc.html#deprecated-methods for more information.
```

> 注意：PyPi 服务遭受 XMLRPC 滥用，PyPi 将不再支持 pip search 服务

我们还可以参考 PyPI 官网提供的[官方 Python 包索引](https://pypi.org/search)来搜
索。

## 2.5 虚拟环境和 Git

我们不需要在版本控制中对虚拟环境中的内容进行跟踪。

1. 在我们的仓库之外创建虚拟环境
2. 不要将虚拟环境目录纳入版本控制系统的控制范围内

在 .gitignore 文件中加入当前虚拟环境

```.gitignore
venv/
```

### 2.5.1 shebang

shebang 是 Python 文件顶部的一个特殊命令，通过它我们可以直接执行 Python 文件：

```python
#!/usr/bin/env python3
print('Hello, world!')
```

### 2.5.2 文件编码

自 Python 3.1 开始，所有的 Python 文件都使用 UTF-8 编码，以允许编辑器使用
Unicode 中的所有字符。

如果我们需要使用一个不同的编码系统，需要告诉 Python 解释器。

比如，要在 Python 文件中使用 Latin-1 编码，我们需要将这行代码放在文件的顶部，紧
跟在 shebang 下面：

```python
# -*- coding: latin-1 -*-
```

如果你指定了 Python 无法识别的编码，它将抛出一个错误。

我们也可以通过下面这行代码告诉解释器当前使用的编码格式：

```python
# coding: latin-1
```

## 2.6 一些额外的关于虚拟环境的小贴士

### 2.6.1 不激活虚拟环境的情况下使用虚拟环境

我们可以在不激活虚拟环境的情况下使用虚拟环境的二进制文件。例如，我们可以直接执行
venv\bin\python 来运行虚拟环境自己的 Python 实例，或者执行 venv\bin pip 来运行虚
拟环境自己的 pip 实例。这样做的效果与激活虚拟环境后的效果相同。

### 2.6.2 一些替代品

我们使用 pip 和 venv。还有一些其他的解决方案值得一看。

#### 2.6.2.1 Pipenv

Pipenv 是一款将 pip 和 venv 结合在一起而成的一个整体的工具，具有许多额外的功能。
工作流程和 pip 与 venv 有很大的不同，可以查看官方文档学习。

#### 2.6.2.2 pip-tools

#### 2.6.2.3 poetry

## 2.7 认识 PEP 8

### 2.7.1 行款限制的历史债务

PEP8 推荐的行款限制为 79 或 80 个字符。

### 2.7.2 制表符还是空格

PEP8 推荐使用空格而不是制表符。永远不要混用两种。

## 2.8 代码质量控制：静态分析工具

通用类型的静态分析器成为 linter，它可以检查代码中存在的常见错误、潜在隐患，以及
代码风格的不一致性。在 Python 社区中，最受欢迎的两个 linter 是 Pylint 和
Flakes。

Python 社区中还有非常多的静态分析工具，包括静态类型检查器（如 Mypy）和复杂度分析
器（如 mccabe）。

### 2.8.1 Pylint

使用 pip 安装 Pylint 包，建议在虚拟环境中安装这个包。安装完成后，可以想 Pylint
传递我们想要分析的文件的名称，如下所示：

```bash
pylint filetocheck.py
```

我们也可以分析整个包或模块。例如，我们想让 Pylint 分析当前工作目录中名为
myawesomeproject 的包，可以运行以下命令：

```bash
pylint myawesomeproject
```

我们可以编写一个 Python 文件尝试使用 Pylint 进行静态分析：

```python
def cooking():
    ham = True
    print(eggs)
    return order
```

执行 pylint 分析：

```bash
python -m pylint .\cooking.py
```

输出结果：

```bash
************* Module cooking
cooking.py:4:0: C0304: Final newline missing (missing-final-newline)
cooking.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cooking.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
cooking.py:3:10: E0602: Undefined variable 'eggs' (undefined-variable)
cooking.py:4:11: E0602: Undefined variable 'order' (undefined-variable)
cooking.py:2:4: W0612: Unused variable 'ham' (unused-variable)

-----------------------------------
Your code has been rated at 0.00/10
```

我们还可以在 Python 文件中禁用 pylint 的一些规则：

```python
# pylint: disable=missing-module-docstring

def cooking():  # pylint: disable=missing-function-docstring
    ham = True
    print(eggs)
    return order
```

再次执行 pylint 进行分析：

```bash
************* Module cooking
cooking.py:6:0: C0304: Final newline missing (missing-final-newline)
cooking.py:5:10: E0602: Undefined variable 'eggs' (undefined-variable)
cooking.py:6:11: E0602: Undefined variable 'order' (undefined-variable)
cooking.py:4:4: W0612: Unused variable 'ham' (unused-variable)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)
```

我们可以通过在项目的根目录中创建一个 pylintrc 文件来控制 Pylint 在项目范围内的行
为。要这样做，运行以下命令：

```bash
python -m pylint --generate-rcfile > pylintrc
```

我们后续可以编辑这个文件以打开和关闭不同的告警、忽略文件和定义其他设置。

当我们运行 pylint 是，它将当前工作目录中查找 pylintrc（或.pylintrc）文件。或者，
我们也可以通过在调用 Pylint 时传递文件名给 `--rcfile` 选项，从而指定一个不同的文
件名，让 Pylint 从中读取设置，命令如下：

```bash
python -m pylint --rcfile=myrcfile filetocheck.py
```

如果执行上述命令遇到以下报错：

```bash
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
```

可对 pylintrc 文件的编码格式更新为 UTF-8，因为该文件的默认格式可能为 UTF-16，而
Pylint 模块默认使用 UTF-8 编码去读取该文件。

Pylint 用户喜欢在他们的主目录中创建 .pylintrdc 或 .config/pylintrc 文件。如果
Pylint 找不到另一个配置文件，将使用主目录中的那个。

### 2.8.2 Flake8

Flake8 工具实际上是以下 3 个静态分析器的组合。

- PyFlakes 是一个 linter，与 Pylint 相似，旨在更快地工作并避免误报。
- pycodestyle 是一个风格检查器，可以帮助我们确保我们编写符合 PEP8 的代码。
- mccabe 用于检查代码的 McCabe 复杂性。它的作用只是在我们的代码结构变得太复杂时
  警告我们。

我们可以使用 pip 安装 Flake8 包，我们通常在虚拟环境中这样做。

为了扫描文件、模块或包，请将器传递给 flake8 命令行。例如，要扫描之前的
cooking.py 文件，可以使用以下命令：

```bash
python -m flake8 .\cooking.py
```

输出内容如下：

```bash
.\cooking.py:4:5: F841 local variable 'ham' is assigned to but never used
.\cooking.py:5:11: F821 undefined name 'eggs'
.\cooking.py:6:12: F821 undefined name 'order'
.\cooking.py:6:17: W292 no newline at end of file
```

默认情况下，命令 glake8 只运行 PyFlakes 和 pycodestyle。如果要分析代码的复杂性，
则需要传递参数 `--max-complexity`，参数名后跟一个表示代码复杂程度的数字。

Flake8 还支持配置文件。在项目目录中，我们可以创建一个 .flake8 文件。该文件中的内
容以 `[flake8]` 开头，然后使我们想要定义的所有 Flake8 设置。

例如，我们想要在每次调用 Flake8 时自动运行 mccabe，而不是每次都指定
`--max-complexity`，我们可以定义一个.flake8 文件，如下所示：

```txt
[flake8]
max-complexity = 10
```

### 2.8.3 Mypy

Mypy 是一个不同寻常的静态分析器，因为它完全专注于类型注释。

## 2.9 代码风格守护者：自动格式化工具

### 2.9.1 autopep8


### 2.9.2 Black