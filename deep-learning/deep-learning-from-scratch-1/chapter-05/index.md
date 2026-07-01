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

> Softmax 中涉及 $ln(x)$ 计算，自然对数函数 $y=ln(x)$的定义域为 $(0, +\infty)$，所以在保证下溢出的同时还要保证输入的 x 必须是大于 0 的

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

首先我们来实现两层神经网络的封装

```py
# 两层神经网络实现
from collections import OrderedDict

import numpy as np
from layer_naive import Affine, ReLU, SoftmaxWithLoss, numerical_gradient


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重参数
        w1 = np.random.randn(input_size, hidden_size) * weight_init_std
        b1 = np.zeros(hidden_size)
        w2 = np.random.randn(hidden_size, output_size) * weight_init_std
        b2 = np.zeros(output_size)
        self.params = {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["w1"], self.params["b1"])
        self.layers["Relu1"] = ReLU()
        self.layers["Affine2"] = Affine(self.params["w2"], self.params["b2"])

        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)
        accuracy = np.sum(y == t) / float(t.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_w = lambda W: self.loss(x, t)

        grads = {}
        grads["w1"] = numerical_gradient(loss_w, self.params["w1"])
        grads["b1"] = numerical_gradient(loss_w, self.params["b1"])
        grads["w2"] = numerical_gradient(loss_w, self.params["w2"])
        grads["b2"] = numerical_gradient(loss_w, self.params["b2"])

        return grads


    def gradient(self, x, t):
        self.loss(x, t)

        dout = 1
        dout = self.last_layer.backward(dout)

        # reverse 函数是一个就地修改原始数据的函数，其返回值为None
        # 此处需要使用 reversed 函数，在不修改原始输入参数的前提下返回倒序之后的新列表
        for layer in reversed(list(self.layers.values())):
            dout = layer.backward(dout)

        grads = {}
        grads["w1"] = self.layers["Affine1"].dw
        grads["b1"] = self.layers["Affine1"].db
        grads["w2"] = self.layers["Affine2"].dw
        grads["b2"] = self.layers["Affine2"].db

        return grads
```

接下来我们来设计层的实现，其中涉及到加法层、乘法层、Affine层、Sigmoid激活函数层、ReLU激活函数层、Softmax激活函数层，以及分类任务中用语计算损失函数的交叉熵误差函数，还有基于数值微分的梯度计算：

```py
# coding: utf-8
import numpy as np


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


class AddLayer:
    """
    加法层
    """

    def __init__(self):
        pass

    def forward(self, x, y):
        return x + y

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy


class ReLU:
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


class Affine:
    """
    Affine 仿射层，计算权重参数的总和
    """

    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None
        self.original_x_shape = None
        self.dw = None
        self.db = None

    def forward(self, x):
        self.original_x_shape = x.shape
        x = x.reshape(x.shape[0], -1)
        self.x = x

        out = np.dot(self.x, self.w) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        dx = dx.reshape(*self.original_x_shape)

        return dx


def softmax(x):
    """
    softmax函数
    """
    x = x - np.max(x, axis=-1, keepdims=True)

    return np.exp(x) / np.sum(np.exp(x), axis=-1, keepdims=True)


def cross_entropy_error(y: np.array, t):
    """
    交叉熵误差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size = y.shape[0]
    delta = 1e-7

    return -np.sum(t * np.log(y + delta)) / batch_size


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
        # 需要主机，计算交叉熵误差时传入的参数是经过 Softmax 计算之后的数据，不是原始数据
        self.loss = cross_entropy_error(self.y, t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        if self.y.size == self.t.size:
            dx = (self.y - self.t) / batch_size
        else:
            dx = self.y.copy()
            dx[np.range(batch_size), self.t] -= 1
            dx = dx / batch_size

        return dx


def _numerical_gradient_1d(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 値を元に戻す

    return grad


def numerical_gradient_2d(f, X):
    if X.ndim == 1:
        return _numerical_gradient_1d(f, X)
    else:
        grad = np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_1d(f, x)

        return grad


def numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)

    it = np.nditer(x, flags=["multi_index"], op_flags=["readwrite"])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)  # f(x+h)

        x[idx] = tmp_val - h
        fxh2 = f(x)  # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2 * h)

        x[idx] = tmp_val  # 値を元に戻す
        it.iternext()

    return grad
```

其中有几点需要注意的地方：

1. 在 `gradient` 方法内部基于反向传播法计算，所以需要对层进行翻转，从右往左开始计算，与正向传播相反的方向计算梯度。其中翻转函数需要注意 `list.reverse()` 方法和 `reversed(list)` 的区别
2. 在设计 `SoftmaxWithLoss` 时，需要充分理解，该逻辑是神经网络中正向传播的最后一层，需要先进行 Softmax 激活函数处理，需要将前面的 Affine 计算结果转换成概率数值，在基于该概率数值计算损失值。而不是直接将前面 Affine 层的计算结果进行交叉熵误差计算。
3. 需要明确理解交叉熵误差计算的含义，以及交叉熵误差函数中 $ln(x)$ 函数的定义域为 $(0, +\infty)$，小于 0 的输入会导致交叉熵误差计算出来的数据为 `nan`。
4. 之前学习的数值微分计算权重参数梯度的实现只考虑了一维数组，没有考虑矩阵场景，需要重写
5. 之前写的 `softmax` 函数只能覆盖一维数据，此处需要修改，需要扩展到多维

