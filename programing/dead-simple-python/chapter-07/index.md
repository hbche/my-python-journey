# 第 7 章 类和对象

## 7.1 声明一个类

```python
class SecretAgent:
```

在 Python 中，一切皆对象，因为一切都继承自 object 类。在 Python 3 中，这种从
object 类开始的继承是隐式的。

我们通常省略显示继承 object 的部分；下面显示继承 object 与上面的代码等效：

```python
class SecretAgent(object):
```

### 7.1.1 初始化器

一个类通常有一个初始化器来定义实例属性的初始值，这些实例属性是每个实例中都存在的
成员变量。如果实例没有实例属性，则不需要定义 `__init__()`。

SecretAgent 类的每个实例都有一个代号和一个秘密列表，因此 SecretAgent 类的初始化
器有两个实例属性，如下所示：

```python
class SecretAgent:

    def __init__(self, codename):
        self.codename = codename
        self._secrets = []
```

初始化器必须具有名称 `__init__`才能被识别为初始化器，并且必须至少接收一个参数，
通常名为 self。这个 self 参数引用方法正在操作的实例。

在这个例子中，初始化器还接收了第二个参数 codename，并将它用作实例属性之一的初始
值。这个 self.codename 属性是秘密代理的代号。

实例属性是实例本身的一部分，因此必须通过对 self 使用点运算符（.）来访问它们。所
有实例属性都应该在初始化器中声明，而不是在其他实例方法中动态声明。因此，将
self.\_secrets 定义为一个空列表，这将是特定秘密代理（实例）所保持的秘密列表。

最后，初始化器不应该通过 return 关键字返回值。如果这样做，调用初始化器将引发
TypeError。但如果需要的话，也可以单独使用 return 关键字来显式地退出方法。

最后，初始化器不应该通过 return 关键字返回值。如果这样做，调用初始化器将引发
TypeError。但如果需要的话，也可以单独使用 return 关键字来显式地退出方法。如下所
示：

```python
from secret_agent import SecretAgent

mouse = SecretAgent('Mouse')
armadillo = SecretAgent('Armadillo')
fox = SecretAgent('Fox')
```

以上代码导入了 SecretAgent 类并创建了 3 个新实例。我们注意到不需要传递任何内容给
第一个参数 self，这是在幕后处理的。相反，实参"Mouse"被传递给初始化器的第二个参数
codename。每个实例还有自己的空列表\_secrets。

### 7.1.2 构造器

如果我们熟悉 C++、Java 或其他类似的语言，我们可能会希望编写一个构造函数——一个构
造类实例的函数，或者我们可能认为初始化器与构造函数执行相同的操作。实际上，Python
3 将典型构造函数的职责分解为初始化器`__init__()`和构造函数`__new__()`两部分。在
Python 中，构造函数`__new__()`负责实际在内存中创建实例。当创建一个新实例时，首先
调用构造函数，然后调用初始化器。构造函数是在对象创建之前自动调用的类中的唯一方法
！

通常不需要定义构造函数，Python 会自动提供。只有当需要对过程进行额外控制时，才需
要创建构造函数。

```python
def __new__(cls, *args, **kw_args):
    return super().__new__(cls, *args, **wk_args)
```

构造器总是具有名称`__new__`，并且它隐式接收一个类作为第一个参数 cls（而初始化器
接收类实例作为参数 self）​。由于初始化器接收参数，因此还需要让构造函数准备好接收
这些参数，同时使用可变参数捕获这些参数并将它们传递给初始化器。

构造器必须返回创建的类实例。从技术上讲，我们可以在这里返回你想要的任何东西，但预
期的行为通常是返回 SecretAgent 类的实例。要做到这一点，就需要调用父类
的`__new__()`函数，我们可能还记得 SecretAgent 类的父类是 object。

在实践中，如果这是构造函数需要做的所有事情，那就省略它！如果没有为其编写任何代码
，Python 将自动处理构造函数的行为。只有在需要控制类的实例化行为时才编写构造函数
。不过，这种情况很少见，我们完全有可能在整个 Python 编程生涯中都不必编写构造函数
。

### 7.1.3 终结器

终结器在类实例的生命周期结束且类实例由垃圾回收器清理时被调用。它仅用于处理特定类
可能需要的复杂清理。与构造函数一样，我们很少需要自己编写终结器。重要的是要理解：
只有在类实例（值）本身由垃圾回收器清理时，终结器才会被调用！

