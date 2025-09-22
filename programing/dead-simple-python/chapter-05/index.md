# 第 5 章 变量和数据类型

## 5.1 Python 中的变量：名称和值

Python 使用 name 这个术语来指代传统的变量。一个 name 指向一个 value 或 object（
对象）​，就像我们的名字指向我们一样。可能有多个 name 指向同一个 value，就像我们
可能有一个名字和一个昵称。一个 value 是内存中一个特定的数据实例。​“变量”这个术语
指代这两者的组合：一个 name 指向一个 value。

## 5.2 赋值

```python
# 变量复制
answer = 42
insight = answer
```

answer 这个名称被绑定到值 42 上，也就是说，这个名称现在可以用来指代内存中的值。
这个绑定的操作称为赋值。接下来把变量 answer 赋值给新的变量 insight。insight 这个
名称并没有指向值的副本，而是指向一同一个原始值。

```bash
answer   ──┐
           |--> 42
insight  ──┘
```

在内存中，名称 insight 被绑定到值 42 上，这个值已经被另一个名称 answer 绑定了。
两个名称都可以继续使用。更重要的是，insight 并没有被绑定到 answer 上，而是被绑定
到了 answer 所指向的值上。一个名称总是指向一个值。

is 运算符，它比较的是两个名称所绑定的值在内存中的位置。这意味着 is 不会检查两个
名称是否指向相等的值，而是检查它们是否指向内存中的同一个值。

```bash
answer = 42
insight = answer
insight is aswer    # True
```

当我们执行赋值操作时，Python 会在背后最初自己的决定：是创建一个新的值，还是绑定
到一个已经存在的值。

```python
spam = 123456789
maps = spam
eggs = 123456789
print(spam == maps)     # True
print(spam == eggs)     # True
print(spam is maps)     # True
print(spam is eggs)     # False
```

名称 spam 和 maps 都被绑定到内存中的同一个值，但是 eggs 可能被绑定到了一个不同但
相等的值。因此，spam 和 eggs 不共享一个身份。

```bash
spam ──┐
       |--> 123456789
maps ──┘

eggs -----> 123456789
```

```python
answer = 42
insight = 42
print(answer is insight)    # True
```

当把 42 赋值给 insight 时，Python 决定把这个名称绑定到已经存在的值。现在，answer
和 insight 都被绑定到内存中的同一个值，因此它们共享一个身份。

这就是为什么身份运算符（is）会让人觉得奇怪。在很多情况下，is 的行为与比较运算符
（==）类似。

最后要注意的是，内置函数 id()返回一个整数来表示传递给它的任何东西的身份。这些整
数就是 is 运算符所要比较的值。如果对 Python 如何处理名称和值感兴趣，不妨试着使用
一下 id()函数。

## 5.3 数据类型

### 5.3.1 type() 函数

如果想知道一个值的类型，可以使用 Python 内置的 type() 函数。Python 中一切都是对
象，所以这个函数实际上只会返回值是哪个类的实例：

```python
# 使用 tpye() 函数获取某个变量的类型信息
answer = 42
print(type(answer))     # <class 'int'>
```

可以将 type() 函数和 is 表达式配合使用：

```python
# 使用 tpye() 函数获取某个变量的类型信息
answer = 42
print(type(answer))     # <class 'int'>

if type(answer) is int:
    # 判断 answer 的类型是否是 int
    print("What's the question?")       # What's the question?
```

当需要对某个变量进行类型检测时，最好使用 isinstance() 而不是 type()，因为
isinstance() 函数考虑了子类和继承。该函数返回 True 或 False，其可以用作 if 语句
中的条件：

```python
# 使用 tpye() 函数获取某个变量的类型信息
answer = 42
print(type(answer))     # <class 'int'>

if isinstance(answer, int):
    # 判断 answer 的类型是否是 int
    print("What's the question?")       # What's the question?
```

### 5.3.2 鸭子模型

如果它看起来像鸭子，走起路来像鸭子，叫起来也像鸭子，那么它可能就是一只鸭子。

