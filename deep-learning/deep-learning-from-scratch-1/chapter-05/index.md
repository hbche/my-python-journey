# 第 5 章 误差反向传播法

前面学习了通过数值微分计算参数的梯度的方式来训练神经网络的权重参数。数值微分虽然实现简单且容易实现，但是计算非常耗时。本章我们将学习通过反向传播法来实现高效的权重计算方法。

## 5.1 计算图

计算图将计算过程以图形表示出来。这里说的图形是指数据结构，通过多个节点和边表示。

### 5.1.1 用计算图求解

### 5.1.2 局部计算

计算图的特征是可以通过传递“局部计算”获得最终结果。

计算图可以集中精力与局部计算，无论全局的计算有多么复杂，各个步骤索要做的就是对象节点的局部计算。虽然局部计算非常简单，但是通过传递它的计算结果，可以获得全局的复杂计算的结果。

### 5.1.3 为何选择计算图解题

优点：

1. 将复杂的全局计算拆分成简单的局部计算，可以通过局部计算使各个节点致力于简单的计算，从而简化问题。
2. 利用计算图可以将中间的计算结果全部保存起来。
3. 使用计算图可以通过反向传播高效计算导数。

我们可以借助计算图正向转播或反向传播高效计算各个标量的导数。

## 5.2 链式法则

### 5.2.1 计算图的反向传播

### 5.2.2 什么是链式法则

在介绍链式法则之前，我们先讲解复合函数。复合函数是由多个函数组成的函数。下面是一个复合函数的实例：

$$
z = t^2 \\
t = x + y
$$

## 5.3 反向传播

### 5.3.1 加法运算的反向传播

首先来考虑加法节点的反向传播。这里以 $z=x+y$为对象，观察它的反向传播。$z=x+y$的导数可由下式（解析性地）计算出来。

$$
\frac{\partial{z}}{\partial{x}}=1\\
\frac{\partial{z}}{\partial{y}}=1\\
$$

反向传播将上流传递过来的导数乘以1，然后传向下游。也就是说，因为加法节点的反向传播只乘以1，所以输入的值会原封不动地流向下一个节点。

### 5.3.2 乘法节点的反向传播

接下来，我们看一下乘法节点的反向传播。这里我们以 $z=xy$ 为例进行分析。这个式子的导数计算如下所示：

$$
\frac{\partial{z}}{\partial{x}}=y\\
\frac{\partial{z}}{\partial{y}}=x\\
$$

乘法的反向传播会将上游的值乘以正向传播时的输入信号的“翻转值”后传递给下游。翻转值表示一种翻转关系，正向传播时信号时x的话，反向传播时则是y；正向传播时信号是y的话，反向传播时则是x。

因为乘法的反向传播会乘以输入信号的翻转值，所以需要保存乘法计算的操作数。另外，加法的法相传播知识将上游的值传递给下游，并不需要正向传播的输入信号。但是，乘法的反向传播需要正向传播的输入信号值。因此，实现乘法节点的反向传播时，要保存正向传播的输入信号。

### 5.3.3 苹果的例子

## 5.4 简单层的实现

### 5.4.1 乘法层的实现

```py
class MulLayer:
    """
    乘法层
    """

    def __init__(self):
        """
        因为是在forward 阶段才传入输入参数，所以构造函数中不进行暂存逻辑
        """
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x * y

    def backward(self, dout):
        dx = self.y * dout
        dy = self.x * dout
        return dx, dy
```

下面我们来以买苹果为例检验上面的乘法层实现是否正确：

```py
from layer_naive import MulLayer


def buy_apple():
    # 苹果个数
    apple_total = 2
    # 苹果单价
    apple_price = 100
    # 税率
    tax = 1.1

    # 苹果计算的乘法层
    apple_mul_layer = MulLayer()
    # 总价计算的乘法层
    tax_mul_layer = MulLayer()

    # 利用乘法层计算总价
    total_price = tax_mul_layer.forward(
        apple_mul_layer.forward(apple_price, apple_total), tax
    )
    print(f"Total price is {total_price}")
    # Total price is 220.00000000000003
    # 根据乘法层的反向传播计算各个参数的导数
    delta_out = 1
    # 计算苹果总价和税率的导数
    delta_apple_total_priace, delta_tax = tax_mul_layer.backward(delta_out)
    print(f"Delta tax is {delta_tax}")
    # Delta tax is 200
    # 根据苹果总价的导数再结合乘法层的反向传播计算苹果单价和苹果个数的导数
    delta_apple_price, delta_apple_total = apple_mul_layer.backward(
        delta_apple_total_priace
    )
    print(
        f"Delta apple price is {delta_apple_price}, delta apple total is {delta_apple_total}"
    )
    # Delta apple price is 2.2, delta apple total is 110.00000000000001


if __name__ == "__main__":
    buy_apple()

```

### 5.4.2 加法层的实现

```py
from layer_naive import AddLayer, MulLayer

# 以买苹果和买橘子的案例测试加法层和乘法层的实现


def buy_apple_orange():
    apple_price = 100
    apple_count = 2
    orange_price = 150
    orange_count = 3
    tax = 1.1

    apple_mul_layer = MulLayer()
    orange_mul_layer = MulLayer()
    add_layer = AddLayer()
    tax_mul_layer = MulLayer()

    # 计算苹果总价
    apple_total_price = apple_mul_layer.forward(apple_price, apple_count)
    # 橘子苹果总价
    orange_total_price = orange_mul_layer.forward(orange_price, orange_count)
    # 计算苹果和橘子的总价
    total_price = add_layer.forward(apple_total_price, orange_total_price)
    # 计算税后的总价
    tax_total_price = tax_mul_layer.forward(total_price, tax)
    print(
        f"苹果单价为{apple_price}， 橘子单价为{orange_price}，税率是10%， 现在购买{apple_count}个苹果和{orange_count}个橘子，税后总价为：{tax_total_price}"
    )
    # 苹果单价为100， 橘子单价为150，税率是10%， 现在购买2个苹果和3个橘子，税后总价为：715.0000000000001

    # 反向传播计算导数
    # 计算税率的导数
    dout = 1
    dout_price, dout_tax = tax_mul_layer.backward(dout)
    print(f"汇率的导数为 {dout_tax}")
    # 汇率的导数为 650
    print(f"水果税前总价的导数为 {dout_price}")
    # 水果税前总价的导数为 1.1
    dout_apple_total_price, dout_orange_total_price = add_layer.backward(dout_price)
    dout_apple_price, dout_apple_count = apple_mul_layer.backward(
        dout_apple_total_price
    )
    print(f"苹果单价的导数为 {dout_apple_price}，苹果个数的导数为 {dout_apple_count}")
    # 苹果单价的导数为 2.2，苹果个数的导数为 110.00000000000001
    dout_orange_price, dout_orange_count = orange_mul_layer.backward(
        dout_orange_total_price
    )
    print(f"橘子单价的导数为 {dout_orange_price}，橘子个数的导数为 {dout_orange_count}")
    # 橘子单价的导数为 3.3000000000000003，橘子个数的导数为 165.0


if __name__ == "__main__":
    buy_apple_orange()
```

## 5.5 激活函数层的实现

### 5.5.1 ReLU层

数学表达式如下：

$$
y=\left\{
\begin{aligned}
0 \qquad(x \leq 0)\\
x \qquad (x > 0)
\end{aligned}
\right.
$$

代码实现如下：

```py
class ReLULayer:
    """
    ReLU 层激活函数
    """

    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = x <= 0
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
```