只要任何对类实例的引用仍然存在，就不会调用终结器。此外，垃圾回收器可能不会在我们
期望的时候清理类实例，这取决于所使用的 Python 实现。

因此，我们仅在与垃圾回收类实例直接相关的代码中使用终结器。它不应该包含任何需要在
其他情况下运行的代码。

```python
class SecretAgent:

    # 初始化器
    def __init__(self, codename):
        self.codename = codename
        self._secrets = []

    # 终结器
    def __del__(self):
        print(f"Agent {self.codename} has been disavowed!")
```

终结器总是具有名称`__del__`，并且接收一个参数 self。它不返回任何内容。

为了演示终结器的用法，下面创建并手动删除一个实例。可以使用 del 关键字删除名称，
从而解除名称与值的绑定。给定具有终结器的 SecretAgent 类，可以创建并删除一个引用
类实例的名称，如下所示：

```python
from secret_agent import SecretAgent

weasel = SecretAgent('Mouse')
del weasel
```

以上代码创建了一个新的 SecretAgent 类实例，并将其绑定到名称 weasel 上，然后立即
使用 del 关键字删除该名称。名称 weasel 现在是未定义的。由于不存在对名称绑定的
SecretAgent 类实例的引用，因此该实例由垃圾回收器清理，垃圾回收器首先调用终结器。

请注意，del 只删除名称，而不删除值！如果有多个名称被绑定到同一个值，并且如果只删
除其中一个名称，则其他名称及其值不受影响。换句话说，del 不会强制垃圾回收器删除对
象。

## 7.2 属性

所有属于类或实例的变量都称为属性（attribute）​。属于实例本身的属性称为实例属性，
有时也称为成员变量。属于类本身的属性称为类属性，有时也称为类变量。

### 7.2.1 实例属性

实例属性属于实例本身，其值对于相应实例是唯一的，对于其他实例不可用。所有实例属性
都应声明在类的初始化器中。

### 7.2.2 类属性

类属性属于类本身，而不属于某个实例。实际上，这意味着所有相关的类实例“共享”类属性
。即使没有任何实例，类属性也依然存在。

类属性声明在类的顶部。可以直接将一个类属性添加到类的套件中，如下所示：

```python
class SecretAgent:
    # 初始化类属性
    _codeword = ""

    # 初始化器，初始化实例属性
    def __init__(self, codename):
        self.codename = codename
        self._secrets = []
```

属性 `_codeword` 属于 SecretAgent 类。通常，所有类属性都在方法之前声明，以便更容
易找到它们，但这只是惯例。重要的是，它们是在方法之外定义的

类属性可以如下所示进行访问：

```python
from secret_agent import SecretAgent

mouse = SecretAgent('Mouse')
SecretAgent._codeword = "Parmesan"
print(SecretAgent._codeword)        # Parmesan
print(mouse._codeword)              # Parmesan
# 针对实例的_codeword进行赋值操作时，会在实例上直接创建一个同名的实例属性，而不会影响类属性，同时实例实行会屏蔽类属性
mouse._codeword = "Cheese"
print(SecretAgent._codeword)        # Parmesan
print(mouse._codeword)              # Cheese
```

可以直接通过类或类的任何实例访问类属性 `_codeword`。如果在类本身中重新绑定或更改
类属性，那么更改将出现在所有情况下。但是，如果将值分配给实例的名称，则会创建具有
相同名称的实例属性，该实例属性会在实例中覆盖类属性，而不会影响其他实例。

类属性对于类的方法所使用的常量值特别有用。在许多情况下，它们比全局变量更加实用且
可维护，尤其是在图形用户界面（Graphical User Interface, GUI）编程中。

## 7.3 作用域命名约定

实际上，Python 没有正式的数据隐藏概念。

### 7.3.1 非公共属性

通过在属性名称前加下画线（如\_secrets）可声明该属性是非公共的，这意味着它不应该
在类之外被修改（最好也不应该在类之外被访问）​。这更像是一种通过风格约定的契约，
实际上没有隐藏任何东西。

### 7.3.2 公共属性

