# 第 3 章 语法速成

## 3.1 "Hello, world!"程序

调用 print() 函数将文本写入控制台，数据作为参数被传递给字符串，并用引用包裹。我
们可以传递任何类型的数据，它将在控制台输出。

```py
print("Hello, world")
```

同样可以使用 input() 函数从控制台获取数据：

```py
name = input("What is your name?")
print("Hello, " + name)
```

## 3.2 语句和表达式

每一行 Python 代码都是一个语句，以换行符结尾。

如果一段代码的结果是单一的值，那么这段代码称为表达式。

```py
message = "Hello, world!"
print(message)
```

如果需要在同一行中放置多个语句，可以使用分号（;）将他们隔开。但是不值得提倡。

```py
message = 'Hello, world!';print(message)
```

## 3.3 空格的重要性

## 3.4 空语句

## 3.5 注释以及文档字符串

## 3.6 声明变量

## 3.7 数学操作

## 3.8 逻辑操作

## 3.9 字符串

## 3.10 函数

## 3.11 类和对象

## 3.12 异常处理

## 3.13 元组和列表

## 3.14 循环

## 3.15 结构模式匹配

## 3.15.1 文本模式与通配符

```py
lunch_order = input("What wolud you like for lunch?")

match lunch_order:
    case "pizza":
        print("Pizza time!")
    case "sandwich":
        print("Here's your sandwich")
    case 'taco':
        print("Taco, taco, TACO, tacotacotaco!")
    case _:
        print("Yummy.")
```

一旦匹配上匹配项，就运行相应 case 的套件，然后匹配语句就结束了；一旦匹配到一个值
，就不再检查它与其他模式是否匹配。

最后一个 case 中的下划线（`_`）是通配符，它将匹配任何值。这称为回退 case，，必须
放在最后，因为它将匹配任何内容。

### 3.15.2 or 模式

可能有一种使用场景需要覆盖多个可能的值。一种方式是使用 or 模式，其中多种字面量值
之间使用竖线分隔：

```py
lunch_order = input("What wolud you like for lunch?")

match lunch_order:
    case 'taco':
        print("Taco, taco, TACO, tacotacotaco!")
    case 'salad' | 'soup':
        print("Eating healthy, eh?")
    case _:
        print("Yummy.")
```

### 3.15.3 捕获模式

结构模式匹配功能的一个非常有用的地方是能够捕获主题的一部分或全部。例如，在上述例
子中，回退 case 只输出 “Yummy.”。这并没有多大帮助。相反，如果有一条默认的消息来
宣布用户的选择。为了实现这一点，我们写一个捕获模式。

```py
lunch_order = input("What wolud you like for lunch?")

# 捕获模式
match lunch_order:
    case 'salad' | 'soup':
        print("Eating healthy, eh?")
    case order:
        print(f"Enjoy your {order}.")
```

这个模式的作用类似于通配符，只是 lunch_order 的值被捕获到 order 中了。现在无论用
户输入什么，如果它与前面的任何模式都不匹配，那么它的值将被捕获并在这里显示。

捕获模式不仅仅可以捕获整个值，还可以编写一个匹配元组或列表的模式，然后只捕获该元
组或列表的一部分：

```py

```
