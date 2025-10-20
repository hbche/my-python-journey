# 第 9 章 集合与迭代

## 9.1 循环

Python 中有两种类型的循环：while 循环和 for 循环。这并不意味着两者可以互换，相反
，每种循环都有自己独特的目的。

### 9.1.1 while 循环

while 循环是非常传统的循环。只要其标头中的表达式的计算结果为 True ，循环体就会执
行。

```python
# 演示 while 循环

number = None

while number is None:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("You must enter a number.")

print(f"You entered {number}")
```

只要 number 的值为 None ，while 循环的代码块就会一直重复。一旦用户输入一个有效的
整数，就会退出循环，并将数字输出到控制台。

如果想提供一种直接退出而不是依赖输入数字的机制，我们可以使用 break 关键字手动退
出循环。这里允许用户通过输入 q 而不是数字来退出循环：

```python
# 演示 while 循环

number = None

while number is None:
    try:
        raw = input("Enter a number: ")
        if raw == 'q':
            # 提前终止循环
            break
        number = int(raw)
    except ValueError:
        print("You must enter a number.")

print(f"You entered {number}")
```

输出如下：

```bash
Enter a number: q
You entered None
```

最后一行输出不对。我们希望程序立即退出。

为了解决这个问题，我们可以使用 else 子句。当 Python 循环正常结束时，运行 else 子
句；但是如果循环因终端、返回或引发的异常而终止，则 else 子句不会运行。

```python
# 演示 while 循环

number = None

while number is None:
    try:
        raw = input("Enter a number: ")
        if raw == 'q':
            # 提前终止循环
            break
        number = int(raw)
    except ValueError:
        print("You must enter a number.")
else:
    # 循环顺利结束时才执行，任何提前结束的场景都不执行else子句
    print(f"You entered {number}")
```

### 9.1.2 for 循环

和 while 循环一样，for 循环也有一个 else 子句，这个 else 子句仅在循环正常结束时
运行，当循环因中断、返回或引发的异常而提前终止时则不会运行。

```python
# 演示 for 循环遍历一组值
numbers = ["One", "Two", "Three"]

for number in numbers:
    print(number)
else:
    print("We're done!")
```

## 9.2 集合

集合是一种容器，其中包含以某种方式组织的一项或多项。每一项都被绑定到一个值，值本
身不包含在集合中。Python 中有 5 种基本的集合：元组、列表、双端队列、可变集合和字
典。每种集合都有多种变体。

### 9.2.1 元组

元组（tuple）是一个不可变序列（类似数组的集合）​，这意味着元组一旦被创建，其中的
元素就不能被添加、删除或重新排序。

通常，元组用于存储异构类型的顺序排列的数据，例如，当需要将类型不同但相互关联的值
放在一起时。下面将一个包含客户名称、咖啡订单和订单大小的元组。

```python
order = ("Jason", "pumkin spice latte", 12)
```

以上代码将元组定义为逗号分隔的值序列，并用括号括起来。

> 注意：在很多情况下，元组的括号在技术上是可选的。它仅仅用来区分元组与其周围环境
> ，比如将元组传递给参数时。始终包括括号是一种很好的习惯。

因为元组中的内容是有序的，所以可以通过方括号中指定的索引来访问对应的元素：

```python
print(order[1])     # pumkin spice latte
```

如果元组只包含一个元素，请在元组后保留一个逗号：

```python
# 只包含一个元素的元组
orders = ("pumkin spice latte",)
```

由于元组是不可变的，因此它不提供任何用于添加、更改或删除元素的内置方法。我们可以
预先完整地定义一个元组，然后访问其中包含的元素。

### 9.2.2 具名元组

collections 模块提供了元组的一种"奇怪小变体"，称为具名元组，它允许我们定义一个带
有名字字段的、类似于元组的集合。和普通元组一样，具名元组也是不可变的，主要用途是
向值添加键，可以通过键可以方位值，同时仍然可通过下表进行访问：

```python
# 演示具名元组的使用
from collections import namedtuple

CoffeeOrder = namedtuple("CoffeeOrder", ("item", "addons", "to_go"))

order = CoffeeOrder("pumpkin spice latte", ('whipped cream', ), True)
print(order.item)       # pumpkin spice latte
print(order[2])         # True
```

以上代码以类型名称 CoffeeOrder 定义了一个新的具名元组，并在其中命名了三个字段
：item、addons 和 to_go。