公共属性 codename 不以下画线开头。它可以在外部被访问或修改，因为它不会真正影响类
的行为。公共属性优于编写一个普通的 getter/setter 方法对。它们的作用是相同的，但
公共属性的结果更干净，样板代码也更少。

如果属性需要自定义 getter 或 setter，一种方法是将属性定义为非公共的，并创建一个
公共特性（property）​。

### 7.3.3 名称修饰

Python 提供了名称修饰功能来重写属性或方法的名称，以防止它们被派生类（继承类）覆
盖。这是一种形式较弱的数据隐藏功能，它还可以用于提供额外的警告级别：​“如果你弄乱
了这个属性，会发生很糟糕的事情！”

为了标记属性（或方法）以进行名称修饰，请在名称前加两个下画线（`__`）​，如下所示
：

```python
class Message:
    def __init__(self):
        self.__format = "UTF-8"
```

`__format` 属性的名称被修饰了，因此以常规的方式在外部访问它将不起作用，如下所示
：

```python
msg = Message()
print(msg.__format)     # AttributeError: 'Message' object has no attribute '__format'. Did you mean: '__format__'?
```

这将引发 AttributeError，因为 msg 实例没有名为\_\_format 的属性，那个属性的名称
被修饰了。请注意，名称修饰不是真正的数据隐藏！你仍然可以访问经过名被修饰的属性，

```python
msg = Message()
print(msg._Message__format) # UTF-8
```

名称修饰的模式是可预测的：一个下画线、类的名称，然后是属性的名称（它有两个前导下
画线）​。

### 7.3.4 公共属性、非公共属性，还是名称修饰符

在决定使一个属性成为公共属性或非公共属性时，你可以问自己一个问题：从外部修改属性
是否会导致类中出现意外或负面行为？如果答案是肯定的，就通过在属性前加一个下画线来
使属性成为非公共属性；如果答案是否定的，则使属性成为公共属性。这取决于使用类的编
码人员是否遵守规则或承担后果。

至于名称修饰，实践中则很少使用这种模式。建议只在以下情况下使用它：需要避免继承中
的命名冲突；从外部访问属性将对类的行为产生异常可怕的影响，因此需要发出额外的警告
。

请记住，Python 没有私有类作用域。真正的秘密数据应该被正确加密，而不是仅对 API 隐
藏。与 Java 等语言不同，Python 没有私有类作用域的优化好处，因为所有属性查找都发
生在运行时。

## 7.4 方法

一个类如果没有方法就一无所有。类的方法使封装成为可能。有 3 种不同类型的方法：实
例方法、类方法和静态方法。

### 7.4.1 实例方法

实例方法是普通方法，它们属于实例本身。实例方法的第一个参数（通常名为 self）提供
对实例属性的访问。

像 SecretAgent 类添加一个实例方法，如下所示：

```python
    # 实例方法
    def remember(self, secret):
        self._secrets.append(secret)
```

除了必需的第一个参数，实例方法还接收第二个参数 secret，该参数将被添加到绑定了实
例属性 `_secrets` 的列表中。

对实例使用点运算符调用这个实例方法，如下所示：

```python
mouse.remember('42.864025, -72.568511')
```

点运算符隐式地将 mouse 传递给 self 参数，因此坐标元组（请注意额外的括号）被传递
给 remember()实例方法的第二个参数 secret。

### 7.4.2 类方法

和类属性一样，类方法属于类，而不属于类的某个实例。这对于使用类属性很好用。

将`_codeword`定义为类属性，这样所有 SecretAgent 实例都能够了解这个属性。为了告知
所有 SecretAgent 实例新的`codeword`，添加一个类方法`inform()`，用于修改类属
性`_codeword`，如下所示：

```python
    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword
```

以上代码在类方法上使用了@classmethod 装饰器。类方法将类作为其第一个参数接收，因
此第一个参数被命名为 cls。类属性（如`_codeword`）是通过传递给 cls 的类进行访问的
。

这带来的一个好处是，不用再担心在类上还是在实例上调用 inform()方法。由于该方法是
一个类实例，它将始终在类（cls）而不是实例（self）上访问类属性，从而避免意外地在
某个实例中隐藏`_codeword`。

这里不打算为此属性添加 getter。毕竟，SecretAgent（秘密代理）必须保密！

我们调用这个类方法，如下所示：

