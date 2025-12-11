# 第 10 章 生成器和推导式

我们摆脱了传统的基于索引的循环的所有麻烦。然而，我们还没能完全摆脱嵌套循环。

解决方式是使用生成器表达式，它允许我们在一个语句中重写循环的整个逻辑，我们甚至可
以使用广受欢迎的列表推导式创建列表。

## 10.1 惰性求值和贪婪迭代

虽然迭代器是惰性的，但是可迭代对象却不是惰性的！

```py
import time

sleepy = ['no pause', time.sleep(1), time.sleep(2)]
print(sleepy[0])    # 终止 3秒，再执行输出语句
```

## 10.2 无限迭代器

惰性求值使得无限迭代器称为可能，这样就可以按需提供值且不会被耗尽。

itertools 模块提供了以下 3 种无限迭代器：

- count() 从给定的数值开始计数，每次加上可选的步长值。因此，count(5, 2)将永远产
  生 5、7、9、11 等值。
- cycle()无限循环遍历给定可迭代对象中的每个元素。因此，cycle([1, 2, 3])将产生
  1、2、3、1、2、3，且将已知持续下去。
- repeat()会无限地重复给定的值，或重复指定次数（可选）。因此，repeat(42)将持续生
  成 42，repeat(42, 10)将生成 10 个 42。

使无限迭代器有用的行为也令其变得危险：无限迭代器没有“刹车”！当向其传递没有 break
语句的 for 循环时，循环将变成无限循环；当使用星号表达式解包或用其创建集合时
，Python 解释器会锁定甚至使系统崩溃。请谨慎使用无限迭代器！

## 10.3 生成器

迭代器类的一个强大替代品是生成器函数，除了使用特殊的 yield 关键字以外，生成器函
数看起来就像普通函数。当直接调用生成器函数时，它将返回一个生成器迭代器（又称生成
器对象），该迭代器封装了生成器函数套件中的逻辑。

在每次迭代中，生成器迭代器将运行到一条 yield 语句，然后等待对特殊方法
`__next__()`的另一次调用，该方法是 Python 在幕后隐式创建的。`__next__()`是负责在
迭代器中提供下一个值的特殊方法。只要将迭代器对象传递给 next()函数或 for 循环中使
用，就将调用`__next__()`。生成器迭代器一旦收到对 `__next__()` 的调用，就继续运行
直至遇到下一条 yield 语句。

```py
from itertools import product
from string import ascii_uppercase as alphabet

def gen_license_plates():
    for letters in product(alphabet, repeat=3):
        letters = ''.join(letters)
        if letters == 'GOV':
            continue

        for number in range(1000):
            yield f"{letters} {number:03}"
```

yield 语句令该函数成为生成器。每当程序执行到 yield 语句时，值就被返回，然后生成
器等待对 `__next__()` 的另一次调用。再次调用 `__next__()` 时，生成器会从之前停止
的地方重新开始，从而生成下一个值。

必须调用生成器函数才能创建想要使用的生成器迭代器。将生成器迭代器绑定到一个名称：

```py
license_plates = gen_license_plates()
```

名称 license_plates 现在绑定了由 gen_license_plates() 创建的生成器迭代器，这就是
具有 `__next__()` 方法的对象。

现在可以像对待任何迭代器一样对待 license_plates。

```py
for plate in license_plates:
    print(plate)
```

在现实场景中，一般不要求同时获得所有可能得数字。

```py
from itertools import product
from string import ascii_uppercase as alphabet

def gen_license_plates():
    for letters in product(alphabet, repeat=3):
        letters = ''.join(letters)
        if letters == 'GOV':
            continue

        for number in range(1000):
            yield f"{letters} {number:03}"


license_plates = gen_license_plates()

registrations = {}

def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    else:
        return None
```

我们可以手动跳过几千个车牌号，模拟之前注册的车牌：

```py
# skip_total = (6 * 26 * 26 * 1000) + (14 * 26 * 1000) + (21 * 1000)
skip_total = 4441888
for _ in range(skip_total):
    next(license_plates)

name = 'Jason C. McDonald'
my_plate = new_registration(name)
print(my_plate)
print(registrations[name])
```

程序的输入如下：

```shell
GOW 888
GOW 888
```

### 10.3.1 生成器 vs 迭代器

迭代器类中的 `__next__()`方法能引发 StopIteration 异常，已宣告没有更多元素可迭代
。生成器不需要显示引发异常，更加重要的是，从 Python3.5 开始，甚至已经不允许这么
做了。当生成器函数终止时，无论是否到达末尾还是显示地使用 return 语句，都将在幕后
自动引发 StopIteration 异常。

