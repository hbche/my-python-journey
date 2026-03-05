# 第 1 章 文件自动化处理

目标：

- 使用 Python 在硬盘上创建、读取和保存文件
- 文件路径识别、处理、文件夹的操作理论学习
- 文件自动化处理实践
- 邮件自动发送理论学习，使用 Python 发送邮件附带 excel 附件

## 1.1 文件处理

### 1.1.1 文件与文件路径

os 常用的操作函数如下：

| 函数     | 说明                                                        |
| -------- | ----------------------------------------------------------- |
| join     | 将多个文件组合起来，以字符串中含有\/的第一个路径开始拼接    |
| getctime | 返回文件或者目录的创建时间                                  |
| getatime | 访问时间，读一次文件的内容，这个时间就会更新                |
| getmtime | 修改时间，修改一次文件的内容，这个时间就会更新              |
| getsize  | 获取文件大小                                                |
| isabs    | 如果 path 是绝对路径，则返回 True                           |
| exists   | 如果 path 存在，则返回 True；如果 path 不存在，则返回 False |
| isdir    | 如果 path 是一个存在的目录，则返回 True，否则返回 False     |
| isfile   | 如果 path 是一个存在的文件，则返回 True，否则返回 False     |

### 1.1.2 当前的工作目录

每当运行在计算机上的程序时，都有一个 “当前工作目录”。利用 `os.getcwd()` 函数，可
以取得当前工作路径的字符串，并可以使用 `os.chdir()` 改变它。

```py
import os

print(os.getcwd())  # 获取当前工作目录，即执行该代码的文件的所在路径

os.chdir('E:\\my-python-journey\\python-for-automated-office-work')   # 改变当前工作目录
print(os.getcwd())  # E:\my-python-journey\python-for-automated-office-work
```

### 1.1.3 路径操作

#### 1.1.3.1 绝对路径和相对路径

- 绝对路径：从根文件夹开始
- 相对路径：相对于程序的当前目录

相对路径中，单个句点`.`表示当前目录的缩写，两个句点`..`表示当前父文件夹。

相对路径和绝对路径常用的几个函数：

- `os.path.abspath(path)`：将相对路径转换为绝对路径，并返回参数的绝对路径的字符
  串。
- `os.path.isabs(path)`：判断是否是绝对路径，是则返回 True，否则返回 False。

#### 1.1.3.2 路径操作

- `os.path.relpath(path, start)`：返回从 start 路径到 path 的相对路径的字符串。
  如果没有提供 start，就使用当前工作目录作为开始路径。
- `os.path.dirname(path)`：返回当前路径的目录名称。
- `os.path.basename(path)`：返回当前路径的文件名称。

如果同时需要一个路径的目录路径和文件名称，可以使用 `os.path.split(path)`，获得这
两个字符串的元组。

如果想获取路径中的每个文件夹和文件名，需要调用 `path.split(os.path.sep)`，使用
`os.path.sep`对文件路径字符串进行分割。

#### 1.1.3.3 路径有效性检查

如果提供的路径不存在，很多 Python 函数就会崩溃并报错。`os.path`提供了一些函数，
用于检查给定的路径是否存在，以及判定是文件还是文件夹。

- `os.path.exists(path)`：如果 path 参数所指的文件或文件夹存在，则返回 True,否则
  返回 False。
- `os.path.isfile(path)`：如果 path 参数存在，并且是一个文件，则返回 True,否则返
  回 False。
- `os.path.isdir(path)`：如果 path 参数存在，并且是一个文件夹，则返回 True,否则
  返回 False。

### 1.1.4 文件及文件夹操作

#### 1.1.4.1 用 `os.makedirs()`创建新文件夹

> `os.makedirs()`会接连创建路径中的中间路径

```py
import os

os.makedirs("D:\\Datewhale\\practice")  # 查看目录，已创建，若文件夹已存在，不会覆盖，会报错
```

#### 1.1.4.2 查看文件大小和文件内容

- `os.listdir(path)`：返回文件名字符串的列表，包含 path 参数中的每一个文件。
- `os.path.getsize(path)`；返回 path 参数中文件的字节数。

```py
import os

print(os.listdir(os.getcwd()))
```

### 1.1.5 文件读写过程

读写文件的 3 个步骤：

1. 调用 `open()`函数，返回一个 File 对象。
2. 调用 File 对象的 `read()` 和 `write()` 方法。
3. 调用 File 对象的 `close()` 方法，关闭该文件。

open 函数中常见的对象方法说明：

| 方法       | 说明                                           |
| ---------- | ---------------------------------------------- |
| read       | 将文件读入字符串中，也可以读取指定字节         |
| readline   | 读入文件的一行到字符串中                       |
| readlines  | 将这个文件按照行读取到字符串列表中             |
| write      | 向文件写入字符串                               |
| writelines | 向文件写入一个行数据列表                       |
| close      | 关闭文件                                       |
| flush      | 把缓冲区的内容写入硬盘                         |
| tell       | 返回文件操作标记的当前位置，以文件的开头为原点 |
| next       | 返回下一行，并把文件操作标记位移到下一行       |
| seek       | 移动文件指针到指定位置                         |
| truncate   | 截断文件                                       |

#### 1.1.5.1 用 open 函数打开文件

文件对象可以通过 Python 内置的 open 函数得到，完整的语法如下：

```py
open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

open 函数有 8 个参数