```python
from secret_agent import SecretAgent

mouse = SecretAgent('Mouse')
fox = SecretAgent('Fox')
SecretAgent.inform("The goose honks at midnight.")
print(mouse._codeword)          # The goose honks at midnight.

fox.inform("The duck quacks at midnight.")
print(mouse._codeword)          # The duck quacks at midnight.
```

inform()类方法既可以直接在 SecretAgent 类上调用，也可以在任何 SecretAgent 实例（
如 fox）上调用。inform()对类属性 `_codeword` 所做的更改会出现在类本身及其所有实
例上。

当使用点运算符调用类方法时，类将隐式地被传递给 cls 参数。该参数名称仍然只是一个
约定，@classmethod 装饰器确保第一个参数始终是类而不是实例。

类方法的一个很棒的用法是作为初始化实例的替代方法使用。例如，内置的整数类提供了
int.from_bytes()类方法，它使用字节值初始化一个新的 int 类实例。

### 7.4.3 静态方法

静态方法是定义在类中的常规函数，其不访问实例属性或类属性。

静态方法和普通函数之间唯一的区别是静态方法属于类的命名空间。

当我们的类提供了一些不需要访问任何类属性、实例属性或方法的功能时，可以使用静态方
法。例如，我们可能会为了处理一些特别复杂的算法而编写一个静态方法，该算法对于类的
实现至关重要。通过将静态方法包含在类中，可表明该算法是类的自包含实现逻辑的一部分
，即使它不访问任何属性或方法。

添加一个静态方法到 SecretAgent 类，它要做的事情是回答问题，如下所示：

```python
    @staticmethod
    def inquire(question):
        print("I konw nothing.")
```

以上代码在静态方法的前面加上了@staticmethod 装饰器。不需要担心第一个参数，因为该
方法不需要访问任何属性。当在类或实例上调用此方法时，它只会输出消息“I know
nothing”​。

```python
from secret_agent import SecretAgent

mouse = SecretAgent('Mouse')
SecretAgent.inquire("Have you learned Python?")     # I konw nothing.
mouse.inquire("What is this?")                      # I konw nothing.
```

## 7.5 特性

特性（property）是一种特殊的*实例方法*，它允许我们编写 getter 和 setter，使其看
起来像是可以直接访问实例的属性。特性允许我们编写一致的接口，在这样的接口中我们可
以通过看起来像是对象的属性的形式来直接使用对象。

建议使用特性，而不是让用户记住是调用方法还是使用属性。相比使用不增强属性访问或修
改功能的 getter 和 setter 来填充类，使用特性也更加符合 Python 惯用法。

### 7.5.1 设置场景

为了演示特性的作用，使用一个没有 getter 的特性扩展 SecretAgent 类。

```python
class SecretAgent:

    _codeword = None

    def __init__(self, codename):
        # 初始化实例属性
        self.codename = codename
        self._secrets = []

    def __del__(self):
        print(f"Agent {self.codename} has been disavowed!")

    def remember(self, secret):
        self._secrets.append(secret)

    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword

    @staticmethod
    def inquire(question):
        print("I konw nothing.")

    @classmethod
    def _encrypt(cls, message, *, decrypt=False):
        # 声明了一个加密解密的类方法，结合类属性`_codeword`对传入的message字符串进行加密解密
        # 使用 sum 计算 _codeword 中每个字符对应的Unicode编码的总和，作为后续message中每个字符的加密、解密偏移量
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
            # 遍历message中的每个字符，计算每个字符的Unicode编码值，在原始编码值基础上进行加密解密偏移
            # 将偏移后的Unicode转换成对应的字符返回
        return "".join(chr(ord(m) + code) for m in message)
```

以下是演示加密解密方法：

```python
from secret_agent_property import SecretAgent

message = "Have you learned Python?"
mouse = SecretAgent('Mouse')
# 必须调用 infom 执行 _codeword 否则 encrypt 方法会报错
SecretAgent.inform('Admin')
encrypt_message = SecretAgent._encrypt(message, decrypt=False)
print(encrypt_message)      # ȱɊɟɎȉɢɘɞȉɕɎɊɛɗɎɍȉȹɢɝɑɘɗȨ
decrypt_message = mouse._encrypt(encrypt_message, decrypt=True)
print(decrypt_message)      # Have you learned Python?
```