### 5.7.3 误差反向传播法的梯度确认

我们现在来通过 MNIST 数据集，测算数值微分计算和导数解析解计算梯度的误差。

```py
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

x_batch = x_train[:3]
t_batch = t_train[:3]

grad_gradient = network.gradient(x_batch, t_batch)
grad_numerical = network.numerical_gradient(x_batch, t_batch)

for key in grad_gradient.keys():
    diff = np.average(np.abs(grad_gradient[key] - grad_numerical[key]))
    print(f"{key}: {str(diff)}")

# w1: 9.878706695770596e-05
# b1: 0.0007424660241043507
# w2: 0.0026460023296286995
# b2: 0.06666666678701484
```

从结果来看，通过数值微分和误差反向传播求出的梯度的差非常小。

> 数值微分和误差反向传播法的计算结果之间的误差为0是很少见的。这是因为计算机的计算精度有限（比如，32位浮点数）​。受到数值精度的限制，刚才的误差一般不会为0，但是如果实现正确的话，可以期待这个误差是一个接近0的很小的值。如果这个值很大，就说明误差反向传播法的实现存在错误。

### 5.7.4 使用误差反向传播法的学习

与之前基于数值微分计算梯度的学习过程相似，唯一的区别是求梯度方法改为了基于反向传播法计算的梯度

```py
import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(784, 50, 10)

batch_size = 100
train_size = x_train.shape[0]
learning_rate = 0.1
train_loop = 10000

train_loss_list = []
train_acc_list = []
test_acc_list = []

item_per_epoch = max(train_size / batch_size, 1)

for i in range(train_loop):
    batch_mask = np.random.choice(train_size, batch_size)
    x_train_batch = x_train[batch_mask]
    t_train_batch = t_train[batch_mask]
    # 通过反向传播求梯度
    grads = network.gradient(x_train_batch, t_train_batch)

    # 更新权重参数
    for key in ("w1", "b1", "w2", "b2"):
        network.params[key] -= grads[key] * learning_rate

    loss = network.loss(x_train_batch, t_train_batch)
    train_loss_list.append(loss)

    # 以 epoch 为单位，计算当前权重的准确率
    if i % item_per_epoch == 0:
        train_acc = network.accuracy(x_train_batch, t_train_batch)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)

# 0.13 0.1097
# 0.91 0.9016
# 0.93 0.9251
# 0.97 0.9341
# 0.95 0.9437
# 0.95 0.9494
# 0.98 0.952
# 0.97 0.9568
# 0.98 0.9596
# 1.0 0.9626
# 0.99 0.9629
# 0.99 0.9648
# 0.99 0.9661
# 1.0 0.9667
# 0.99 0.9678
# 1.0 0.9692
# 1.0 0.9702
```

## 5.8 小结

- 通过使用计算图，理解反向传播算法
- 理解计算图的局部计算过程
- 理解计算图的正向传播，学习通过反向传播，计算各个节点的导数
- 基于反向传播算法，将每层计算进行封装，高效计算梯度
- 比较数值微分和误差反向传播法的结果，确认误差反向传播法的实现是否正确

## 5.9 课后思考

<details>
  <summary>1. 为什么反向传播法中实现的两层神经网络代码中 `predict` 方法最后的输出层没有调用`softmax`激活函数，而是直接将 `Affine` 层的计算结果作为输出进行 `accuracy` 计算？</summary>
  这是一个很好的观察！在`predict`方法中确实**没有**调用softmax激活函数，而是直接返回了Affine层的输出（即逻辑回归中的"logits"）。这是有意为之的，原因如下：

## 主要原因

### 1. **Softmax是单调递增函数，不影响分类结果**

```python
# 假设Affine2输出为 [2.0, 1.0, 0.5]
# 直接比较：argmax = 0 (最大值是2.0)
# Softmax后：[0.665, 0.245, 0.090]，argmax仍然是0
```

Softmax只改变数值范围（变成概率），但不改变相对大小顺序，因此**不影响最终的分类决策**。

### 2. **计算效率**

在推理（预测）时，我们只需要知道哪个类别的得分最高，不需要计算概率分布。跳过softmax可以节省计算资源。

### 3. **与训练阶段保持一致**

- 训练时：`SoftmaxWithLoss`层在内部计算softmax，然后计算交叉熵损失
- 预测时：直接使用logits进行比较，结果等价

## 如果要输出概率怎么办？

如果你确实需要概率值（比如用于置信度评估），可以这样修改：

