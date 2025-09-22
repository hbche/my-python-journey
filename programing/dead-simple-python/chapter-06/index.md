# 第 6 章 函数和匿名函数

> 函数式是什么意思？
>
> 为了理解函数式编程是什么，我们必须了解它不是什么。过程式编程和面向对象编程都是
> 命令式的，即通过具体的过程描述如何实现目标。
>
> 过程式编程围绕控制块进行组织，并且重点关注控制流。面向对象编程围绕类和对象进行
> 组织，并且重点关注状态-特别是对象的属性。
>
> 函数式编程围绕函数进行组织。这种编程范式是声明式的，这意味着问题被分解为抽象步
> 骤。编程逻辑在数学上是一致的，在不同的语言中基本上没有变化。
>
> 在函数式编程中，需要为每个步骤编写一个函数。每个函数接收一个输入并产生一个输出
> ，它是自包含的，并且只做一件事，而不关心程序的其余部分。函数也没有状态，这意味
> 着他们不会在调用之间存储信息。一旦退出函数，所有局部名称都会失效。每次使用相同
> 的输入调用函数时，它都会生成相同的输出。
>
> 最重要的或许是，函数不应该有任何副作用，这意味着他们不应该改变任何东西。如果我
> 们将一个列表传递给纯函数，该函数不应该改变这个列表。相反，它应该输出一个全新的
> 列表（或者我们期望的值）。
>
> 纯净还是不纯净？
>
> 函数式编程范式围绕纯函数进行组织，纯函数没有副作用或状态，并且每个函数只执行一
> 个任务。
>
> Python 中的函数式编程行为通常被认为是“不纯的”​，这主要是由于存在可变数据类型。
> 为了确保函数没有副作用，需要做额外的工作。
>
> 如果特别处理一下细节，是可以在 Python 中编写纯函数式代码的，但是大多数 Python
> 爱好者选择从函数式编程中借用某些思想和概念，并将它们与其他编程范式结合起来。

## 6.1 Python 函数基础

```python
import random

def roll_dice(sides):
    """模拟掷骰子"""

    return random.randint(1, sides)

print("Roll for initiative...")
player1 = roll_dice(20)
player2 = roll_dice(20)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

假设我们想一次投掷骰子，并将结果以元组形式返回，则可以重写 roll_dice() 函数。

```python
import random

def roll_dice(sides, dice):
    """
    sides: 骰子面数
    dice: 单次掷的骰子数
    模拟掷骰子，一次掷多个骰子
    """

    # 使用tuple 将生成器转换成元组
    return tuple(random.randint(1, sides) for _ in range(dice))

print("Roll for initiative...")
player1, player2 = roll_dice(20, 2)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

返回的元组可以被解包，这意味着元组中的每一项都被绑定到一个名称上，可以用这个名称
来访问值。

## 6.2 递归

```python
import random

def roll_dice(sides, dice):
    """递归实现掷骰子"""
    if dice < 1:
        return ()
    roll = random.randint(1, sides)
    return (roll, ) + roll_dice(sides, dice-1)


print("Roll for initiative...")
player1, player2 = roll_dice(20, 2)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

## 6.3 默认参数

```python
import random

def roll_dice(sides, dice=1):
    """
    sides: 骰子面数
    dice: 单次掷的骰子数
    模拟掷骰子，一次掷多个骰子
    """

    # 使用tuple 将生成器转换成元组
    return tuple(random.randint(1, sides) for _ in range(dice))

print("Roll for initiative...")
player1, = roll_dice(20)
player2, = roll_dice(20)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

使用可选参数时，有一个潜在的陷阱：默认参数值只在函数定义时计算一次。使用任何可变
的数据类型作为可选参数是一件非常危险的事情。

```python
# 计算斐波那契数列

def fibonacci_next(series=[1, 1]):
    """计算斐波那契数列的下一轮值"""
    series.append(series[-2] + series[-1])
    return series

fib1 = fibonacci_next()
print(fib1)
fib1 = fibonacci_next(fib1)
print(fib1)

fib2 = fibonacci_next()
print(fib2)
```

我们期望的输出是：

```bash
[1, 1, 2]
[1, 1, 2, 3]
[1, 1, 2]
```

但是实际输出结果为：

