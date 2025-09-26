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
及与集合论相关的各种操作，尤其实在大型数据集中。

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
