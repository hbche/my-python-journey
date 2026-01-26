# Python 学习笔记

以下是 Python 编程学习

## 基础

### Python 开发环境

#### Python 安装

#### Python 解释器

##### 交互式会话

##### 运行 Python 文件

```bash
python your_program.py
```

#### 包和虚拟环境

##### 创建一个虚拟环境

```bash
python -m venv virtual_name
```

其中 -m 表示调用 Python 的模块，venv 是 -m 对应的模块，virtual_name 是我们指定的
虚拟环境名

##### 激活虚拟环境

```bash
# Linux
source venv/bin/activate
# Windows
.\Scripts\activate.bat
# Windows ps
.\Scripts\activate.ps1
```

##### 退出虚拟环境

```bash
# Linux
deactivate
# Windows
.\Scripts\deactivate.bat
```

#### pip 介绍

##### 系统范围内的包

##### 安装包

```bash
python -m pip install package
python -m pip install package==version
python -m pip install package>=version
```

##### requirements.txt

```bash
# 通过 requirements.txt 在虚拟环境中安装依赖包
python -m pip install -r requirements.txt
```

##### 更新包

```bash
# 更新指定的包
python -m pip install --upgrade package
# 通过 requirements.txt 文件更新包
python -m pip install --upgrade -r requirements.txt
```

##### 卸载包

```bash
python -m pip uninstall package
```

> 卸载指定包时，该包所依赖的包在安装时会一并安装，但是在卸载时是不会被卸载的，所
> 以此时虚拟环境就发挥大作用了。一旦我们陷入这种困境，我们可以删除虚拟环境，再创
> 建一个新的虚拟环境，然后只安装所需要的包即可。

##### 搜索包

```bash
python -m pip search web scraping
```

#### 代码质量控制：静态分析工具

##### Pylint

##### Flake8

##### Mypy

#### 代码风格守护者：自动格式化工具

##### autopep8

##### Black

### 变量和数据类型

#### 变量

1. 在使用变量之前必须先定义变量，否则将会报错
2. 不要更改变量中存储的数据的类型，即使是替换值也是如此
3. Python 是一种强类型语言，这意味着我们不能将不同类型的数据组合在一起
4. Python 是弱绑定的，因此可以将不同类型的值分配给现有变量。但是不建议这样做
5. Python 没有任何正式定义的常量，只是建议使用全大写和下划线的命名方式来指示变量
   作为常量来使用

#### 数字类型

1. 整数
2. 浮点数
3. 复数

#### 运算符

##### 算数运算

| 运算符      | 说明                       | 示例                           |
| ----------- | -------------------------- | ------------------------------ |
| +、-、\*、/ | 分别对应加减乘除计算       | `7 / 4 = 1.75`                 |
| %           | 取余运算                   | `-7 % 4 = 1` 和 `-7 % -4 = -3` |
| \*\*        | 平方运算                   | `7 ** 2 = 49`                  |
| //          | 整除运算，直接丢弃小数部分 | `7 // 4 = 1`                   |

##### 位运算

| 运算符 | 说明   | 示例         |
| ------ | ------ | ------------ |
| &      | 与操作 | `9 & 8 = 8`  |
| \|     | 或操作 | `9 \| 8 = 9` |
| ^      | 异或   | `9 ^ 8 = 1`  |

### 函数

### 类

### 异常处理

### 集合与迭代

### 文本输入输出和上下文管理

## 进阶

### 自省与泛型

### 异步和并发

### 线程和并行