```bash
[1, 1, 2]
[1, 1, 2, 3]
[1, 1, 2, 3, 5]
```

fib1 现在被绑定到与 series 相同的可变值，因此对 fib1 的任何更改都会反映在每次函
数调用的默认参数值中。第二次函数调用进一步改变了这个列表。

当第三次调用 fibonacci_next()时，我们可能希望从一个干净的状态（即[1, 1, 2]​）开
始，这是对原始默认参数值进行单次操作后的结果。但实际上，我们得到的是之前处理的那
个可变值：fib2 现在是列表的第 3 个别名。出问题了！

简而言之，永远不要使用可变值作为默认参数值。相反，请使用 None 作为默认值。

修复后的实现：

```python
# 计算斐波那契数列

def fibonacci_next(series=None):
    """计算斐波那契数列的下一轮值"""
    if series == None:
        series = [1, 1]
    series.append(series[-2] + series[-1])
    return series

fib1 = fibonacci_next()
print(fib1)
fib1 = fibonacci_next(fib1)
print(fib1)

fib2 = fibonacci_next()
print(fib2)
```

以上代码使用 None 作为默认参数值，然后在使用该默认参数值时创建了一个*新的可变
值*。

## 6.4 关键字参数

可读性极为重要。关键字参数可以通过将标签附加到函数调用中的参数上来帮助解决这个问
题。

按照输入的顺序映射的参数称为位置参数。

```python
dice_cup = roll_dice(6, 5)
```

我们可能会猜测这是在掷多个骰子，也许还指定了这些骰子有多少面。但问题在于，是掷 6
个 5 面骰子还是掷 5 个 6 面骰子？

> Python 之禅：面对太多可能，不要尝试猜测。

可以通过使用关键字参数来消除歧义。不需要更改函数定义就能使用关键字参数，只需要更
改函数调用即可：

```python
dice_cup = roll_dice(sides=6, dice=5)
```

每个名称都来自 roll_dice()的函数定义，它有两个参数：sides 和 dice。在我们的函数
调用中，可以通过名称直接分配值给这些参数。现在，每个参数的含义都非常清晰。指定参
数的名称，匹配函数定义中的名称，然后直接分配所需的值。

使用关键字参数时，甚至不必按顺序列出它们，确保所有必需的参数都接收到值即可：

```python
dice_cup = roll_dice(dice=5, sides=6)
```

当函数有多个可选参数时，这更有帮助。

重写 roll_dice()函数，使掷出的骰子默认是 6 面的:

```python
import random

def roll_dice(sides=6, dice=1):
    """
    sides: 骰子面数
    dice: 单次掷的骰子数
    模拟掷骰子，一次掷多个骰子
    """

    # 使用tuple 将生成器转换成元组
    return tuple(random.randint(1, sides) for _ in range(dice))

print("Roll for initiative...")
player1, = roll_dice(20)
player2, = roll_dice(20)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

关键字参数允许进一步简化函数调用:

```python
dice_cup = roll_dice(dice=5)
```

只需要传入可选参数 dice 的值，另一个参数 sides 会使用默认值。哪个参数先出现在函
数的参数列表中已经不再重要，你只需要使用自己想要的参数，剩下的就不用管了。

甚至可以混合使用位置参数和关键字参数。

```python
dice_cup = roll_dice(6, dice=5)
```

以上代码将 6 作为位置参数传递给函数定义中的第一个参数 sides，然后将 5 作为关键字
参数传递给第二个参数 dice。

这在很多情况下都很有用，特别是当我们不想费心命名位置参数但又想使用许多可选参数时
。唯一的规则是关键字参数必须处在函数调用中的位置参数之后

## 6.5 重载函数

Python 通常不需要重载函数。通过使用动态类型、鸭子类型和可选参数，便可以编写一个
函数来处理所有输入场景。

## 6.6.可变参数

有时候，我们根本不知道需要多少个参数。解决方案是使用任意参数列表，它会自动将多个
参数打包到一个可变参数或可变位置参数中。

```python
import random

# 使用可选参数收集实参
def roll_dice(*dice):
    """模拟掷骰子"""

    # 使用tuple 将生成器转换成元组
    return tuple(random.randint(1, d) for d in dice)