Python 并不关心值的数据类型是什么，而关心值的数据类型的功能。例如，如果一个对象
支持所有的数学运算符和函数，并且接收浮点数和整数作为二元运算符的操作数，那么
Python 就会认为这个对象是数值类型。

## 5.4 作用域和垃圾回收

### 5.4.1 局部作用句以及引用计数垃圾回收器

```python
def smap():
    message = 'Spam'
    word = 'spam'
    for _ in range(100):
        # 循环没有局部作用域，因此在循环外部也能访问 separator
        seperator = ', '
        message += seperator + word
    message += seperator
    message += 'spam!'

    return message
```

以上代码创建了一个 spam()函数，其中定义了名称 message、word 和 separator。可以在
函数内部访问这些名称中的任何一个，这就是它们的局部作用域。循环没有自己的作用域，
因此 separator 的定义无关紧要，可以在循环外部访问它。

```python
def smap():
    message = 'Spam'
    word = 'spam'
    for _ in range(100):
        # 循环没有局部作用域，因此在循环外部也能访问 separator
        seperator = ', '
        message += seperator + word
    message += seperator
    message += 'spam!'

    return message

print(message)      # NameError: name 'message' is not defined
```

尝试在定义 message 的 spam()函数的上下文之外访问 message 会引发 NameError。

### 5.4.2 解释器关闭

当 Python 解释器被要求关闭时，例如当 Python 程序终止时，将进入解释器关闭阶段。在
这个阶段，解释器将释放所有分配的资源、多次调用垃圾回收器并触发对象中的析构函数。

### 5.4.3 全局作用域

当一个名称在模块内部而不在任何函数、类或列表推导式中定义时，可以认为这个名称拥有
全局作用域。

```python
high_score = 10

def score():
    new_score = 465
    if new_score > high_score:     # UnboundLocalError: cannot access local variable 'high_score' where it is not associated with a value
        print("New high score")
        # 更新 high_score
        high_score = new_score

score()
print(high_score)
```

当我们执行这段代码时，Python 会提示你在赋值之前就使用了一个局部变量。问题在于，
以上代码是在 score()函数的作用域中给 high_score 赋值的，这会使全局名称
high_score 被新的局部名称 high_score 覆盖。在函数中的任何地方创建局部名称
high_score 都会使函数无法“看到”全局名称 high_score。

为了让代码正常工作，需要声明你将在局部作用域中使用全局名称，而不是定义一个新的局
部名称。使用 global 关键字可以做到这一点，

```python
high_score = 10

def score():
    # 声明high_score为外部的全局变量high_score，而不是函数内部的局部变量
    global high_score
    new_score = 465
    if new_score > high_score:
        print("New high score")
        # 更新 high_score
        high_score = new_score

score()
print(high_score) # 465
```

在函数中做其他事情之前，必须声明正在使用全局名称 high_score。这意味着在 score()
中，无论在何处给 high_score 赋值，都会使用全局名称，而不是试图创建一个新的局部名
称。代码现在能按预期工作了。

每当我们想在局部作用域中重新绑定一个全局名称时，必须先使用 global 关键字。如果只
是访问一个全局名称指向的当前值，则不需要使用 global 关键字。

```python
current_score = 0

def score():
    new_score = 465
    current_score = new_score

score()
print(current_score)        # 0
```

上述代码虽然能够正常运行，但是并不符合我们的预期。

```python
current_score = 0

def score():
    # 声明此处是全局变量，不是函数内部新声明的局部变量
    global current_score
    new_score = 465
    current_score = new_score

score()
print(current_score)        # 0
```

以上代码指定了在 score()函数中使用全局名称 current_score，代码按预期工作。

### 5.4.4 全局作用域的注意事项

关于全局作用域，还有一个重要问题需要注意。在全局作用域中修改任何变量，比如在函数
外部重新绑定或改变一个名称，有可能导致令人困惑的行为和令人惊讶的 bug——特别是当你
开始处理多个模块的时候。可以在全局作用域中“声明”一个名称，然后在局部作用域中重新
绑定和改变这个全局名称。

