# 第 6 章 与学习相关的技巧

目标：

1. 理解神经网络的学习过程
2. 理解并掌握SGD（stochastic ）等常用学习算法
3. 掌握参数初始化的方法
4. 理解并掌握正则化常用手法

## 6.1 参数的更新

### 6.1.1 探险家的故事

一个走夜路的探险家如何根据坡度判断一步一步深入谷底。

### 6.1.2 SGD

数学公式：

$$
W = W - learning\_rate * \frac{\partial{L}}{\partial{W}}
$$

代码实现：

```py
class SGD:
    """
    随机梯度下降法计算权重
    """

    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate

    def update(self, params, grads):
        for key in grads.keys():
            params[key] -= self.learning_rate * grads[key]
```

使用方法：

```py
import numpy as np
from dataset.mnist import load_mnist
from optimizer import SGD
from two_layer_net import TwoLayerNetwork

if __name__ == "__main__":
    # # 测试softmax
    # x = np.array([[1, 2, 3], [1, 1, 1]])
    # x = softmax_standard(x)
    # print(x)
    # print(np.sum(x, axis=1, keepdims=True))

    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, one_hot_label=True
    )

    network = TwoLayerNetwork(28 * 28, 100, 10)
    optimizer = SGD()

    # 批处理大小
    batch_size = 100
    # 训练数据总数，用于生成随机索引
    train_size = t_train.shape[0]
    # 训练迭代次数
    train_loop = 10000
    # 每轮训练过程中，根据梯度更新参数的学习率
    learn_rate = 0.01

    # 重点注意：iter_per_epoch的含义，计算误差的轮次
    iter_per_epoch = max(train_size / batch_size, 1)

    # 重点注意：需要记录什么不清楚
    # 记录每次迭代过程中的误差结果
    train_loss_list = []
    # 保存每轮计算的准确率
    train_acc_list = []
    test_acc_list = []

    for i in range(train_loop):
        train_mask = np.random.choice(train_size, batch_size)
        x_train_batch, t_train_batch = x_train[train_mask], t_train[train_mask]

        # 通过误差反向传播法计算梯度
        grads = network.gradient(x_train_batch, t_train_batch)
        # # 根据梯度和学习率更新权重参数
        # for key in grads.keys():
        #     network.params[key] -= learn_rate * grads[key]
        optimizer.update(network.params, grads)

        # 使用新参数计算损失值
        loss = network.loss(x_train_batch, t_train_batch)
        # 保存每轮训练过程中的损失值
        train_loss_list.append(loss)

        if i % iter_per_epoch == 0:
            print(f"Loss: {loss}.")
            # 重点注意： 此处不是使用 batch 训练数据计算准确率，而是使用全量的训练数据
            train_acc = network.accuracy(x_train, t_train)
            train_acc_list.append(train_acc)
            test_acc = network.accuracy(x_test, t_test)
            test_acc_list.append(test_acc)
            print(f"Train Accuracy: {train_acc}, Test Accuracy: {test_acc}")
```

### 6.1.3 SGD 的缺点

虽然 SGD 简单，并且容易实现，但是在解决某些问题时可能没有效率。我们可以使用SGD计算下面这个函数的最小值：

$$
f(x, y) = \frac{1}{20}x^2 + y^2
$$

我们来使用 matplotlib 绘制这个函数的图像：

```py
# SGD 训练法缺陷

import matplotlib.pyplot as plt
import numpy as np

# 创建网格
x = np.arange(-10, 10.0, 0.1)
y = np.arange(-10, 10.0, 0.1)

X, Y = np.meshgrid(x, y)
print(X.shape)  # (100, 200)
print(Y.shape)  # (100, 200)
Z = X**2 / 20 + Y**2

# 创建三维坐标系
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# # 绘制曲面
# ax.plot_surface(X, Y, Z)
# 绘制网格（不填充颜色）
ax.plot_wireframe(
    X,
    Y,
    Z,
    color="black",  # 网格颜色
    linewidth=0.6,  # 网格线宽
    rstride=5,  # 行方向每隔5个点绘制一条线
    cstride=5,  # 列方向每隔5个点绘制一条线
)

# 设置坐标轴标签
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.set_title(r"$f(x, y)=\frac{1}{20}x^2+y^2$")
# 设置坐标轴刻度
ax.set_xticks(np.arange(-10, 10, 5))
ax.set_yticks(np.arange(-10, 10, 5))

plt.show()
```