```python
def predict_proba(self, x):
    for layer in self.layers.values():
        x = layer.forward(x)
    # 应用softmax得到概率
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # 数值稳定性
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)
```

## 代码中的验证

在`accuracy`方法中：

```python
y = self.predict(x)        # 得到logits
y = np.argmax(y, axis=1)   # 直接取最大值的索引作为预测类别
```

这等价于：

```python
y = self.predict(x)
y = np.argmax(softmax(y), axis=1)  # 结果完全相同
```

**总结**：这是一种常见的设计模式，在推理阶段跳过softmax以提升效率，因为分类结果不受影响。

</details>

<details>
    <summary>2. 学习阶段需要softmax是因为需要计算交叉熵误差吗？能否直接将Affine层的输出进行交叉熵误差计算？</summary>
    **完全正确！** 你的理解非常准确。如果Affine层直接输出负值，直接计算交叉熵确实会报错。

## 问题演示

```python
import numpy as np

# Affine层输出（logits）
logits = np.array([2.0, -1.0, 0.5])  # 包含负值！

# 错误示例：直接计算交叉熵
def bad_cross_entropy(logits, t):
    # 直接取log - 会报错！
    return -np.sum(t * np.log(logits))
    # ValueError: math domain error (log of negative number)

# 运行会报错
# t = np.array([0, 1, 0])  # one-hot标签
# bad_cross_entropy(logits, t)  # ❌ 报错！
```

## 解决方案

### 方案1：通过Softmax转换为概率（标准做法）

```python
def softmax(x):
    exp_x = np.exp(x - np.max(x))  # 数值稳定性处理
    return exp_x / np.sum(exp_x)

logits = np.array([2.0, -1.0, 0.5])
probs = softmax(logits)  # [0.636, 0.032, 0.332] 全部为正且和为1

# 现在可以安全计算交叉熵
def cross_entropy(probs, t):
    return -np.sum(t * np.log(probs))

t = np.array([0, 1, 0])  # 真实标签是第1类
loss = cross_entropy(probs, t)  # ✅ 正常工作
print(f"Loss: {loss}")  # 输出: 3.44
```

### 方案2：使用LogSumExp技巧（数值稳定，无需显式Softmax）

这就是为什么 `SoftmaxWithLoss` 层内部使用这个技巧：

```python
def cross_entropy_with_logits_stable(logits, t):
    """
    直接使用logits计算交叉熵，数值稳定
    数学上等价于: -log(softmax(logits)[correct_class])
    """
    # 找到正确类别的索引
    class_idx = np.argmax(t)

    # 数值稳定的log-sum-exp
    max_logit = np.max(logits)
    exp_sum = np.sum(np.exp(logits - max_logit))

    # 稳定计算：-log(softmax(logits)[class_idx])
    loss = -logits[class_idx] + max_logit + np.log(exp_sum)
    return loss

# 测试
logits = np.array([2.0, -1.0, 0.5])
t = np.array([0, 1, 0])
loss = cross_entropy_with_logits_stable(logits, t)
print(f"Stable loss: {loss}")  # 输出: 3.44 (与上面结果相同)
```

## 你代码中的实际处理

在你的 `TwoLayerNet` 中：

```python
class TwoLayerNet:
    def __init__(self, ...):
        # ...
        self.lastLayer = SoftmaxWithLoss()  # ← 关键！

    def loss(self, x, t):
        y = self.predict(x)  # y是logits（可能含负值）
        return self.lastLayer.forward(y, t)  # ← 内部处理！
```

`SoftmaxWithLoss.forward()` 内部会：

```python
class SoftmaxWithLoss:
    def forward(self, x, t):
        # 1. 先计算softmax（将logits转为概率，全部变为正数）
        self.y = softmax(x)  # 现在所有值在(0,1)之间

        # 2. 再计算交叉熵（现在安全了）
        self.loss = cross_entropy_error(self.y, t)
        return self.loss
```

## 总结

| 输入         | 直接计算交叉熵  | 通过Softmax | 使用LogSumExp |
| ------------ | --------------- | ----------- | ------------- |
| Logits含负值 | ❌ 报错         | ✅ 安全     | ✅ 安全       |
| Logits含正值 | ✅ 可能但无意义 | ✅ 标准做法 | ✅ 标准做法   |
| 概率值(0-1)  | ✅ 可以         | ❌ 不需要   | ❌ 不需要     |

**关键点**：

1. 对数函数 `ln(x)` 定义域确实是 `(0, +∞)`
2. Affine层输出可以包含负值，所以**不能**直接计算交叉熵
3. 必须通过Softmax将logits转换为概率（正值）后再计算
4. `SoftmaxWithLoss` 层封装了这个过程，确保数值稳定性

这就是为什么你的代码中 `predict` 不包含Softmax（为了效率），但 `loss` 中通过 `SoftmaxWithLoss` 处理（为了正确性）！🎯

</details>