print("Roll for initiative...")
# 两个骰子的面数都是20，第一个参数表示第一个骰子的面数，第二个参数表示第二个骰子的面数
player1, player2 = roll_dice(20, 20)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")
```

以上代码通过在参数 dice 的前面加一个星号（\*）将其转换成了可变参数。现在，传递给
roll_dice()的所有参数都将被打包到一个元组中，绑定到名称 dice。

可变参数的位置很重要：可变参数必须位于函数定义中的任何位置参数之后。可变参数之后
的任何参数都只能用作关键字参数，因为可变参数消耗了所有剩余的位置参数。

```python
import random

# 使用可选参数实现
def roll_dice(*dice):
    return tuple(random.randint(1, d) for d in dice)

# 同时投掷 5 个 6面的骰子
dice_cup = roll_dice(6, 6, 6, 6, 6)
print(dice_cup)

# 同时投掷面数不同的4个骰子
bunch_o_dice = roll_dice(20, 6, 8, 4)
print(bunch_o_dice)
```

递归实现：

```python
import random

# 使用递归实现
def roll_dice(*dice):
    if dice:
        roll = random.randint(1, dice[0])
        # 生成dice 1~列表结尾的切片，*表示将列表进行解包
        return (roll, ) + roll_dice(*dice[1:])
    return ()

# 同时投掷 5 个 6面的骰子
dice_cup = roll_dice(6, 6, 6, 6, 6)
print(dice_cup)

# 同时投掷面数不同的4个骰子
bunch_o_dice = roll_dice(20, 6, 8, 4)
print(bunch_o_dice)
```

大部分代码看起来和之前的递归版本很相似，最重要的变化在于传递给递归函数调用的内容
。名称前面的星号（\*）表示将元组 dice 解包到参数列表中。由于已经处理了列表中的第
一项，因此使用切片 [1:] 来删除第一项 ​，以确保它不会再次被处理。

### 关键字可变参数

为了捕获未知数量的关键字参数，请在参数名称的前面加两个星号（\*\*）​，使参数成为
关键字可变参数。传递给函数的关键字参数被打包到一个单独的字典对象中，以保留关键字
和值之间的关联。它们也可以通过在名称的前面加两个星号来解包。

当需要将参数盲目地传递给另一个函数调用时，关键字可变参数非常有用。

```python
def call_something_else(func, *args, **kwargs):
    return func(*args, **kwargs)
```

call_something_else()函数有一个位置参数 func，这里为其传入一个可调用对象，例如另
一个函数。第二个参数 args 是一个可变参数，用于捕获所有剩余的位置参数。最后一个参
数是关键字可变参数 kwargs（有时也记作 kw）​，用于捕获任何关键字参数。请记住，即
便这两个参数都为空，这段代码仍然可以正常工作。

可以通过将对象传递给 callable()函数来检查该对象是否可调用。

args 和 kwargs 这两个名称是惯例用法，分别用于表示位置可变参数和关键字可变参数。

当函数调用可调用对象 func 时，首先解包所有捕获的位置参数，然后解包所有关键字参数
。函数代码不需要任何关于可调用对象参数列表的信息，相反，在第一个位置参数之后传递
给 call_something_else()的所有参数都会被传递。

```python
def say_hi(name):
    """模拟问候"""
    print(f"Hello, {name.title()}!")

def call_something_else(func, *args, **kwargs):
    return func(*args, **kwargs)

call_something_else(say_hi, name='Bob') # 关键字参数
```

## 6.7 仅关键字参数

可以使用可选参数将一些关键字参数转换为仅关键字参数，仅关键字参数是 PEP 3102 中引
入的。这些参数不能作为位置参数传递值，而只能作为关键字参数。

```python
# 使用可选参数限制函数只能传递关键字参数
import random

def roll_dice(*, dice=1, sides=6):
    # 此处使用了未命名的可选参数*，以确保参数列表中该可变参数之后的每个参数都只能通过名称来访问。
    return tuple(random.randint(1, sides) for _ in range(dice))