接下来我们在绘制等高线示意图：

```py
# 使用等高线研究SGD的缺陷
import matplotlib.pyplot as plt
import numpy as np

# 创建网格数据
x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = X**2 / 20 + Y**2

plt.figure(figsize=(7, 6))
# 绘制等高线
contour = plt.contour(X, Y, Z, levels=20, cmap="viridis")

# 添加数值标签
plt.clabel(contour, inline=True, fontsize=8)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x, y)=\frac{1}{20}x^2+y^2$")

plt.axis("equal")

plt.show()
```

为了能明显看出 SGD 的训练缺陷，我们现在在等高线图中绘制训练过程中的移动路径：

```py
import matplotlib.pyplot as plt
import numpy as np

# 使用等高线绘制函数 $f(x,y)=\frac{1}{20}x^2+y^2$的梯度


class SGD:
    def __init__(self, learning_rate=0.1):
        self.learning_rate = learning_rate

    def update(self, params, grads):
        for key in params:
            params[key] -= self.learning_rate * grads[key]


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0 * y


def move_points():
    init_pos = (-7.0, 2.0)
    params = {}
    params["x"], params["y"] = init_pos[0], init_pos[1]
    grads = {}
    grads["x"], grads["y"] = 0, 0

    x_history = []
    y_history = []
    optimizer = SGD(0.95)

    for i in range(20):
        x_history.append(params["x"])
        y_history.append(params["y"])

        grads["x"], grads["y"] = df(params["x"], params["y"])
        optimizer.update(params, grads)

    return x_history, y_history


# 绘制等高线
def plot_contour():
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # for simple contour line
    mask = Z > 7
    Z[mask] = 0

    # plot
    # plt.subplot(2, 2, 1)
    plt.figure(figsize=(8, 6))
    x_history, y_history = move_points()
    plt.plot(x_history, y_history, "o-", color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, "+")
    # colorbar()
    # spring()
    plt.title("SGD")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    plot_contour()
```

我们发现随着梯度更新，更新路径呈现"之"字型移动，这是一个相当低效的路径。

![](./assets/SGD_grads_1.png)

也就是说，SGD的缺点是，如果函数的形状非匀向，比如呈延伸状，搜索的路径就非常低效。

SGD低效的根本原因是，梯度的方向并没有指向最小值的方向。

有两个问题：

1. 容易震荡
2. 前进一步马上忘记上一步走的方向，严格依赖当前梯度

### 6.1.4 Momentum

SGD是因为不区分梯度大小，将参数固定更新 `learning_rate` 倍的梯度，就会导致沿y轴梯更新幅度更大，从而出现“之”字型回荡。

我们能够基于梯度进行改进，依赖梯度的大小来计算更新幅度。这就是我们接下来要学习的改进方案 - Momentum。

momentum 的物理公式为：

$$
p=mv
$$

一个球滚起来以后，即使坡度变小，它仍然会继续向前滚。

机器学习中借鉴了这个思维，**不要值相信当前梯度，而要保留之前运动的惯性**。

于是引入了一个新的变量 `v` —— 它表示参数的更新速度。

Momentum 的标准公式：

$$
v_t​=βv_{t-1}​−ηg_t​
$$

其中：

- $g_t$：表示梯度
- η：学习率
- β：Momentum 系数

我们转换成如下方式：

$$
v = αv - η\frac{\partial{L}}{\partial{W}}
$$

其中

- α：Momentum 系数
- η：学习率

接下来我们以一个权重参数来逐步分析，加深对 Momentum 原理的理解：

```md
初始化：
v=0
w=10
learning_rate=0.1
momentum=0.9

第一轮计算：
`grad=2`
`v = momentum*v-learning_rate*grads = 0*0.9 - 0.1*2 = -0.2`
`w = w+v = 10-0.2 = 9.8`

第二轮计算：
`grad=2`
`v = momentum*v-learning_rate*grads = 0.9*(-0.2) - 0.1*2 = -0.38`
`w = w+v = 9.8 - 0.38 = 9.42`

第三轮计算：
`grad=2`
`v= momentum*v-learning_rate*grads = 0.9*(-0.38) - 0.1*2 = -0.542`
`w = w+v = 9.42 - 0.542 = 8.878`
```

| 轮次 | grad | v      | w     |
| ---- | ---- | ------ | ----- |
| 1    | 2    | 0      | 9.8   |
| 2    | 2    | -0.38  | 9.42  |
| 3    | 2    | -0.542 | 8.878 |