接下来，通过将值传递给 CoffeeOrder 初始化器来创建具名元组的新实例，并将该实例绑
定到 order。这样就可以通过字段名或索引来访问 order 中的值了。

在实践中，大多数 Python 爱好者更青睐于字段或类，而不是命名元组。当然，这三者都有
各自的最佳使用场景。

### 9.2.3 列表

列表是可变的序列集合，这意味着可以在列表中添加、删除和重新排列元素。通常，列表用
来存储同类型的可顺序排列的数据：

```python
# 演示列表使用
specials = ["pumkin spice latte", "caramel macchiato", "mocha cappuccino"]
```

以上代码将列表定义为逗号分隔的序列，并用方括号括起来。和元组一样，可通过在方括号
中指定索引来访问某个列表元素：

```python
print(specials[1])  # caramel macchiato
```

可以将列表用作数组、堆栈或队列。

可使用 pop() 从列表中返回和删除元素，如果不将索引传递给 pop()，则默认删除最后一
项：

```python
drink = specials.pop() # 移除最后一元素，并返回该元素
print(drink)    # mocha cappuccino
print(specials) # ['pumkin spice latte', 'caramel macchiato']
```

如果将索引作为参数传递给 pop()，则指定的元素将被删除：

```python
drink = specials.pop(1) # 删除索引为1的元素，并返回该元素
print(drink)    # caramel macchiato
print(specials) # ['pumkin spice latte']
```

还可以使用 append() 将新元素添加到列表的末尾：

```python
specials.append('cold brew')    # 在列表结尾追加元素
print(specials) # ['pumkin spice latte', 'cold brew']
```

如果想在列表的其他地方添加一个元素，可以使用 insert()：

```python
specials.insert(1, "americano") # 在索引为1的位置插入指定的元素
print(specials) # ['pumkin spice latte', 'americano', 'cold brew']
```

insert() 的第一个参数是目标索引 1，新元素 "americano" 是其第二个参数。

以上是修改列表的 3 中最常用的方法。Python 还提供了更多方法，其中很多还挺有意思的
。Python 官方文档是我们学习所有可行方法的最佳资源。

> 注意：如果想要一个传统的动态大小的数组，它可以用来紧凑地存储一种类型的数据，请
> 查阅 Python 官方文档的“array”——高效的数字数组。但是其实很少需要这样做。

### 9.2.4 双端队列

collections 模块还提供了另外一种序列 deque，又称为双端队列，其针对访问第一个和最
后一个元素的操作进行了优化。当性能特别重要时，它特别适合用作堆栈或队列。

```python
# 使用双端队列模拟咖啡店排队
from collections import deque
customers = deque(['Daniel', 'Denis'])
```

以上代码从 collections 模块中导入 deque 包后，创建了一个新的双端队列，并将其绑定
到 customers。尽管可以省略初始化并并一个空白双端队列开始，但这里还是先传递了一个
包含两个客户的列表作为其初始值。

现在，Simon 进入了咖啡馆并排队，使用 append() 将其追加到双端队列的末尾：

```python
customers.append('Simon')
print(customers)    # deque(['Daniel', 'Denis', 'Simon'])
```

然后咖啡师开始服务队列中的下一位客户，移除第一位客户 Daniel，从队伍的前面（左边
）开始，使用 popleft()：

```python
customer = customers.popleft() # 从队列中移除最前面的元素
print(customer)     # Daniel
print(customers)    # deque(['Denis', 'Simon'])
```

现在又变成了两个人在排队。假设 James 想插队到所有人的前面，使用 appendleft()将其
追加到双端队列的左侧：

```python
customers.appendleft('James')
print(customers)    # deque(['James', 'Denis', 'Simon'])
```

但 Simon 不介意，因为排在最后的人赢得了免费咖啡。从双端队列中删除最后一项：

```python
last_in_line = customers.pop()
print(last_in_line) # Simon
```

现在，双端队列只有 James 和 Denis：

```python
print(customers)    # eque(['James', 'Denis'])
```

### 9.2.5 可变集合

可变集合是一种内置的、可变的、无序的集合，其中所有元素都必须是唯一的。如果尝试添
加可变集合中已存在的元素，添加操作会被忽略。我们将主要使用可变集合进行快速检查以
及与集合论相关的各种操作，尤其是在大型数据集中。

存储在可变集合中的每个值都必须是可哈希的，Python 文档将可变集合定义为具有“在其生
命周期内永不改变的哈希值”。可哈希对象实现了特殊方法 `__hash__()`。所有内置的不可
变数据类型都是可哈希的，因为其值在整个生命周期中都不会改变。然而，还有很多可变类
型是不可哈希的。

