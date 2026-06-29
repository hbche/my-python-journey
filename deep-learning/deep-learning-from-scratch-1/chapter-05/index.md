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

### 5.5.2 Sigmoid 层

sigmoid 函数表达式：

$$
y = \frac{1}{1+e^{-x}}
$$

我们先基于链式法则，完成 sigmoid 梯度计算的解析解：

$$
\frac{\partial{y}}{\partial{x}}=-\frac{1}{(1+e^{-x})^{2}}(-e^{-x})=\frac{1}{1+e^{-x}}\frac{e^{-x}}{1+e^{-x}}
$$

从而计算得到：

$$
\frac{\partial{y}}{\partial{x}}=\frac{1}{1+e^{-x}}\frac{(1+e^{-x})-1}{1+e^{-x}}=y(1-y)
$$

代码实现如下：

```py
class Sigmoid:
    """
    sigmoid 激活层
    """

    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * self.out * (1.0 - self.out)

        return dx
```

在这个实现中，正向传播时将输出保存在实例变量 out 中。然后，反向传播时，使用该变量 out 进行计算。

## 5.6 Affine/Softmax 层的实现

### 5.6.1 Affine 层

在神经网络的正向传播中，为了计算加权信号的总和，使用了矩阵的乘积运算。

权重计算表达式：

$$
L=X\cdot{W}+B
$$

我们假设 $X 的 shape 为 $(2,)$，$W$ 的 shape 为 $(2, 3)$，B 的 shape 为 $(3, )$，我们来推导 $\frac{\partial{L}}{\partial{X}}$ 和 $\frac{\partial{L}}{\partial{W}}$，其中 $X$ 的 shape 和其导数的维度需要保持一致，$W$ 的 shape 也需要和其导数的维度保持一致：

$$
\frac{\partial{L}}{\partial{X}}=\frac{\partial{L}}{\partial{Y}}W^T\\
\frac{\partial{L}}{\partial{W}}=X^T\frac{\partial{L}}{\partial{Y}}
$$

### 5.6.2 批量版本的 Affine 层

假设输入数据有 N 个。则 $X$ 的维度为 $(N, 2)$，$W$的维度为$(2, 3)$，$Y$的维度为$(N, 3)$。

加上偏置时，需要特别注意。正向传播时，偏置被加到 $X\cdot{W}$ 的各个数据上。比如，N=2，偏置会被分别加到这两个数据上，具体例子如下：

```py
X_dot_W = np.array([[0, 0, 0,], [10, 10, 10]])
B = np.array([1, 2, 3])
X_dot_W + B
# array([[ 1,  2,  3],
#        [11, 12, 13]])
```

正向传播时，偏置会被加到每一个数据（第1个、第2个……）上。因此，反向传播时，各个数据的反向传播的值需要汇总为偏置的元素。用代码表示的话，如下所示：

```py
>>> dY = np.array([[1, 2, 3], [4, 5, 6]])
>>> db = np.sum(dY, axis=0)
>>> db
array([5, 7, 9])
```

这个例子中，假定数据有2个。偏置的反向传播会对这2个数据的导数按元素进行求和。因此，这里

代码实现如下：

```py
class Affine:
    """
    Affine 仿射层，计算权重参数的总和
    """

    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.w) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx
```

### 5.6.3 Softmax-with-Loss 层

神经网络中进行的处理有推理和学习两个阶段。神经网络的推理通常不使用Softmax层。例如手写数字识别，在进行推理时会将最后一个 Affine 层的输出作为识别结果。神经网络中未被正则化的输出结果有时被称为“得分”。也就是说，当神经网络的推理只需要给出一个答案的情况下，因为此时只对得分最大值感兴趣，所以不需要Softmax层。不过，神经网络的学习阶段则需要Softmax层。

我们接下来以交叉熵误差作为损失函数，封装 Softmax-with-Loss 层（Softmax函数+交叉熵误差）。

我们先进行拆解，Softmax层和CrossEntropyError层。

Softmax 函数表达式如下：

$$
E=-\sum_{k}{t_k}\log({y_k})
$$

TODO：详细推理过程需要补充

整体代码实现如下：

```py

class SoftmaxWithLoss:
    """
    基于交叉熵误差作为损失函数的Softmax层
    """

    def __init__(self):
        # 经过 Softmax 计算之后的结果
        self.y = None
        self.t = None
        self.loss = None

    def forward(self, x, t):
        self.y = softmax(x)
        self.t = t
        self.loss = cross_entropy_error(x, t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx
```

## 5.7 误差反向传播法的实现

### 5.7.1 神经网络学习的全貌图

##### 前提

神经网络中有合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程称为学习。神经网络的学习分为下面4个步骤。

##### 步骤1（mini-batch）

从训练数据中随机选择一部分数据

##### 步骤2（计算梯度）

计算损失函数关于各个权重参数的梯度。

##### 步骤3（更新参数）

将权重参数沿梯度方向进行微小的更新。

##### 步骤4（重复）

重复步骤1、步骤2、步骤3。


### 5.7.2 对应误差反向传播法的神经网络的实现

以两层神经网络为例进行实现:

``` py

```

### 5.7.3 误差反向传播法的梯度确认