> 建议使用特性，而不是让用户记住是调用方法还是使用属性。相比使用不增强属性访问或
> 修改功能的 getter 和 setter 来填充类，使用特性也更加符合 Python 惯用法。

### 7.5.2 定义一个特性

特性（property）和属性（attribute）类似，但特性由 3 个实例方法组成
：getter、setter 和 deleter。记住，对类的用户而言，特性看起来就像普通的属性一样
。访问特性需要调用 getter，将值分配给特性需要调用 setter，使用 del 关键字删除特
性则需要调用 deleter。

和普通的 getter 或 setter 方法一样，特性可以访问或修改一个或多个属性，甚至根本不
访问或修改属性。这取决于我们想要做什么。

为 SecretAgent 类定义一个名为 secret 的特性，将其作为 `_secrets` 实例属性的
getter、setter 和 deleter。这种方法将允许你添加逻辑，例如让 setter 在将数据存储
到 `_secrets` 的属性之前对其进行加密。

在定义特性之前，需要定义组成特性的 3 个实例方法。从技术上讲，可以随意命名它们，
但惯例是将它们命名为 getx、setx 和 delx，其中 x 是特性的名称。这里将它们定义为非
公共方法，因为我希望直接使用特性。

首先定义 getter，如下所示：

```python
    def _getsecret(self):
        return self._secrets[-1] if self._secrets else None
```

`_getsecret()` 不接收参数并且应该返回特性的值。在这个例子中，我们想让 getter 返
回绑定到实例属性 `self._secrets` 的列表中的最后一项，如果列表为空，则返回 None。

其次定义 setter，代码如下：

```python
    def _setsecret(self, value):
        self._secrets.append(self._encrypt(value))
```

`_setsecret()` 接收一个参数，该参数接收在调用中分配给特性的值。在本例中，假设这
是某种字符串，可通过之前定义的静态方法\_encode()对它进行编码，然后将其存储在
`self._secrets` 中。

接下来定义 deleter，代码如下：

```python
    def _delsecret(self):
        self._secrets = []
```

`_delsecret()` 不接收参数并且不返回任何值。当特性被删除时，无论是在后台被删除、
由垃圾回收器删除，还是使用`del secret`显式地删除，这个方法都会被调用。在这个例子
中，当特性被删除时，我们希望整个 secret 列表被清除。

最后定义特性本身，如下所示：

```python
    # 声明特性
    secret = property(fget=_getsecret, fset=_setsecret, fdel=_delsecret)
```

> 特性声明必须在 getter、setter 和 deleter 之后，否则 property 函数将报错找不到
> 指定的 fget、fset 和 fdel。

特性属于类本身，在 `__init__()` 方法之外，且在类的组成方法之后定义。分别将 3 个
实例方法传递给 fget、fset 和 fdel 关键字参数（也可以将它们以相同的顺序作为位置参
数进行传递）。将特性绑定到名称 secret，secret 将成为特性的名称。

这个特性现在可以像实例属性一样被使用，如下所示：

```python
from secret_agent_property import SecretAgent

mouse = SecretAgent("Mouse")
mouse.inform("Parmesano")
print(mouse.secret)         # None
mouse.secret = "12345 Main Street"
print(mouse.secret)         # ϗϘϙϚϛφϳЇЏДφϹКИЋЋК
mouse.secret = "555-1234"
print(mouse.secret)         # ϛϛϛϓϗϘϙϚ

print(mouse._secrets)       # ['ϗϘϙϚϛφϳЇЏДφϹКИЋЋК', 'ϛϛϛϓϗϘϙϚ']
del mouse.secret
print(mouse._secrets)       # []
```

每当我们尝试检索特性的值时，就会调用 getter。而当我们将值分配给特性时，则会调用
setter。没必要记住并显式地调用专用的 getter 或 setter，可以像对待属性一样对待特
性。

回想一下，secret 特性的 deleter 会清除 `_secrets` 列表中的内容。在删除特性之前，
列表中包含两个元素；删除特性后，列表为空。

没必要逐一定义特性的 3 个部分。例如，如果不希望 secret 特性中有一个 getter，可以
从类代码中删除 `_getsecret()`。毕竟，SecretAgent（秘密代理）不应该分享他们的秘密
。