使用一个可变集合在咖啡队伍中进行抽奖，每个客户只能参与一次：

```python
# 定义集合
raffle = {'James', 'Denis', 'Simon'}
```

首先将可变集合定义为逗号分隔的值序列，用花括号括起来。在本例中，初始值有 3 个。

当客户进来时，使用 add() 将他的名字追加到可变集合中。如果他的名字（如 Denis）已
经在可变集合中，那么即便尝试追加，他的名字也不会被重复添加：

```python
# 使用add方法想可变集合中追加元素
raffle.add('Daniel')
raffle.add('Denis')
print(raffle)   # {'James', 'Denis', 'Simon', 'Daniel'}
```

print 语句输出可变集合中当前所有元素。可变集合是无序的，因此无法预测元素出现的顺
序。

可以使用 discard() 从可变集合中删除元素。由于 Simon 早些时候已经赢得了一些东西，
所以他不能再参与抽奖：

```python
# 使用discard方法从可变集合中移除元素
raffle.discard('Simon')
print(raffle)   # {'Daniel', 'Denis', 'James'}
```

也可以使用 remove() 来删除一个值，但是若果指定的值不在可变集合中，则会引发
KeyError。discord() 永远不会引发错误。

最后，使用 pop() 从可变集合中返回并删除任意项：

```python
winner = raflle.pop()
print(winner)
```

> 请注意，任意并不意味着随意！pop()方法总是返回和删除恰好位于可变集合第一个位置
> 的元素。因为可变集合是无序的，并且 Python 并不保证元素的内部顺序，所以不要依赖
> 可变集合来提供可靠的随机性。

> 要指定一个空的可变集合，可以使用 set()，因为一对空的花括号实际指的是一个空白字
> 典。

### 9.2.6 不可变集合

可变集合的不可变孪生对象是不可变集合，它们的工作方式大致相同。不可变集合和可变集
合的区别就像列表和元组的区别：一旦创建，不可变集合就不能再追加或删除元素。

为了证明这一点，创建一个不可变集合来存储过往所有获奖的客户，以免他们再次参与抽奖
：

```python
raffle = {'Kyle', 'Denis', 'Jason'}
# 创建不可变集合，记录过往获奖名单
pre_winners = frozenset({'Denis', 'Simon'})
```

可以将一组字符串、现有的可变集合或另一个线性集合传递给 frozenset()进行初始化
。pre_winners 被定义之后，其内容就不能修改 —— 记住，这是不可变的。常规的可变集合
仍然可以修改。

可变集合和不可变集合一个令人兴奋的功能是它们都支持集合数学运算。可以使用数学运算
符和逻辑运算符来计算并集(|)、交集(&)、差集(-)以及对称差集(^)。它们还可以用于测试
一个集合是另一个集合的子集(<或<=)还是超集(>或>=)。Python 官方文档介绍了其他几个
用于组合和比较任意类型集合的函数。

使用 -= 运算符从抽奖集删除所有以往的获奖者：

```python
# 使用 -= 运算符删除过往获奖者
raffle -= pre_winners
print(raffle)   # 打印删除后的抽奖名单  {'Kyle', 'Jason'}
```

然后就可以使用 pop() 从 raffle 中取出任意一个元素来找到下一位获奖者：

```python
winner = raffle.pop()
print(winner)
```

### 9.2.7 字段

字典是一种可变集合，它以键值对的形式存储数据，而不是以线性方式存储数据。这种关联
的存储方式称为映射。键实际上可以是任意类型，只要该类型是可哈希的即可。最容易记住
的是，可哈希类型实际总是不可变的。

键值对中的值可以是任何值。无论字典中的数据量大小如何，通过键进行查找总是特别快。
（在其他语言中，这种数据类型成为哈希表。）

使用字段存储 Uncomment Cage 的咖啡味：

```python
menu = {"drip": 1.95, "cappuccino": 2.95}
```

以上代码将字典创建为一系列以逗号分隔的键值对，用花括号括起来，并用冒号分隔每个键
值对中的键和值。在本例中，键是表示咖啡味的字符串，值是表示加个的浮点数。

可通过在方括号中指定键来访问各个元素：

```python
print(menu["drip"])     # 1.95
```