### 5.4.5 nonlocal 关键字

Python 允许在一个函数中实现另一个函数。下面展示函数嵌套对作用域的影响：

```python
spam = True

def order():
    eggs = 12

    def cook():
        nonlocal eggs

        if spam:
            print("Spam!")

        if eggs:
            eggs -= 1
            print("...and eggs.")

    cook()

order()
```

order()函数中包含 cook()函数，每个函数都有自己的作用域。

请记住，只要一个函数只访问全局变量名称（如 spam）​，就不需要做任何特殊的事情。然
而，尝试给一个全局名称重新赋值会导致一个新的局部名称被定义，这个局部名称会覆盖全
局名称。内部函数使用定义在外部函数中的名称时也如此，这称为嵌套作用域或封闭作用域
。 为了解决这个问题，可以指定 eggs 的作用域为 nonlocal，这意味着可以在封闭作用域
（而不是局部作用域）中找到它。内部函数 cook()可以很好地访问全局名称 spam。

nonlocal 关键字从最内层的封闭作用域开始查找指定的名称，如果没有找到，则移动到外
层的封闭作用域继续查找。重复这个过程，直至找到这个名称，或者确定这个名称在非全局
的封闭作用域中不存在。

### 5.4.6 作用域解析

Python 中关于搜索名称的作用域和顺序的规则称为作用域解析。作用域解析的顺序：

- Local: 局部作用域
- Enclosing-function locals: 外部函数的局部作用域
- Global: 全局作用域
- Built-in: 内置作用域

### 5.4.7 关于类的一些特殊情况

类有一套独立的处理作用域的流程。从技术上讲，类不会直接影响作用域解析顺序。每个直
接声明在类中的名称都是这个类的属性（attribute）​，可以通过对类名（或对象名）使用
点（.）运算符来访问。

```python
class Nutrimatic:
    output = 'Something almost, but not quite, entirely unlike tea.'

    def request(self, beverage):
        return self.output

machine = Nutrimatic()
mug = machine.request('Tea')
print(mug)      # Something almost, but not quite, entirely unlike tea.

print(machine.output)       # Something almost, but not quite, entirely unlike tea.
print(Nutrimatic.output)    # Something almost, but not quite, entirely unlike tea.
```

### 5.4.8 分代垃圾回收器

## 5.5 不可变的真相

Python 中的值分为不可变的值和可变的值。两者的区别在于能否在原地修改，这也意味着
它们在内存中是能够改变的。

不可变的值不能在原地修改。例如，整数（int）​、浮点数（float）​、字符串（str）和
元组（tuple）都是不可变的。如果尝试修改一个不可变的值，则会得到一个完全不同的值

```python
eggs = 12
carton = eggs
print(eggs is carton)   # True
eggs +=1
print(eggs is carton)   # False
print(eggs)             # 13
print(carton)           # 12
```

我们再来看一组可变对象：

```python
temps = [87, 76, 79]
highs = temps
print(temps is highs) # True
temps += [81]
print(temps is highs) # True
print(highs)          # [87, 76, 79, 81]
print(temps)          # [87, 76, 79, 81]
```

## 5.6 赋值传递

Python 使用的是值传递还是引用传递？

两者都不是。更准确地说，Python 使用的是赋值传递。

值和绑定到它们的名称都不会被移动。相反，每个值都通过赋值被绑定到参数。

```python
def greet(person):
    print(f"Hello, {person}.")

my_name = "Jason"
greet(my_name)
```

在以上代码中，内存中只有字符串"Jason"的一个副本，它被绑定到 my_name。当把
my_name 传给 greet()函数，具体来说是传给 person 参数时，值就通过赋值被绑定到参数
，即 person =my_name。

再次强调，赋值不会复制值。名称 person 现在被绑定到值 "Jason"。

赋值传递的概念在我们刚开始使用可变值（如列表）时会变得棘手。为了演示这种经常出现
的意外行为，编写一个函数：