dice_cup = roll_dice(sides=6, dice=2)
print(dice_cup)
```

以上代码使用了未命名的可选参数\*，以确保参数列表中该可变参数之后的每个参数都只能
通过名称来访问。如果调用者传入太多的位置参数，则会引发 TypeError。这会影响使用方
式，现在只能使用关键字参数。

使用位置参数则会报错：

```python
# 使用位置参数
dice_cup = roll_dice(6, 2)
print(dice_cup)
```

错误信息：

```bash
TypeError: roll_dice() takes 0 positional arguments but 2 were given
```

### 6.7.1 仅位置参数

从 Python3.8 开始，还可以定义仅位置参数。当参数名称不明确或未来可能改变时，这很
有用，这意味着任何将其用作关键字参数的代码未来都可能发生变化。

位置参数必须始终位于参数列表的开头。在参数列表中使用斜线(/)即可将斜线前面的所有
参数指定为仅位置参数：

```python
# 限制dice参数只能通过位置参数传递
import random

def roll_dice(dice=1, /, sides=6):
    """使用斜杠标识前面的参数指定为仅位置参数，后面的参数即可为位置参数也可谓关键字参数"""

    return tuple(random.randint(1, sides) for _ in range(dice))
```

以下是不同的调用方式：

```python
# 都传递位置参数
dice_cup1 = roll_dice(4, 20)            # dice=4, sides=20
# 仅传入第一个位置参数，sides为默认值
dice_cup2 = roll_dice(4)                # dice=4, sides=6
# 位置参数只用默认值，sides使用关键字参数
dice_cup3 = roll_dice(sides=20)         # dices=4, sides=20
# 位置参数+关键字参数
dice_cup4 = roll_dice(4, sides=20)      # dices=4, sides=20
```

以上调用都是等效的，如果试图通过关键字参数指定 dice 参数，会报错：

```python
dice_cup4 = roll_dice(dice=4, sides=20)
```

错误信息：

```bash
TypeError: roll_dice() got some positional-only arguments passed as keyword arguments: 'dice'
```

### 6.7.2 参数类型

```python
def func(pos_only=None, /, pos_kw=None, *, kw_only=None):
```

参数 pos_only 是仅位置参数，因为它位于斜线(/)标记之前。任何仅位置参数都必须首先
出现在参数列表中。由于此参数具有默认值，因此它是可选的。但是，如果想传递一个实参
给它，则这个实参必须是传递给函数的第一个位置参数，否则将引发 TypeError。

下一个参数是 pos_kw，它可以是位置参数或关键字参数，位于任何仅位置参数和显现(/)标
记之后。

最后，星号（\*）标记之后的参数是 kw_only，它是一个关键字参数。在这个例子中，如果
函数接收到两个以上的位置参数，将会引发 TypeError。

## 6.8 嵌套函数

有时候，我们希望在函数内部复用逻辑，可以在函数中嵌套函数。

我们可以使用嵌套函数来改进 roll_dice() 的递归版本：

```python
def roll_dice(sides, dice):
    """递归实现掷骰子"""
    # 嵌套函数
    def roll():
        return random.randint(1, sides)

    if dice < 1:
        return ()
    return (roll(), ) + roll_dice(sides, dice-1)
```

## 6.9 闭包

可以创建一个函数，用它构建并返回一种称为闭包的对象，闭包包含一个或多个 nonlocal
名称。

```python
import random

# 使用闭包重写掷骰子
def make_dice_cup(sides=6, dice=1):
    def roll():
        return tuple(random.randint(1, sides) for _ in range(dice))
    return roll

roll_for_damage = make_dice_cup(sides=8, dice=5)
damage = roll_for_damage()
print(damage)
```

使用闭包时需要小心，因为很容易违反函数式编程的规则。如果闭包有能力改变它所封闭的
值，它就变成了一种事实上的对象，而且是一个很难调试的对象！

### 6.9.1 带闭包的递归

以下是一个经典的带闭包递归的错误示例：

```python
import random
# 使用待递归的闭包实现掷骰子
def make_dice_cup(sides=6, dice=1):

    def roll():
        nonlocal dice
        if dice < 1:
            return ()
        dice -= 1
        return (random.randint(1, sides), ) + roll()

    return roll