如果正在访问的键不在字典中， 则引发 KeyError。可以通过为方括号中指定的键赋值来添
加或修改元素。在这里，向字典中追加 "americano" 键，并指定价格为 2.49：

```python
# 添加元素
menu['americano'] = 2.49
print(menu)     # {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}
```

出于某些原因，美式咖啡在咖啡馆里并不是很受欢迎，所以我们决定使用 del 关键字将其
从字典中删除：

```python
# 删除指定元素
del menu['americano']
print(menu)     # {'drip': 1.95, 'cappuccino': 2.95}
```

再次提醒，如果方括号中的键不在字典中，将引发 KeyError。

### 9.2.8 检查还是例外？

关于应该直接使用 in 运算符，还是使用带有 KeyError 的 try 语句来检查字典中的键，
仍存在一些争议。

若使用 EAFP 策略，则代码如下：

```python
menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

def check(order):
    try:
        print(f"Your total is {menu[order]}")
    except KeyError:
        print("That item is not on the menu.")

check('drip')       # Your total is 1.95
check('tea')        # That item is not on the menu.
```

以上代码在 try 语句中尝试访问和键 order 关联的字段 menu 中的值。如果键无效，将引
发 KeyError，在 except 子句中捕获这一异常，然后采取适当的行动来处理。

这种方式更适用于无效键处于异常情况的场景。通常，使用 except 子句是一种在性能方面
开销更加昂贵的操作，但是对处理错误和其他异常情况来说，这又是完全合理的开销。

如果使用 LBYL 策略，则代码如下：

```python
menu = {"drip": 1.95, "cappuccino": 2.95, "americano": 2.49}

def checkout(order):
    if order in menu:
        print(f"Your total is {menu[order]}")
    else:
        print("That item is not on the menu.")

checkout("drip")        # Your total is 1.95
checkout("tea")         # That item is not on the menu.
```

在这种策略中，在执行任何操作之前检查 oder 是否为 menu 字典中存在的键。如果是，就
可以安全地访问和键关联的值。如果希望经常检查键是否有效，则这种方法更加可取，因为
这两种情况都有可能发生。失败比例外更常见，因此，以上两种策略在理想情况下具有大致
相同的性能。

### 9.2.9 字典变体

Python 有一个 collections 模块，其提供了内置字典的一些变体。以下是三种最常见的变
体，以及它们各自对应的独特行为。

- defaultdict: 允许指定生成默认值的可调用对象。如果尝试访问未定义键的值，Python
  将使用此默认值自动定义一个新的键值对。
- OrderedDict: 具有用以跟踪和管理键值对顺序的额外功能。从 Python 3.7 开始，内置
  的 dict 也正式保留了插入顺序，但是 OrderedDict 专门针对重新排序进行了优化，并
  具有额外的行为支持。
- Counter: 是专为计算可哈希对象而设计的，对象是键，计数是整数值。在其他编程语言
  中，这种类型的集合被称为多重集。

## 9.3 集合的解包

所有集合都可以解包到多个变量中，这意味着每个元素都有自己的名称。例如，可以将包含
3 个客户的双端队列解包到 3 个单独的变量中。首先创建客户的双端队列：

```python
from collections import deque

customers = deque(['Kyle', 'Simon', 'James'])
```

接下来解包这个双端队列。把以逗号分割的名称列表按顺序放在赋值运算符的左侧，即可完
成解包：

```python
first, second, third = customers
print(first)        # Kyle
print(second)       # Simon
print(third)        # James
```

有时，我们会看到赋值运算符的左侧部分用括号括了起来，不过，解包线性集合时不需要使
用括号。被解包的集合则放在赋值运算符的右侧。

解包有一个主要限制：我们必须知道要解包的值有多少个！为了演示这一点，用 append()
方法向双端队列中追加一个客户：

```python
customers.append('Daniel')
```

如果在赋值运算符的左侧指定太多或太少的名称，将引发 ValueError。由于当前双端队列
包含四个值，因此尝试将其解包为三个值会失败：

```bash
    first, second, third = customers
    ^^^^^^^^^^^^^^^^^^^^
ValueError: too many values to unpack (expected 3)
```

要解决这个问题，可以在赋值运算符的左侧指定第 4 个名称。但是对于这个例子，我们想
忽略第 4 个值，可通过将其解包为下划线(\_)来忽略任何元素：

```python
first, second, third, _ = customers
print(first)        # Kyle
print(second)       # Simon
print(third)        # James
```

当下划线用作名称时，通常表示应该忽略响应值。可以根据需要多次使用下划线。如果想忽
略集合中的最后两个值，如下所示：