我们发现，相同梯度情况下，momentum 方案更新权重的速度越来越快。为什么 momentum 能减少震荡呢？因为参数的更新是基于前一轮的梯度进行计算的，如果相邻两轮的梯度变动交到，在SGD算法中就直接产生震荡了，但是在 momentum 算法中，可能不会存在震荡，因为第二次的计算是叠加了第一次的梯度的，两次梯度如果方向相反，会产生叠加，抵消一部分震荡。

代码实现如下：

```py
class Momentum:
    def __init__(self, learning_rate=0.01, momentum=0.9):
        """
        在SGD的基础上增加 momentum 系数，控制加速度
        """
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, value in params.items():
                self.v[key] = np.zeros_like(value)
        for key in params.keys():
            self.v[key] = self.v[key] * self.momentum - self.learning_rate * grads[key]
            params[key] += self.v[key]
```

> 需要注意的是，我们需要维护每一个参数的速度，在每一轮参数更细过程中，更新指定参数的速度值，并根据对应的梯度更新参数

同 SGD 的示例一样，我们也使用等高线图绘制梯度变更路径：

```py
import matplotlib.pyplot as plt
import numpy as np
from optimizer import Momentum

# 使用等高线绘制函数 $f(x,y)=\frac{1}{20}x^2+y^2$的梯度


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0 * y


def move_points():
    init_pos = (-7.0, 2.0)
    params = {}
    params["x"], params["y"] = init_pos[0], init_pos[1]
    grads = {}
    grads["x"], grads["y"] = 0, 0

    x_history = []
    y_history = []
    optimizer = Momentum(learning_rate=0.1)

    for i in range(20):
        x_history.append(params["x"])
        y_history.append(params["y"])

        grads["x"], grads["y"] = df(params["x"], params["y"])
        optimizer.update(params, grads)

    return x_history, y_history


# 绘制等高线
def plot_contour():
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # for simple contour line
    mask = Z > 7
    Z[mask] = 0

    # plot
    # plt.subplot(2, 2, 1)
    plt.figure(figsize=(8, 6))
    x_history, y_history = move_points()
    plt.plot(x_history, y_history, "o-", color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, "+")
    # colorbar()
    # spring()
    plt.title("SGD")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    plot_contour()
```

![](./assets/momentum.png)

观察上图，我们发现，与SGD相比，“之”字形的程度减轻了。这是因为虽然 x 轴方向受到的力非常小，但是一直在同一方向上受力，所以朝同一方向会有一定的加速。反过来，虽然y轴方向受到的力很大，但是因为交替地受到正方向和反方向的力，它们会互相抵消，所以y轴方向上的速度不稳定。

相比 SGD，momentum虽然减轻了震荡，但是并没有解决震荡问题。

### 6.1.5 AdaGrad

SGD 是固定学习率的方式更新参数，momentum 是基于前一次的梯度动态更新参数，两者都无法避免震荡，那么我们能否通过动态计算学习率的方式来实现呢？学习率太小的话更新次数会增加，学习率太大的话，容易错过最佳值。现在我们基于梯度动态更新学习率，来提高学习效率。

在关于学习率的技巧中，有一种称为**学习率衰减**的方法，即随着学习的进行，使学习率逐渐减小。实际上，一开始“多”学，然后逐渐“少”学的方法，在神经网络的学习中经常被使用。

AdaGrad 会为每个参数的每个元素适当第调整学习率，与此同时进行学习（AdaGrad 的 Ada 来自英文单词 Adaptive，即“适当的”）.

$$
h = h + \frac{\partial{L}}{\partial{W}}  \frac{\partial{L}}{\partial{W}}
$$

AdaGrad 的核心思想：历史梯度越大，以后学习率越小。

因为如果某个参数的梯度一直很大，说明其在剧烈变化，应该慢一点更新。如果有个参数梯度一直都很小，说明学习得比较慢，应该快一点更新。

AdaGrad 会保存一个变量：

$$
h_t=h_{t-1}+g_t^2
$$

然后计算更新参数：

$$
θ=θ-η\frac{g}{\sqrt{h}+ε}
$$

其中：

- g：当前梯度
- h：历史梯度的平方累计
- ε：防止除零

> ε 通常为 $10^{-7}$。

为什么需要平方？

1. 负数变正数，我们只关心梯度的大小
2. 大的梯度影响更明显

为什么在更新参数的时候进行开方？

1. 避免学习率下降太快

