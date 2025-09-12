# 第 18 章 Django 入门

## 18.1 建立项目

### 18.1.1 定制规范

### 18.1.2 建立虚拟环境

**虚拟环境**是系统的一个位置，可在其中安装包，并将这些包与 Python 其他包隔离开来。

为项目新建一个目录，将其命名为 learning_log，再在终端中切换到这个目录，并执行以下命令创建一个虚拟环境：

```bash
python -m venv ll_env
```

这里运行了模块 venv ，并使用它创建一个名为 ll_env 的虚拟环境。

### 18.1.3 激活虚拟环境

现在需要使用下面命令激活虚拟环境

```bash
.\ll_env\Scripts\activate
```

当环境处于激活状态时，环境名将包含在括号内，这意味着可在环境中安装和使用已安装的包。

要停止使用虚拟环境，可执行 deactive 命令：

```bash
deactivate
```

如果关闭运行虚拟环境的终端，虚拟环境也将不再处于活动状态。

### 18.1.4 安装 Django

激活虚拟环境后，执行如下命令来更新 pip 并安装 Django：

```bash
pip install --upgrade pip
```

如果升级 pip 时遇到如下报错

```bash
ERROR: To modify pip, please run the following command:
\python-crash-course\chapter-18\learning_log\ll_env\Scripts\python.exe -m pip install --upgrade pip
```

建议使用如下方式更新：

```bash
python -m pip install --upgrade pip
```

此处的 python 使用的是当前激活虚拟环境中的 python.exe。

可使用如下命令查看当前虚拟环境安装了哪些包：

```bash
pip list
```

输出如下：

```bash
Package Version
------- -------
pip     25.2
```

安装 Django：

```bash
pip install django
```

执行 pip list 查看现在虚拟环境安装了哪些包

```bash
Package  Version
-------- -------
asgiref  3.9.1
Django   5.2.6
pip      25.2
sqlparse 0.5.3
tzdata   2025.2
```

pip 从各种地方下载资源，因此升级频繁，有鉴于此，每当我们搭建新的虚拟环境后，都最好更新 pip。

由于现在是在虚拟环境中工作，因此不管使用什么系统，安装 Django 的命令都相同：不需要指定标志--user，也无须使用像 python -m pip install package_name 这样较长的命令。别忘了，Django 仅在虚拟环境 ll_env 处于活动状态时才可用。

### 18.1.5 在 Django 中创建项目

在虚拟环境出于活跃状态下，执行如下命令新建一个项目：

```bash
django-admin startproject ll_project .
```

再执行 ls 可查看当前目录下都有哪些内容：

```bash
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/9/12     21:07                ll_env
d-----         2025/9/12     21:28                ll_project
-a----         2025/9/12     21:28            688 manage.py
```

命令 startproject 让 Django 新建一个名为 ll_project 的项目。这个命令末尾的句点让新项目使用合适的目录结构，这样在开发完后可轻松地将应用程序部署到服务器上。

startproject 还生成了一个 manage.py 程序，这是一个简单的程序，接收命令并将其交个 Django 的相关部分。我们将使用这些命令管理使用数据库和运行服务器等程序。

目录 ll_project 包含四个文件，其中最重要的是 settings.py、urls.py 和 wsgi.py。文件 settings.py 指定 Django 如何与系统交互以及如何管理项目。在开发项目的过程中，我们将修改其中的一些设置，并添加一些设置。文件 urls.py 告诉 Django，应创建哪些网页来响应浏览器请求。文件 wsgi.py 帮助 Django 提供它创建的文件，名称是 Web Service Gate Interface（Web 服务器网关接口）的首字母缩写。

### 18.1.6 创建数据库

Django 将大部分与项目相关的信息存储在数据库中，因此需要创建一个供 Django 使用的数据库。我们需要在虚拟环境下执行以下命令来常见数据库：

```bash
python manage.py migrate
```

我们将修改数据库称为迁移数据库。首次执行 migrate 将让 Django 确保数据库与项目的当前状态匹配。

### 18.1.7 查看项目

下面来核实 Django 正确地创建了项目。为此，可使用命令 runserver 查看项目的状态：

```bash
python manage.py runserver
```

Django 启动了一服务器，让我们能够查看系统中的项目，了解它的工作情况。

## 18.2 创建应用程序

Django 项目由一些列应用程序组成，它们协同工作让项目成为一个整体。本章只创建一个应用程序，它将完成项目里的大部分工作。

```bash
python manage.py startapp learning_logs
```

命令 startapp appname 让 Django 搭建应用程序所需的基础设施。我们使用 ls 查看 learning_logs 下生成哪些文件？

```bash
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2025/9/12     22:05                migrations
-a----         2025/9/12     22:05             66 admin.py
-a----         2025/9/12     22:05            163 apps.py
-a----         2025/9/12     22:05             60 models.py
-a----         2025/9/12     22:05             63 tests.py
-a----         2025/9/12     22:05             66 views.py
-a----         2025/9/12     22:05              0 __init__.py
```

我们使用 models.py 来定义要在应用程序中管理的数据。

### 18.2.1 定义模型

打开 models.py ：

```python
from django.db import models

# Create your models here.
```

这里导入了 models 模块，并让我们创建自己的模型。模型告诉 Django 如何处理应用程序中存储的数据。模型就是一个类，包含属性和方法。下面是用户将存储的主题的模型：

```python
from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型中的字符串表示"""
        return self.text
```

这里创建了一个 Topic 类，它继承了 Model，即 Django 中定义了模型基本功能的类。我们给 Topic 类添加了两个属性：text 和 date_added。

属性 text 是一个 CharField - 由字符组成的数据，即文本。当需要存储少量文本时，可使用 CharField。在定义 CharField 属性时，必须告诉 Django 该在数据库中预留多少空间。这里将 max_length 设置为 200（即 200 个字符），这对于存储大多数主题名来说足够了。

属性 date_added 是一个 DateTimeField - 记录日期和时间的数据。我们传递实参 auto_now_added=True，每当用户创建新主题时，Django 都会将这个属性自动设置为当前的日期和时间。

最好告诉 Django 我们希望它如何表示模型的实例。如果模型有 `__str(self)__` 方法，那么每当需要生成表示模型实例的输出时，Django 将调用这个方法。

要了解 Django 模型中使用的各个字段，请参阅 _Django Model Field Reference_。

### 18.2.2 激活模型

要使用这些模型，必须让 Django 将前述应用程序包含到项目中。为此，打开 settings.py ，其中有个片段告诉 Django，哪些应用程序被安装到乐项目中：

```python

```