```python
    # 声明特性的setter
    def _setsecret(self, value):
        self._secrets.append(self._encrypt(value))

    # 声明特性的deleter
    def _delsecret(self):
        self._secrets = []

    # 声明特性
    secret = property(fset=_setsecret, fdel=_delsecret)
```

因此，可以给 secret 特性赋值，但不能访问 setter 特性的值，如下所示：

```python
from secret_agent_property import SecretAgent

mouse = SecretAgent("Mouse")
mouse.inform("Parmesano")
mouse.secret = "12345 Main Street"
mouse.secret = "555-1234"

print(mouse.secret)     # AttributeError: property 'secret' of 'SecretAgent' object has no getter
```

给 mouse.secret 赋值的方法和以前一样，因为调用了 setter。

然而，尝试访问值会引发 AttributeError。也可以为 secret 特性写一个总是返回 None
的 getter，但必须记住它返回了这个无用的值。

### 7.5.3 使用装饰器创建特性

创建特性很容易，但是到目前为止所展示的实现方法并不是地道的 Pythonic 方法，因为必
须依靠方法名来提醒我们它们是特性的一部分。幸好还有另一种方法。

Python 提供了一种更简洁的方法来定义特性：使用装饰器。

1. property() 和装饰器

仍然使用 property()函数，但使用装饰器来标记相关的方法。这 种方式可以增强可读性，
主要用于省略 getter 的情况。可以使用特性的名称作为方法 的名称，并依靠装饰器来明
确其作用。

使用这种方式重写 secret 特性：

```python
    # 声明特性
    secret = property()
```

在编写实例方法之前将 secret 定义为特性。由于没有向 property()传递任何参数，因此
secret 特性的 3 个实例方法都默认为 None。接下来添加 getter，如下所示：

```python
    # 声明特性 getter
    @secret.getter
    def secret(self):
        return self._secrets[-1] if self._secrets else None
```

使用装饰器声明的 getter，getter 现在必须与特性具有相同的名称，即 secret。如果不
这样的话，当 getter 第一次被调用时就会引发 AttributeError，而不是在创建类时失败
。方法被装饰器 @secret.getter 修饰，这将其指定为特性的 getter，就像将它传递给
property(fget=)一样。

然后是 setter，如下所示：

```python
    # 声明特性 setter
    @secret.setter
    def secret(self, value):
        self._secrets.append(value)
```

类似的，setter 也必须与特性具有相同的名称，并且被装饰器@secret.setter 修饰。

最后是 deleter，如下所示：

```python
    # 声明特性 deleter
    @secret.deleter
    def secret(self):
        self._secrets = []
```

类似于 getter 和 setter, deleter 被装饰器@secret.deleter 修饰。

2. 纯装饰器

另一种更好的方式是使用装饰器声明特性，而不是使用 property() 函数。这种方式更简单
，也更常用。当定义拥有 getter 的特性时，首选这种方式。

如果定义了一个 getter，则不必显式地创建并分配 property()。相反，装饰器@property
可以应用于 getter：

```python
    @property
    def secret(self):
        return self._secrets[-1] if self._secrets else None

    @secret.setter
    def secret(self, value):
        self._secrets.append(self._encrypt(value))

    @secret.deleter
    def secret(self):
        self._secrets = []
```

以上代码使用装饰器 @property 而非@secret.getter 来定义 getter，这样将创建一个与
方法具有相同名称的特性。由于定义了特性 secret，因此不需要在代码中使用 secret =
property()。

请记住，这种快捷方式仅适用于 getter。setter 和 deleter 必须使用与以前相同的方式
来定义。

### 7.5.4 什么时候不使用特性？

## 7.6 特殊方法

特殊方法有时候也被称为魔法方法，它们允许我们为自己的类添加对几乎任何 Python 运算
符或内置命令的支持！

特殊方法以两个下画线（\*\*）开头和结尾。你已经见到了 3 个特殊方法
：`__nit__()`、`__new__()`和`__del__()`。Python 定义了大约 100 个特殊方法，其中
大多数在 Python 官方文档的“数据模型”部分有介绍。

### 7.6.1 场景设置

本节使用一个新的类 GlobalCoordinates，该类以纬度和经度的方式存储一个全局坐标。如
下所示：