下面我们使用 Python 实现上述 AdaGrad 学习算法：

```py
class AdaGrad:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, value in grads.items():
                self.h[key] = np.zeros_like(value)
        for key in params.keys():
            self.h[key] = self.h[key] + grads[key] * grads[key]
            params[key] -= (
                self.learning_rate * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            )
```

使用等高线图来分析 AdaGrad 学习路径：

```py
import matplotlib.pyplot as plt
import numpy as np
from optimizer import AdaGrad

# 使用等高线绘制函数 $f(x,y)=\frac{1}{20}x^2+y^2$的梯度


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0 * y


def move_points():
    init_pos = (-7.0, 2.0)
    params = {}
    params["x"], params["y"] = init_pos[0], init_pos[1]
    grads = {}
    grads["x"], grads["y"] = 0, 0

    x_history = []
    y_history = []
    optimizer = AdaGrad(learning_rate=1.5)

    for i in range(20):
        x_history.append(params["x"])
        y_history.append(params["y"])

        grads["x"], grads["y"] = df(params["x"], params["y"])
        optimizer.update(params, grads)

    return x_history, y_history


# 绘制等高线
def plot_contour():
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # for simple contour line
    mask = Z > 7
    Z[mask] = 0

    # plot
    # plt.subplot(2, 2, 1)
    plt.figure(figsize=(8, 6))
    x_history, y_history = move_points()
    plt.plot(x_history, y_history, "o-", color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, "+")
    # colorbar()
    # spring()
    plt.title("SGD")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    plot_contour()
```

![](./assets/AdaGrad.png)

通过观察学习路径，我们发现，随着训练的深入，后面出现了梯度为 0 的问题，导致后续学习路径趋于一条直线，表示后续学习对参数更新微乎其微。

### 6.1.6 RMSProp

我们发现 AdaGrad 有一个明显的短板，随着学习的深入，梯度更新后面趋近于0，导致参数无法更新。**根本原因是AdaGrad记录了所有历史梯度数据**，导致 `h` 的值越来与越大。最终 $\frac{1}{\sqrt{h}}$趋近于 0 。

我们尝试只根据一定比率的最新的历史数据对 AdaGrad 算法进行更新，于是就衍生出了 RMSProp 算法。RMSProp 算法的公式如下：

$$
h_t = ρh_{t-1} + (1-ρ)g^2
$$

其中：

- ρ：表示保留的历史梯度数据的比例

代码实现如下：

```py
class RMSProp:
    def __init__(self, ratio=0.9, learning_rate=0.01):
        self.ratio = ratio
        self.learning_rate = learning_rate
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, value in grads.items():
                self.h[key] = np.zeros_like(value)

        for key in params.keys():
            self.h[key] = (
                self.ratio * self.h[key] + (1 - self.ratio) * grads[key] * grads[key]
            )
            params[key] -= (
                self.learning_rate * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            )
```

我们通过等高线图绘制学习路径来观察 RMSProp 算法：

```py
import matplotlib.pyplot as plt
import numpy as np
from optimizer import RMSProp

# 使用等高线绘制函数 $f(x,y)=\frac{1}{20}x^2+y^2$的梯度


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0 * y


def move_points():
    init_pos = (-7.0, 2.0)
    params = {}
    params["x"], params["y"] = init_pos[0], init_pos[1]
    grads = {}
    grads["x"], grads["y"] = 0, 0

    x_history = []
    y_history = []
    optimizer = RMSProp(ratio=0.9, learning_rate=1.0)

    for i in range(20):
        x_history.append(params["x"])
        y_history.append(params["y"])

        grads["x"], grads["y"] = df(params["x"], params["y"])
        optimizer.update(params, grads)

    return x_history, y_history


# 绘制等高线
def plot_contour():
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # for simple contour line
    mask = Z > 7
    Z[mask] = 0

    # plot
    # plt.subplot(2, 2, 1)
    plt.figure(figsize=(8, 6))
    x_history, y_history = move_points()
    plt.plot(x_history, y_history, "o-", color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, "+")
    # colorbar()
    # spring()
    plt.title("SGD")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    plot_contour()
```

具体展示如下图所示：
![](./assets/RMSProp.png)

### 6.1.7 Adam

为了解决 AdaGrad 算法中梯度消失的问题，我们结合 momentum 算法试试？

Momentum 参照小球在碗中滚动的物理规则进行移动，AdaGrad为参数的每个元素适当地调整更新步伐。