1. 作为迭代器类

为了证实这一点，编写一个随机生成高速公路车流量的迭代器类。一旦它正常工作，就将其
重写为一个生成器函数。

```py
from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

class Traffic:
    """
    定义迭代器类，模拟车流量
    """

    def __iter__(self):
        """
        不需要初始化器，因为没有实例属性。定义返回self的__iter__()特殊方法，是这个类变成可迭代的
        """
        return self

    def __next__(self):
        """
        为这个类定义__next__()方法，作为迭代器

        如果从列表中随机选取的车是None，将引发StopIteration异常，以指示车流中存在间隙，否则从colors列表中随机选取一种颜色，然后返回一个包含车辆和颜色的格式化字符串
        """
        vehicle = choice(vehicles)


        if vehicle is None:
            raise StopIteration

        color = choice(colors)

        return f"{color} {vehicle}"

count = 0
for count, vehicle in enumerate(Traffic(), start=1):
    print(f"Wait for {vehicle}...")

print(f"Merged after {count} vehicles!")
```

输出如下：

```shell
Wait for white motorcycle...
Wait for green motorcycle...
Merged after 2 vehicles!
```

2. 作为生成器函数：

```py
from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    """
    生成器函数
    """
    while True:
        vehicle = choice(vehicles)
        if vehicle is None:
            return

        color = choice(colors)
        yield f"{color} {vehicle}"


traffic = traffic_generator()

count = 0
for (count, vehicle) in enumerate(traffic, start = 1):
    print(f"Wait for {vehicle} ...")

print(f"Merged after {count} vehicles!")
```

一旦函数返回，无论是隐式地到达终点还是通过 return 语句，迭代器都将在幕后引发
StopIteration。

因为并不知道将随机生成多少车流量，所以我们希望这个生成器先无限期地运行，直至从
vehicles 列表中获得 None。然后并不引发 StopIteration，而是使用 return 语句来退出
函数，以说明迭代已经完成。从 Python 3.5 开始，在迭代器函数中引发 StopIteration
将触发 RuntimeError。

### 10.3.2 生成器关闭

和任何迭代器一样，生成器也可是无限的。然而，用完一个迭代器之后，应该关闭它，因为
让其在内存中闲置对程序的其余部分来说是在浪费资源。

为了证明这一点，将当前的 traffic() 生成器函数重写为无限的。仍然使用之前示例中的
两个列表：

```py
from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    """
    生成器函数，构建一个无限迭代器
    """
    while True:
        vehicle = choice(vehicles)
        # if vehicle is None:
        #     return

        color = choice(colors)
        yield f"{color} {vehicle}"

def car_wash(traffic, limit):
    """
    接受一个无限迭代器，在迭代limit次数之后，关闭迭代器
    """
    count = 0
    for vehicle in traffic:
        print(f"Washing {vehicle}.")
        count += 1
        if count >= limit:
            traffic.close()

# 传入无限迭代器
car_wash(traffic_generator(), 10)
```

以上代码将 traffic 迭代器传递给 car_wash() 函数，同时传递一个整数值来限制可以清
洗的车辆数量。该函数遍历 traffic，清洗车辆并进行计数。

一旦到达限制，traffic 将不可再迭代，所以将其关闭。这将在生成器中引发
GeneratorExit，进而引发 StopIteration——结束循环，从而结束函数。

由于 car_wash() 函数关闭了迭代器，因此无法再将器传递给 next()以获得结果。如下所
示：

```py
# 传入无限迭代器
queue = traffic_generator()
car_wash(queue, 10)
# queue迭代器已经在car_wash函数中被关闭了，所以后续不再支持迭代，继续迭代的话会触发 StopIteration。
next(queue)
```

### 10.3.3 行为关闭

当生成器明确关闭时，可以让生成器做一些其他事情，而不是安静地退出。可以通过捕获
GeneratorExit 异常来实现这一目标：

```py
from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    """
    生成一个无限迭代器
    """

    while True:
        # 没有return逻辑，将变为无限迭代器
        vehicle = choice(vehicles)
        color = choice(colors)
        try:
            yield f"{color} {vehicle}"
        # 通过捕获 GeneratorExit 异常，可以实现在迭代器关闭的时候做一些其他逻辑
        except(GeneratorExit):
            print("No more vehicles.")
        raise

def car_wash(traffic, limit):
    count = 0
    for count, vehicle in enumerate(traffic, start=1):
        print(f"Washing {vehicle}.")

        if count + 1 > limit:
            traffic.close()

car_wash(traffic_generator(), 10)
```

