# 第 2 章 感知机

感知机作为神经网络（深度学习）起源的算法。学习感知机的构造也是学习通往神经网络和深度学习的一种重要思想。

## 2.1 什么是感知机

感知机接收多个输入信号，输出一个信号。

感知机的多个输入信号都有各自固有的权重，这些权重发挥着控制各个信号的重要作用。权重越大，对应该权重的信号的重要性就越高。

感知机就像长江，各个输入数据就好比长江的上游分支，权重就好比每个上游分支的河道宽度，河道越宽，水流量就越大，从该河流分支流入大海的水量也就越大。

我们用以下表达式表示只有两个输入数据的感知机：

$$
y=\left\{
\begin{aligned}
0\qquad(w_1x_1+w_2x_2 \leq θ)\\
1\qquad(w_1x_1+w_2x_2  > θ)\\
\end{aligned}
\right.
$$

## 2.2 简单逻辑电路

### 2.2.1 与门

我们接下来使用感知机解决简单的问题。这里首先以逻辑电路为题材思考与门。

与门逻辑是“两个输入都为真时其结果才为真，其余场景都为假”的逻辑电路。以三峡闸机为例，闸门打开为1，闸门关闭为0；我们的目的是水流流向下游，只有每道闸机都打开了，水流才能顺势流向下游，只要有一道闸机是关闭的，则没有水流通过。

与门的真值表如下所示：

| $x_1$ | $x_2$ | y   |
| ----- | ----- | --- |
| 0     | 0     | 0   |
| 1     | 0     | 0   |
| 0     | 1     | 0   |
| 1     | 1     | 1   |

可以使用 $(w_1, w_2, θ)=(0.5, 0.5, 0.7)$的感知机实现。

### 2.2.2 与非门和或门

与非门是与门逻辑取反的操作，即“两个输入都为真时输出结果为假，其余场景都为真”的逻辑电路。还是以三峡大坝的闸机为例，我们这次的目的是防止三峡下游水患，需要防止上游水流流入下游，此时我们要将所有闸机都关闭，才能做到截断水流。

与非门的真值表如下所示：

| $x_1$ | $x_2$ | y   |
| ----- | ----- | --- |
| 0     | 0     | 1   |
| 1     | 0     | 0   |
| 0     | 1     | 0   |
| 1     | 1     | 0   |

可以使用 $(w_1, w_2, θ)=(-0.5, -0.5, -0.7)$的感知机实现。

或门是只要有一个输入为真则输出结果为真的逻辑电路。类比小区的门禁，我们的目标是进入小区，只要有一个门是开着的，我们就能进入小区。

或门的真值表如下所示：

| $x_1$ | $x_2$ | y   |
| ----- | ----- | --- |
| 0     | 0     | 0   |
| 1     | 0     | 1   |
| 0     | 1     | 1   |
| 1     | 1     | 1   |

可以使用 $(w_1, w_2, θ)=(0.5, 0.5, 0)$的感知机实现。

## 2.3 感知机的实现

### 2.3.1 简单的实现

```py
# 实现感知机


def and_logic(x1, x2):
    """
    与门
    """
    w1, w2, theta = 0.5, 0.5, 0.7
    if x1 * w1 + x2 * w2 <= theta:
        return 0
    else:
        return 1


def not_and_logic(x1, x2):
    """
    与非门
    """
    w1, w2, theta = -0.5, -0.5, -0.7
    if x1 * w1 + x2 * w2 <= theta:
        return 0
    else:
        return 1


def or_logic(x1, x2):
    """
    或门
    """
    w1, w2, theta = 0.5, 0.5, 0
    if x1 * w1 + x2 * w2 <= theta:
        return 0
    else:
        return 1


if __name__ == "__main__":
    input_data = [
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
    ]

    and_result = [and_logic(x1, x2) for [x1, x2] in input_data]
    print(and_result)
    # [0, 0, 0, 1]
    not_and_result = [not_and_logic(x1, x2) for [x1, x2] in input_data]
    print(not_and_result)
    # [1, 1, 1, 0]
    or_result = [or_logic(x1, x2) for [x1, x2] in input_data]
    print(or_result)
    # [0, 1, 1, 1]
```

### 2.3.2 导入权重和偏置

我们将上述感知机的表达式进行转换。

$$
y=\left\{
\begin{aligned}
0\qquad (b + w_1x_1 + w_2x_2 \leq θ)\\
1\qquad (b + w_1x_1 + w_2x_2 > θ)\\
\end{aligned}
\right.
$$

此处，$b$称为**偏置**，$w_1$和$w_2$称为**权重**。

```py
# 实现感知机
import numpy as np

if __name__ == "__main__":
    # 输入
    x = np.array([0, 1])
    # 权重
    w = np.array([0.5, 0.5])
    # 偏置
    b = -0.7
    print(np.sum(w * x) + b)
    # -0.19999999999999996
```

### 2.3.3 使用权重和偏置的实现

```py
# 实现感知机
import numpy as np


def and_logic(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def not_and_logic(x1, x2):
    """
    与非门
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def or_logic(x1, x2):
    """
    或门
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


if __name__ == "__main__":
    input_data = [
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
    ]

    and_result = [and_logic(x1, x2) for [x1, x2] in input_data]
    print(and_result)
    # [0, 0, 0, 1]
    not_and_result = [not_and_logic(x1, x2) for [x1, x2] in input_data]
    print(not_and_result)
    # [1, 1, 1, 0]
    or_result = [or_logic(x1, x2) for [x1, x2] in input_data]
    print(or_result)
    # [0, 1, 1, 1]
```

## 2.4 感知机的局限性

### 2.4.1 异或门

异或门是两个输入数据不相同时结果为真，两个输入数据相同时输出结果为假的逻辑电路。好比一个有两把锁的开关，我们的目标是开锁，如果使用任意相同的两把钥匙都无法开门，只有使用两把各自的钥匙才能打开门。

以下是异或门的真值表：

| $x_1$ | $x_2$ | y   |
| ----- | ----- | --- |
| 0     | 0     | 0   |
| 1     | 0     | 1   |
| 0     | 1     | 1   |
| 1     | 1     | 0   |

我们无法使用前面介绍的感知机直接实现异或门逻辑电路。

我们的感知机函数是一条直线，如果在直接坐标系中绘制上述异或逻辑的数据点，我们发现四个点成矩形分布，其中输出为1的点对应左上角和右下角的两个点，我们无法通过一条直线将其分类。

### 2.4.2 线性和非线性

感知机的局限性在于它只能表示由一条直线分割的空间。弯曲的直线虽然能够将异或门分隔开，但是弯曲的曲线是无法用感知机表示的。由曲线分割而成的空间称为非线性空间。由直线分割而成的空间称为线性空间。

## 2.5 多层感知机

单层感知机无法表示异或门，但是感知机可以叠加，我们不妨试试多层感知机，看是否能够实现异或门表示。

### 2.5.1 已有门电路组合

我们对比前三种门电路，看是否可以将其中两种叠加来生成异或门。

我们发现将输入数据先经过与非门和或门处理之后，将计算结果再经过与门处理之后，输出结果就是异或门。

具体真值表计算如下所示：

| $x_1$ | $x_2$ | NOT_AND | OR  | AND |
| ----- | ----- | ------- | --- | --- |
| 0     | 0     | 1       | 0   | 0   |
| 0     | 1     | 1       | 1   | 1   |
| 1     | 0     | 1       | 1   | 1   |
| 1     | 1     | 0       | 1   | 0   |

### 2.5.2 异或门的实现

```py
# 实现感知机
import numpy as np


def and_logic(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def not_and_logic(x1, x2):
    """
    与非门
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def or_logic(x1, x2):
    """
    或门
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def not_or_logic(x1, x2):
    s1 = not_and_logic(x1, x2)
    s2 = or_logic(x1, x2)
    return and_logic(s1, s2)


if __name__ == "__main__":
    input_data = [
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
    ]

    and_result = [and_logic(x1, x2) for [x1, x2] in input_data]
    print(and_result)
    # [0, 0, 0, 1]
    not_and_result = [not_and_logic(x1, x2) for [x1, x2] in input_data]
    print(not_and_result)
    # [1, 1, 1, 0]
    or_result = [or_logic(x1, x2) for [x1, x2] in input_data]
    print(or_result)
    # [0, 1, 1, 1]
    not_or_result = [not_or_logic(x1, x2) for [x1, x2] in input_data]
    print(not_or_result)
    # [0, 1, 1, 0]
```

这样异或门就通过两层感知机实现了。

## 2.6 从与非门到计算机

## 2.7 小结

- 感知机是具有输入和输出的算法
- 感知机将权重和偏置设为参数
- 使用感知机可以表示与门和或门等逻辑电路
- 异或门无法通过单层感知机实现
- 使用2层感知机可以表示异或门
- 单层感知机只能表示线性空间，而多层感知机可以表示非线性空间
- 多层感知机（理论上）可以表示计算机