```python
first, second, _, _ = customers
print(first)        # Kyle
print(second)       # Simon
```

只有 customers 中的前两个值被解包，最后两个值则被忽略。

顺便说明一下，如果需要解包一个只包含一个值的集合，在要解包到的名称后保留一个逗号
即可：

```python
# 注意：只有一个元素的元组，结尾需要保留一个逗号，区分()运算符
baristas = ('Jason', )
barista,  = baristas
print(barista)
```

### 9.3.1 星号表达式

如果不知道集合中有多少额外的值，则可以使用带星号的表达式(称为星号表达式)捕获多个
还未解包的值：

```python
# 星号表达式
customers = deque(['Kyle', 'Simon', 'James', 'Daniel'])
first, second, *rest = customers
print(first)        # Kyle
print(second)       # Simon
print(rest)         # ['James', 'Daniel']
```

前两个值被解包为 first 和 second，其余的值（如果有的话）则被打包到 rest 列表中。
只要被解包的集合至少有两个值，能逐一对应赋值运算符左侧每个未加星号的名称，这行代
码就能工作。如果集合中仅有两个值，则 rest 将是一个空列表。

可以在解包列表中的任何位置（包括开头）使用星号表达式。如下所示：

```python
# 星号表达式
customers = deque(['Kyle', 'Simon', 'James', 'Daniel'])
first, *middle, last = customers
print(first)        # Kyle
print(middle)       # ['Simon', 'James']
print(last)         # Daniel
```

甚至可以使用星号表达式来忽略多个值：

```python
# 星号表达式
customers = deque(['Kyle', 'Simon', 'James', 'Daniel'])
*_, second_to_last, last = customers
print(second_to_last)   # James
print(last)             # Daniel
```

通过在下划线前加上星号，以上代码捕获了多个值，但又忽略了他们，而不是将它们打包到
一个列表中。在这种情况下，其实只解包了集合中的最后两个值。

每个解包语句中只能有一个星号表达式，因为星号表达式是贪婪的 —— 其力图捕获尽可能多
的值。在评估星号表达式前，Python 将值解包到所有其他名称中。在同一个语句中使用多
个星号表达式是没有意义的，因为 Python 无法确定一个表达式在哪里停止，以及另一个表
达式又在何处开始。

### 9.3.2 字典的解包

字典可以向任何其他内建类型的集合一样解包。默认情况下，只有键被解包，就像解包表示
咖啡口味的字典那样：

```python
menu = {'drip': 1.95, 'cappuccion': 2.95, 'americano': 2.49}
a, b, c = menu
print(a)        # drip
print(b)        # cappuccion
print(c)        # americano
```

如果想要的是值，就必须使用字典视图进行解包，字典视图提供了对字典中键和值的访问。
在这种情况下，使用 value() 字典视图：

```python
# 对字典的值进行解包
a, b, c = menu.values()
print(a)        # 1.95
print(b)        # 2.95
print(c)        # 2.49
```

还可以通过 item() 字典视图同时解包获得键和值，浙江返回元组形式的键值对：

```python
# 基于字典的 item 视图解包
a, b, c = menu.items()
print(a)        # ('drip', 1.95)
print(b)        # ('cappuccion', 2.95)
print(c)        # ('americano', 2.49)
```

还可以通过在元组将被解包到的一对名称周围使用圆括号，在同一语句中解包每个键值元组
：

```python
(a_name, a_price), (b_name, b_price), *_ = menu.items()
print(a_name)       # drip
print(a_price)      # 1.95
print(b_name)       # cappuccion
print(b_price)      # 2.95
```

可以使用这种带括号的解包策略来解包二维集合，如元组列表或集合元组

## 9.4 集合的结构模式匹配

从 Python3.10 开始，可以对元组、里诶包和字典进行结构模式匹配。

在模式中，元组和列表是可以互换的，因为它们都和序列模式匹配。序列模式使用和解包相
同的语法，且具有使用星号表达式的能力。例如，可以匹配序列的第一个和最后一个元素，
并忽略中间所有其他元素：

```python
order = ['venti', 'no whip', 'mocha latte', 'for here']

match order:
    case ('tall', *drink, 'for here'):
        drink = ' '.join(drink)
        print(f"Filling ceramic mug with {drink}.")
    case ['grande', *drink, 'to go']:
        drink = ' '.join(drink)
        print(f"Filling large paper cup with {drink}.")
    case ('venti', *drink, 'for here'):
        drink = ' '.join(drink)
        print(f"Filling extra large tumbler with {drink}.")

# Filling extra large tumbler with no whip mocha latte.
```