将 yield 语句包裹在 try 语句中。当 traffic.close() 被调用时，生成器等待的
GeneratorExit 异常就被触发。我们可以捕获次异常，并做我们想做的任何事情，例如输出
一条消息。最重要的是，必需触发 GeneratorExit 异常，否则生成器永远不会关闭！

### 10.3.4 异常报出

生成器的一种很少使用的功能是 throw() 方法，用来将生成器置于某种异常状态，特别是
当需要执行一些超出常规 close()的特殊操作时。

其实和 close()引发 GeneratorExit 的方式类似，事实上，close()在功能上和
throw(GeneratorExit)相同。

尽管这听起来非常有用，但 throw()在现实世界中并没有那么多用例。

下面使用 traffic() 生成器编写一个示例来演示这种行为。现捕获 ValueError 以允许跳
过车辆，这将是后文使用 throw()方法在 yield 语句中引发的异常。

```py
from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    while True:
        vehicle = choice(vehicles)
        color = choice(colors)
        try:
            yield f"{color} {vehicle}"
        except ValueError:
            # 跳过指定车辆，跳过逻辑又上层函数控制
            print(f"Skipping {color} {vehicle}...")
            continue
        except GeneratorExit:
            print("No more vehicles.")
            raise

def wash_vehicle(vehicle):
    # 如果当前车辆包含 semi ，则抛出异常，交由上层函数处理
    if 'semi' in vehicle:
        raise ValueError("Cannot wash vehicle.")
    print(f"Washing {vehicle}.")


def car_wash(traffic, limit):
    count = 0
    for vehicle in traffic:
        # 此处捕获 wash_vehicle抛出的 ValueError，通过traffic.throw(ValueError)，将异常传递到生成器内部，触发ValueError，实现skip逻辑
        try:
            wash_vehicle(vehicle)
        except Exception as e:
            traffic.throw(e)
        else:
            count += 1

        if count >= limit:
            traffic.close()

car_wash(traffic_generator(), 10)
```

在生成器的 yield 语句中引发 ValueError 异常，该异常将被捕获，并且生成器将宣布当
前车辆被忽略，然后进入其无限循环的下一次迭代。

在将洗车的逻辑抽象到 wash_vehicle() 函数中时，这才真正有用。wash_vehicle() 函数
内部将引发异常。

wash_vehicle()检验到 semi 是否被要求清洗时，如果被要求清洗，则引发 ValueError。

## 10.5 生成器表达式

生成器表达式是一个迭代器，它能将生成器的整个逻辑封装到一个表达式中。生成器表达式
是惰性的，因此可以用来处理大量数据而无需锁定程序。

下面是一个使用循环生成 ABC 和 3 个数字组成的车牌号：

```py
def license_plates():
    for num in range(1000):
        yield f"ABC{num: 03}"

for plate in license_plates():
    print(plate)
```

现在使用生成器表达式重写上述案例：

```py
# 使用生成器表达式生成迭代器
license_plates = (f"ABC {num:03}" for num in range(1000))

for plate in license_plates:
    print(plate)
```

现在生成器表达式包含在括号中，并被绑定到名称 license_plates。生成器表达式本质上
是循环语句的反转。

在生成器表达式中，首先声明前面循环套件中的逻辑，在其中定义一个将在每次迭代中进行
计算的表达式。然后创建一个由字母 A、B、C 和迭代中当前数字组成的字符串，如果它不
是三位数，在其左侧用 0 填充。和 lambda 表达式中的 return 类似，生成器表达式中的
yield 也是隐含的。

接下来声明循环本身，和以前类似，对一个 range()可迭代对象进行迭代，在每次迭代中使
用 numb 作为值。

输出结果和使用生成器函数一样。

### 10.5.1 生成器对象都是惰性的

生成器对象都是惰性的，无论其是由生成器函数生成的还是由生成器表达式生成的。这意味
着生成器对象会按需产生值，而不是提前准备。

```py
sleepy = (time.sleep(t) for t in range(0, 3))
```

和列表不同，列表的定义导致程序在继续之前将休眠 3 秒，因为每个元素都在定义时进行
了计算。这段代码会立即运行，因为它推迟了对其值的运算，直至有需要时才计算。定义生
成器表达式本身不会执行 time.sleep()。

即使手动迭代第一个值，也不会产生延迟：

```py
sleepy = (time.sleep(t) for t in range(0, 3))

print("Calling...")
next(sleepy)
print("Done!")
```

因为 time.sleep(0)在生成器表达式的第一次迭代中被调用过，所以 next(sleepy)立即返
回。而对 next(sleepy) 的后续调用将导致程序休眠。

### 10.5.2 生成器表达式具有复合循环