```python
class GlobalCoordinates:

    def __init__(self, *, latitude, longitude):

        self._lat_deg = latitude[0]
        self._lat_min = latitude[1]
        self._lat_sec = latitude[2]
        self._lat_dir = latitude[3]

        self._lon_deg = longitude[0]
        self._lon_min = longitude[1]
        self._lon_sec = longitude[2]
        self._lon_dir = longitude[3]

    @staticmethod
    def degree_from_decimal(dec, *, lat):
        if lat:
            direction = "S" if dec < 0 else "N"
        else:
            direction = "W" if dec < 0 else "E"
        dec = abs(dec)
        degrees = int(dec)
        dec -= degrees
        minutes = int(dec * 60)
        dec -= minutes / 60
        seconds = round(dec * 3600, 1)
        return (degrees, minutes, seconds, direction)

    @staticmethod
    def decimal_from_degrees(degrees, minutes, seconds, direction):
        dec = degrees + minutes/60 + seconds / 3600
        if direction == 'S' or direction == 'W':
            dec = -dec
        return round(dec, 6)

    @property
    def latitude(self):
        return self.decimal_from_degrees(self._lat_deg, self._lat_min, self._lat_sec, self._lat_dir)

    @property
    def longitude(self):
        return self.decimal_from_degrees(self._lon_deg, self._lon_min, self._lon_sec, self._lon_dir)
```

GlobalCoordinates 类将纬度和经度转换并存储为由度、分、秒，以及表示基本方向的字符
串构成的元组。

### 7.6.2 转换方法

我们应该仔细考虑自己的类应该支持转换为哪些数据类型。下面介绍一些用于数据转换的特
殊方法。

1. 规范字符串表示： `__repr__()`

在编写一个类时，最好定义 `__repr__()` 实例方法，它返回对象的常规字符串表示。这个
字符串表示应该包含创建具有相同内容的另一个类实例所需的所有数据。

如果没有为 GlobalCoordinates 定义 `__repr__()` 实例方法，Python 将回退到其默认的
表示，这几乎没有任何实际用途。创建一个 GlobalCoordinates 实例，并通过 repr() 输
出这个默认的表示，如下所示：

```python
from global_coordinates import GlobalCoordinates

nsp = GlobalCoordinates(latitude=(37, 46, 32.6, 'N'), longitude=(122, 24, 39.4, 'W'))

print(repr(nsp))    # <global_coordinates.GlobalCoordinates object at 0x0000021A54DF6900>
```

下面我们来自定义 `__repr__()` 实例方法，如下所示：

```python
    def __repr__(self):
        return (
            f"<GlobalCoordinates lat={self._lat_deg}° {self._lat_min}′ {self._lat_sec}″ \\ {self._lat_dir} lon={self._lon_deg}° {self._lon_min}′ {self._lon_sec}″ \\ {self._lon_dir}"
        )
```

运行以上代码将返回一个字符串，其中包含创建实例所需的所有信息，如下所示：

```bash
<GlobalCoordinates lat=37° 46′ 32.6″ \ N lon=122° 24′ 39.4″ \ W>
```

2. 易读字符串表示：`__str__()`

`__str__()`与`__repr__()`具有类似的作用，但前者用于生成更可读的文本，而不是更专
业的规范表示；后者对于调试更有用。

如果没有定义`__str__()`，那么`__repr__()`将被调用，但在这个例子中这是不可取的。
用户只应该看到美观的坐标！

如下所示：

```python
    def __str__(self):
        return (
            f"lat={self._lat_deg}° {self._lat_min}′ {self._lat_sec}″ \\ {self._lat_dir} lon={self._lon_deg}° {self._lon_min}′ {self._lon_sec}″ \\ {self._lon_dir}"
        )
```

不同于 `__repr__()`，这里省略了所有无聊的技术信息，并专注于组合和返回用户可能想
要看到的字符串表示。

`__str__()` 在将类的实例传递给 str() 时会被调用，尽管将实例直接传递给 print() 或
作为格式化字符串中的表达式也会调用 `__str__()`，如下所示：

```python
print(f"No Starch Press's offices are at {nsp}")
```

输出结果如下所示：

```bash
lat=37° 46′ 32.6″ \ N lon=122° 24′ 39.4″ \ W
```

3. 唯一标识符（哈希）：`__hash__()`