序列模式是相同的，无论是括在圆括号中还是括在方括号中，按里诶包顺序和每个模式进行
比较。对于每一个序列，检查第一个和最后一个元素，其余元素则通过通配符捕获到 drink
中。在每种情况下，都将 drink 中的元素结合在一起，以确定用什么来填充所选的容器。

还可以使用映射模式对字典中的特定值进行模式匹配，只是改为使用字典，代码如下所示：

```python
# 使用字典进行序列匹配
order = {
    'size': 'venti',
    'notes': 'no whip',
    'drink': 'mocha latte',
    'serve': 'for here'
}

match order:
    case {'size': 'tall', 'serve': 'for here', 'drink': drink}:
        print(f"Filling ceramic mug with {drink}.")
    case {'size': 'grande', 'serve': 'to go', 'drink': drink}:
        print(f"Filling large paper cup with {drink}.")
    case {'size': 'venti', 'serve': 'for here', 'drink': drink}:
        print(f"Fulling extra large tumbler with {drink}.")

# Fulling extra large tumbler with mocha latte.
```

映射模式包裹在花括号中。仅检查映射模式中指定的键，而忽略其他键。在这个版本中，检
查'size'和'serve'键，以及和键'drink'关联的值，并将它们捕获到 drink 中。

如果运行这个版本的代码，就会注意到 'notes' 被去掉了。为了解决这个问题，可以将代
码改写为使用通配符捕获所有剩余的键，如下所示：

```python
# 使用字典进行序列匹配
order = {
    'size': 'venti',
    'notes': 'no whip',
    'drink': 'mocha latte',
    'serve': 'for here'
}

match order:
    case {'size': 'tall', 'serve': 'for here', **rest}:
        drink = f"{rest['notes']} {rest['drink']}"
        print(f"Filling ceramic mug with {drink}.")
    case {'size': 'grande', 'serve': 'to go', **rest}:
        drink = f"{rest['notes']} {rest['drink']}"
        print(f"Filling large paper cup with {drink}.")
    case {'size': 'venti', 'serve': 'for here', **rest}:
        drink = f"{rest['notes']} {rest['drink']}"
        print(f"Fulling extra large tumbler with {drink}.")

# Fulling extra large tumbler with no whip mocha latte.
```

> 因为映射模式中未明确列出的任何键都会被忽略，所以忽略所有剩余键而不捕获它们的通
> 配符（两个星号加一个下画线，即\*\*\_）在映射模式中是不合法的。

值得注意的是，我们仍然可以直接访问 order。如下所示：

```python
# 使用字典进行序列匹配
order = {
    'size': 'venti',
    'notes': 'no whip',
    'drink': 'mocha latte',
    'serve': 'for here'
}

match order:
    case {'size': 'tall', 'serve': 'for here'}:
        drink = f"{order['notes']} {order['drink']}"
        print(f"Filling ceramic mug with {drink}.")
    case {'size': 'grande', 'serve': 'to go'}:
        drink = f"{order['notes']} {order['drink']}"
        print(f"Filling large paper cup with {drink}.")
    case {'size': 'venti', 'serve': 'for here'}:
        drink = f"{order['notes']} {order['drink']}"
        print(f"Fulling extra large tumbler with {drink}.")

# Fulling extra large tumbler with no whip mocha latte.
```

和以前一样，出于模式匹配的目的，映射模式中省略的每个键都将被忽略。

## 9.5 以索引或键访问元素

很多集合是可订阅的，这意味着可以通过在方括号中指定索引来访问某个元素

```python
specials = ['pumpkin spice latte', 'caramel macchiato', 'macho cappuccino']
print(specials[1])      # caramel macchiato
specials[1] = 'drip'
print(specials[1])      # drip
```

可订阅的集合类实现了特殊方法`__getitem__()`、`__setitem__()`和`__delitem__()`，
其中每个方法都接收一个整型参数。可以通过直接使用特殊方法而非方括号来查看效果。

```python
specials = ['pumpkin spice latte', 'caramel macchiato', 'macho cappuccino']
# 使用特殊方法来访问和修改元素
print(specials.__getitem__(1))
specials.__setitem__(1, 'drip')
print(specials.__getitem__(1))
```