生成器表达式一次可以支持多个循环，并复制嵌套循环的逻辑，循环按从最外层到最内层的
顺序列出。

重写车牌号生成器表达式，以生成所有可能的字母和数字组合，从 AAA 000 开始到 ZZZ
999 结束。因为生成器表达式是惰性的，所以生成数据很快，这些值在被请求之前不会真正
创建。

```py
# 使用复合循环结构的生成器表达式生成车牌号
from itertools import product
from string import ascii_uppercase as alphabet

license_plates = (f"{''.join(letters)} {num:03}"
                  for letters in product(alphabet, repeat=3)
                  for num in range(1000))
```

以上代码在生成器表达式中使用了两个循环。第一个循环通过 itertools.product() 遍历
3 个字母的所有可能组合。product 迭代器在每次迭代时生成一个元组，必须在创建格式化
字符串时使用"".join()将其连接为一个字符串。第二个循环迭代了 0 到 999 之间的所有
数字。

在每次迭代中，都使用 f-字符串来生成车牌号。结果是一个绑定到 license_plates 的迭
代器，可以延迟生成所有可能的车牌号。在被请求之前，不会创建下一个车牌号。

### 10.5.3 生成器表达式中的条件

可以在生成器表达式中追加一个条件来实现条件判断：

```py
license_plates = (f"{''.join(letters)} {num:03}"
                  for letters in product(alphabet, repeat=3)
                  if letters != ('G', 'O', 'V')
                  for num in range(1000))
```

以上代码追加了如下条件：如果元组 letters 的值不是('G', 'O', 'V')，则使用此值，否
则跳过迭代（隐式地执行 continue 语句）。

这里的顺序非常重要！循环和条件从上到下进行计算，就行是嵌套在一起。如果在生成数字
后检查('G', 'O', 'V')，则在 1000 个单独的迭代中隐式地调用 continue 语句，但由于
这发生在第二个循环之前，因此数字永远不会在('G', 'O', 'V')情况下生成，生成器表达
式在第一个循环中就继续执行了。

这种语法一开始可能令人感觉有点麻烦。可以将其视为嵌套循环，原本处在末尾的 yield
被提取出来并放在最前面。用嵌套循环写的等效生成器函数如下：

```py
def generate_license_plates():
    for letters in product(alphabet, repeat=3):
        if letters != ('G', 'O', 'V'):
            for num in range(1000):
                yield f"{"".join(letters)} {num:03}"
```

对比前述代码，可以看到最后一行被移到了最前面，删除了 yield 关键字，因为它隐含在
生成器表达式中。还需要删除每一行的冒号。这种编写生成器表达式的方式有助于确保我们
的逻辑合理。

虽然也可以在生成器表达式中使用 if-else，但是有一个问题：这和仅使用 if 的效果并不
相同！

以下是使用生成器函数实现：

```py
# 使用三元表达式
def generate_divis_by_three():
    for n in range(100):
        yield n if n % 3 == 0 else 'redacted'
```

其中使用了三表达式实现返回值计算。三元表达式遵循"a if expression else b"的形式。
如果 expression 的计算结果为 True，则三元表达式的计算结果为 a，否则为 b。三元表
达式可以出现在任何地方，如赋值语句和返回语句中。但是在大多数情况下，并不鼓励使用
三元表达式，因为其实在难以阅读。三元表达式主要用于 lambda 表达式和生成器表达式，
毕竟在这种场景中使用完成的条件语句是不可能的。

转换为生成器表达式实现：

```py
# 改为含有三元表达式的生成器表达式
divis_by_three = (n if n % 3 == 0 else 'redacted' for n in range(100))
```

但是如果使用 if 语句但删除 else 语句，则会遇到问题：

```py
divis_by_three = (n if n % 3 == 0 for n in range(100))
```

运行后将返回以下结果：

```bash
SyntaxError: expected 'else' after 'if' expression
```

没有 else 语句就不是三元表达式。

### 10.5.4 嵌套生成器表达式

和生成器函数不同，生成器表达式仅在嵌套的句子复合语句中使用，因此只有一个顶级循环
。可以通过将一个生成器表达式嵌套在另一个生成器表达式中来解决这个问题。但是实际上
相当于编写两个单独的生成器表达式，并让其中一个使用另一个。

```py
# 使用复合的生成器表达式
license_plates = (f"{letters} {num:03}"
                  for letters in ("".join(chars) for chars in product(alphabet, repeat=3))
                  if letters != 'GOV'
                  for num in range(1000)
                  )
```

内部嵌套的生成器表达式处理 product()迭代的结果，将 3 个字母连接为一个字符串。