dice_cup = make_dice_cup(sides=8, dice=5)
damage1 = dice_cup()
print(damage1)
damage2 = dice_cup()
print(damage2)
```

由于返回的闭包都共用外层函数的参数，在经过一轮调用之后，由于闭包直接对外层函数的
dice 参数做修改，所以后续调用中 dice 都为 0，导致后续闭包的调用返回的都是 `()`
空元祖。

为了实现一个递归闭包，需要在闭包上使用一个可选参数。

```python
import random
# 使用待递归的闭包实现掷骰子
def make_dice_cup(sides=6, dice=1):

    def roll(dice=dice):
        if dice < 1:
            return ()
        return (random.randint(1, sides), ) + roll(dice - 1)

    return roll

dice_cup = make_dice_cup(sides=8, dice=5)
damage1 = dice_cup()
print(damage1)
damage2 = dice_cup()
print(damage2)
```

这个版本使用 nonlocal 名称 dice 作为新的局部参数 dice 的默认值。

### 6.9.2 有状态闭包

虽然通常最好将闭包编写为纯函数，但有时也有必要创建有状态闭包——在调用之间保留一些
状态以供闭包使用。一般来说，除非没有其他解决方案，否则应避免使用有状态闭包。

## 6.10 lambda 表达式

mbda 表达式是由表达式组成的匿名（无名）函数，其结构如下：

```python
lambda x, y: x + y
```

冒号的左侧是参数列表，如果不想接收任何参数，则可以省略参数列表。冒号的右侧是
return 表达式，lambda 表达式会对其求值并隐式地返回结果。要使用 lambda 表达式，就
必须将其绑定到一个名称，可以通过赋值或将其作为参数传递给另一个函数。

```python
# lambda表达式基础
add = lambda x, y: x + y
answer = add(20, 22)
print(answer)       # 42
```

### 6.10.1 为什么 lambda 表达式很有用？

我们先来看一个没有使用 lambda 表达式的案例：

```python
import random

# 模拟文本大冒险中的玩家角色
# 声明全局变量
# 当前经验值
xp = 10
# 当前血条
health = 10
def attempt(action, min_roll, outcome):
    """
    action: 表示执行某种操作
    min_roll: 表示操作的下限
    outcome: 表示后续操作
    """
    global xp, health
    roll = random.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} SUCCESS.")
        result = True
    else:
        print(f"{action} FAILED.")
        result = False

    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"Experience is now {xp}")

    return result

def eat_bread(success):
    if success:
        return (1, 0)
    else:
        return (-1, 0)

def fight_ice_weasel(success):
    if success:
        return (0, 10)
    else:
        return (-10, 10)

attempt('Eating bread', 5, eat_bread)
attempt('Fighting ice weasel', 15, fight_ice_weasel)
```

下面使用 lambda 表达式重写上面的代码：

```python
import random

# 模拟文本大冒险中的玩家角色
# 声明全局变量
# 当前经验值
xp = 10
# 当前血条
health = 10
def attempt(action, min_roll, outcome):
    """
    action: 表示执行某种操作
    min_roll: 表示操作的下限
    outcome: 表示后续操作
    """
    global xp, health
    roll = random.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} SUCCESS.")
        result = True
    else:
        print(f"{action} FAILED.")
        result = False

    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"Experience is now {xp}")

    return result

def eat_bread(success):
    if success:
        return (1, 0)
    else:
        return (-1, 0)

def fight_ice_weasel(success):
    if success:
        return (0, 10)
    else:
        return (-10, 10)

attempt('Eating bread', 5, lambda success: (1,10) if success else (-1, 0) )
attempt('Fighting ice weasel', 15, lambda success: (0, 10) if success else (-10, 10))
```

以上每个函数调用的第三个参数都是一个 lambda 表达式，它接收一个名为 success 的参
数，并根据 success 的值返回另一个值。

通过使用 lambda 表达式，便可以用一行代码创建出许多不同的可能结果。

请记住，lambda 表达式只能有一个 return 表达式！这使得 lambda 表达式非常适用于短
小、清晰的逻辑片段，尤其是当通过将逻辑保持在另一个函数调用中的用例附近来使代码更
具可读性时。

### 6.10.2 将 lambda 作为排序的键

lambda 表达式最常见的一个用途是作为排序键使用，排序键是一个可调用的函数，它返回
应该用于排序的集合或对象的一部分。排序键通常被传递给另一个函数，该函数负责以某种
方式对数据进行排序。

```python

```