这些特殊方法由 dict 类实现，只不过他们都接受一个键作为唯一参数。字典因为没有正式
的“索引”，所以不能视为可订阅的集合对象。

## 9.6 切片符

切片符允许我们访问列表或元祖中特定的元素或元素范围。在集合的 5 种基本类型中，只
有元组和列表可以切片。可变集合和字典都不可订阅，所以切片符对它们不起作用。双端队
列虽然是可订阅的，但是由于其实现方式，但也不能使用切片符进行切片。

要获取列表或元组的切片，可以在切片符周围使用方括号，切片符通常由 3 部分组成，以
冒号分隔：

```python
[start:stop:step]
```

要在切片中声明的第一个元素的包含索引是 start。独占索引 stops 则要刚好超过切片停
止的位置。索引 step 允许你跳过元素甚至颠倒顺序。

### 9.6.1 开始和停止

通过指定切片的开始位置和结束位置，可以指定一个范围：

```python
orders = [
    "caramel macchiato",
    "drip",
    "pumpkin spice latte",
    "drip",
    "cappuccino",
    "americano",
    "mocha latte",
]
three_four_five = orders[3:6]
print(three_four_five)      # ['drip', 'cappuccino', 'americano']
```

该切片从索引 3 开始，在索引 6 之前结束，因此包含索引 3~5 处的元素。

切片的一个重要规则：start 必须始终引用 stop 之前的元素。默认情况下，列表是从头到
尾遍历的，所以 start 必须小于 stop。

切片并不需要所有参数。如果省略 start，切片从第一个元素开始；如果省略 stop，切片
将以最后一个元素结束。

如果想要列表中除前 4 个元素之外的所有元素，可以使用如下写法：

```python
after_third = orders[4:]
print(after_third)          # ['cappuccino', 'americano', 'mocha latte']
```

该切片从索引 4 开始，由于没有在冒号后指定 stop 参数，因此该切片包括直至列表末尾
的其余所有元素。

可以通过如下写法，访问列表中的前两项：

```python
next_two = orders[:2]
print(next_two)             # ['caramel macchiato', 'drip']
```

由于没有在冒号前指定 start 参数，因此默认从列表开头开始切片。stop 为 2，所以该切
片包含索引 2 之前的所有元素。

### 9.6.2 负索引

可以使用负数作为索引，这样就可以从列表或元组的末尾开始遍历。例如，索引-1 指的是
列表中的最后一项：

```python
print(orders[-1])           # mocha latte
```

负索引也适用于切片。例如，如果想得到列表末尾的 3 个订单，可以使用如下写法：

```python
# 获取末尾的3个元素
last_three = orders[-3:]
print(last_three)           # ['cappuccino', 'americano', 'mocha latte']
```

请记住，start 索引必须始终在 stop 索引前，默认情况下，列表是从左到右遍历的。因此
，起点必须是-3，即倒数第三个订单；终点必须是-1.

### 9.6.3 步长

默认情况下，列表从头到尾完成遍历，从最小索引到最大索引，一个接一个。切片符的
step 参数允许我们更改此行为，以便更好地控制切片中包含哪些值以及值的顺序。

例如，可以通过将 step 设置为 2，创建一个每隔一个元素去一次值的咖啡订单的切片，该
切片从第二个订单开始：

```python
# 指定步长为2，实现每个一个元素取一项
every_order = orders[1::2]
print(every_order)          # ['drip', 'drip', 'americano']
```

以上代码从索引 1 开始切片。由于没有指定 stop 索引，切片会持续到列表的末尾。step
为 2 表示切片每隔一个元素进行取值。对于订单列表，这意味着切片由索引 1、3、5 处的
元素组成。

负的步长会反转列表或元组的读取方向。例如，将 step 设为-1，不指定 start 隔 stop，
将返回整个订单列表的反转版本。

```python
reverse = orders[::-1]
print(reverse)              # ['mocha latte', 'americano', 'cappuccino', 'drip', 'pumpkin spice latte', 'drip', 'caramel macchiato']
```

我们能够注意到-1 的前面有两个冒号，这是为了声明没有为 start 或 stop 指定任何值。
否则，Python 将无法知道-1 是针对 step 参数的。

### 9.6.4 切片复制

关于切片的另外一件事就是它们总是返回一个包含所选元素的新列表或元组，原始列表或元
组仍然存在。如下所示代码将创建一个列表的完美浅副本。