```python
def find_lowest(temperatures):
    temperatures.sort()
    print(temperatures[0])
```

乍看上去，我们可能会假设在将列表传递给 temperatures 参数时会创建一个副本，所以如
果修改了绑定到参数的值不会对原列表造成影响。然而，列表是可变的，这意味着列表本身
的值可以被修改：

```python
temps = [85, 76, 79, 72, 81]
find_lowest(temps)
print(temps)        # [72, 76, 79, 81, 85]
```

当把 temps 传递给函数的 temperatures 参数时，实际上只是为列表创建了一个别名
（alias）​，所以对 temperatures 所做的任何更改都可以从绑定到同一列表的所有其他名
称中看到，这个改变可以从 temps 中看到。

当 find_lowest()对传递给 temperatures 的列表进行排序时，实际上是对 temps 和
temperatures 引用的可变列表进行排序。这是一个函数有副作用的典型例子，即对函数调
用之前存在的值进行更改。

通常，函数不应该有副作用，即任何作为参数传递给函数的值都不应该被直接更改。为了避
免改变原始值，必须显式地对原始值进行复制

```python
def find_lowest(temperatures):
    # 使用 sorted 对原始列表排序并返回新的列表，不修改原始列表
    sorted_temps = sorted(temperatures)
    print(sorted_temps[0])

temps = [85, 76, 79, 72, 81]
find_lowest(temps)
print(temps)        # [85, 76, 79, 72, 81]
```

sorted()函数没有副作用，它使用传递给它的列表中的项创建了一个新列表。

## 5.7 集合和引用

所有的集合（包括列表）都使用了一个巧妙的技术细节：集合中的元素是引用。

```python
# 通过生成二维数组，生成棋盘
board = [["*"] * 3] * 3

# 模拟第一个子
board[1][0] = 'X'

# 打印棋盘
for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")

# 结果：
# X * *
# X * *
# X * *
```

我们发现通过 \* 运算符生成的二维数组，第二个维度 —— 3 个`[["-"] * 3]` 列表的副本
。

在最开始，我们创建了一个包含 3 个 "-" 字符串的列表。字符串由于是不可变的，因此不
能在原地修改，这符合预期。将列表中的第一项重新绑定到 "X" 不会影响其他两项。

外层的列表由 3 个列表项组成。因为定义了一个列表项并使用了 3 次，所以现在一个可变
列表项有 3 个名称！使用一个引用来改变某个列表项的值，会改变这 3 个名称共享的值，
于是所有 3 个引用都可以看到这个变化。

有几种方法可以解决这个问题，都是通过确保每一行都引用一个单独的值来实现的：

```python
board = [['*'] * 3 for _ in range(3)]
```

只需要改变最初定义游戏棋盘的方式即可。这一次使用列表推导式来创建行。简而言之，这
个列表推导式将 3 次使用 ["-"] \* 3 来定义 3 个不同的列表值。

```python
scores_team_1 = [100, 95, 120]
scores_team_2 = [45, 30, 10]
scores_team_3 = [200, 35, 190]

scores =  (scores_team_1, scores_team_2, scores_team_3)
```

以上代码创建了 3 个列表，并给每个列表分配了一个名称。然后将这 3 个列表打包到了元
组 scores。我们可能还记得，元组不能直接修改，因为它们是不可变的。但是这条规则并
不适用于元组中的元素——不能改变元组本身，但是可以（间接地）修改它们的值：

```python
scores_team_1[0] = 300
print(scores[0])        # [300, 95, 120]
```

当修改列表 scores_team_1 时，这个变化会出现在元组的第一个元素中，因为这个元素只
是一个可变值的别名。

当要修改元组中的可变列表时，可以通过二维索引来直接修改:

```python
scores[0][0] = 300
print(scores[0])        # [300, 95, 120]
```

元组并不能保护数据不被修改。不可变性主要是为了效率，而不是为了保护数据。可变值总
是会被修改，无论它们在哪里或者如何被引用。