```python
order_copy = orders[:]
orders.append('the end item')
print(order_copy)           # ['caramel macchiato', 'drip', 'pumpkin spice latte', 'drip', 'cappuccino', 'americano', 'mocha latte']
print(orders)               # ['caramel macchiato', 'drip', 'pumpkin spice latte', 'drip', 'cappuccino', 'americano', 'mocha latte', 'the end item']
```

由于既没有指定 start 也没有指定 stop，因此这个切片包含所有元素。

### 9.6.5 切片对象

还可以使用初始化方法 slice() 直接创建切片对象，以便复用。

```python
my_slice = slice(3, 5, 2)       # 等价与 [3:5:2]
print(my_slice)
```

对应的 start、stop 和 step 作为位置参数传递进来。实际上这种方法比常规切片符的使
用限制更多，因为这种形式无法省略 stop 值。

但无论如何，现在可以使用 my_slice 代替切片符，并直接用在 print() 语句中。

### 9.6.6 对自定义对象切片

如果想在自己的对象中实现切片，只需要将切片对象作为所需操作的特殊方法的参数即可，
比如 `__getitem__(self, sliced)`、`__setitem(self, sliced)`和
`__delitem(self, sliced)`。然后就可以通过 sliced.start、sliced.stop 和
sliced.step 获得切片对象关键的 3 个部分。

### 9.6.7 使用 islice()

我们仍然可以使用 itertools.islice()对双端队列或任何不可订阅的集合进行切片，其行
为和切片符相同，只是不支持任何负值参数。

```python
islice(collection, start, stop, step)
```

例如，islice()可以从字典中取出一个切片，但不能用普通的切片符来切片，因为没有索引
可用。在此，从 menu 字典中每隔一个元素取出一个元素：

```python
from itertools import islice

menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}
# 在字典的items视图中，从索引0开始到索引为3的范围内，每各一个元素取一个
menu = dict(islice(menu.items(), 0, 3, 2))
print(menu)     # {'drip': 1.95, 'americano': 2.49}
```

以上代码将 menu 字典作为元组列表传递给 islice()，然后传递 start、stop 和 step 参
数值以每隔一个元素取出一个元素，最后通过 islice()创建一个新字典将其绑定到 menu。

## 9.7 in 运算符

可以使用 in 运算符快速检查特定值是否包含在指定的集合中。

```python
orders = [
    "caramel macchiato",
    "drip",
    "pumpkin spice latte",
    "drip",
    "cappuccino",
    "americano",
    "mocha latte",
]

if "mocha cappuccino" in orders:
    print("Open chocolate surup bottle.")
```

把要检查的值放在 in 运算符的左侧，要搜索的集合放在 in 运算符的右侧。如果在集合中
找到该值的至少一个实例，则 in 运算符返回 True，否则返回 False。

还可以检查列表是否遗漏特定元素。例如，入股了现在没有人和 drip 咖啡，则不妨关闭咖
啡机。

```python
if 'drip' in orders:
    print("Shut off percolator.")       # Shut off percolator.
```

追加 not 能反转 in 条件。因此，如果在集合中找不到该值，则表达式的计算结果为
True。

可以通过实现特殊方法 `__contains__()` 来为自定义类追加对 in 运算符的支持。

## 9.8 检验集合的长度

要想知道一个集合中包含多少个元素，可以使用 len() 函数。

```python
customers = ['Glen', 'Todd', 'Newman']
print(len(customers))       # 3
```

len 函数以整数形式返回 customers 中的元素数量。由于 customers 中有 3 个元素，因
此返回值为 3。对于字典，len()将返回键值对的数量。

进行迭代时，使用 len() 的次数将比预期的少，这改变了集合的遍历方式，毕竟这样就很
少需要知道集合的具体长度了。

在测试集合是否为空时，甚至不需要使用 len()函数。集合如果包含内容，则是“真实的”，
这意味着计算结果为 True。否则，集合如果为空，则是“虚假的”，这也就意味着计算结果
为 False。

```python
customers = []

if customers:
    print("There are customers.")
else:
    print("Quiet day.")

print(bool(customers))

# Quiet day.
# False
```

customers 是空的，在用作表达式时，计算结果为 False。如果直接将 customers 当成布
尔值，就会输出 False。

通常，只有当需要将集合的长度作为数据本身的一部分时，才使用 len()。

```python
orders_per_day = [56, 41, 49, 22, 71, 43, 18]
average_orders = sum(orders_per_day) // len(orders_per_day)     # 向下取整
print(average_orders)       # 42
```

## 9.9 迭代