### 5.7.1 浅拷贝

有很多方法可以确保你将一个名称绑定到一个可变值的副本上，而不是将其绑定到原始值上
。其中最明确的方法是使用 copy()函数，这有时也被称为浅拷贝。

```python
class Taco:

    def __init__(self, toppings):
        self.ingredients = toppings

    def add_sauce(self, sauce):
        self.ingredients.append(sauce)

default_toppings = ["Lettuce", "Tomato", "Beef"]
mild_taco = Taco(default_toppings)
hot_taco = Taco(default_toppings)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")       # Hot: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Mild: {mild_taco.ingredients}")     # Mild: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Default: {default_toppings}")       # Default: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
```

我们发现传入的 default_toppings 在经历了 `hot_taco.add_sauce` 函数调用之后被篡改
了，以下是修改后的：

```python
from copy import copy

class Taco:

    def __init__(self, toppings):
        # 将参数传递进来的默认配料进行复制，防止类中的方法篡改外部的参数
        self.ingredients = copy(toppings)

    def add_sauce(self, sauce):
        self.ingredients.append(sauce)

default_toppings = ["Lettuce", "Tomato", "Beef"]
mild_taco = Taco(default_toppings)
hot_taco = Taco(default_toppings)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")       # Hot: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Mild: {mild_taco.ingredients}")     # Mild: ['Lettuce', 'Tomato', 'Beef']
print(f"Default: {default_toppings}")       # Default: ['Lettuce', 'Tomato', 'Beef']
```

### 5.7.2 深拷贝

```python
from copy import copy

class Taco:

    def __init__(self, toppings):
        # 将参数传递进来的默认配料进行复制，防止类中的方法篡改外部的参数
        self.ingredients = copy(toppings)

    def add_sauce(self, sauce):
        self.ingredients.append(sauce)

default_toppings = ["Lettuce", "Tomato", "Beef"]
mild_taco = Taco(default_toppings)
hot_taco = copy(mild_taco)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")       # Hot: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Mild: {mild_taco.ingredients}")     # Mild: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Default: {default_toppings}")       # Default: ['Lettuce', 'Tomato', 'Beef']
```

根据输出我们发现，copy 并没有复制 mild_taco 的属性数据，即 hot_taco 和 mild_taco
的 ingredients 是同一份数据。

解决办法是使用深克隆：

```python
import copy

class Taco:

    def __init__(self, toppings):
        # 将参数传递进来的默认配料进行复制，防止类中的方法篡改外部的参数
        self.ingredients = copy.copy(toppings)

    def add_sauce(self, sauce):
        self.ingredients.append(sauce)

default_toppings = ["Lettuce", "Tomato", "Beef"]
mild_taco = Taco(default_toppings)
hot_taco = copy.deepcopy(mild_taco)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")       # Hot: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Mild: {mild_taco.ingredients}")     # Mild: ['Lettuce', 'Tomato', 'Beef']
print(f"Default: {default_toppings}")       # Default: ['Lettuce', 'Tomato', 'Beef']
```

## 5.8 隐式类型转换和显示类型转换

变量名称没有类型。因此，Python 没有典型的类型转换需求。

Python 会自动完成转换，例如在将整数（int）和浮点数相加时，这称为隐式类型转换
（coercion）。

```python
print(42.5)
x = 5 + 1.5         # 6.5
y = 5 + True        # 6
```

即便 Python 会进行隐式类型转换，也存在一些情况需要我们通过代码进行显式类型转换
​，即使用一个值来创建另一种类型的值，例如当我们需要把整数转换为字符串时。显式转
换是将一种类型的值明确转换为另一种类型的值。

Python 中的每种数据类型都是一个类的实例。因此，我们想要创建的类型的类只需要有一
个初始化器，用于处理你要转换的值的数据类型。

```python
# 显示类型转换
life_universe_everything = '42'
answer = float(life_universe_everything)
print(type(answer))     # <class 'float'>
print(answer)   # 42.0
```

## 5.9 小结
