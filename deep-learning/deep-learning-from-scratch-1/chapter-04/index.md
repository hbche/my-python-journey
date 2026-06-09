# 第 4 章 神经网络的学习

本章的主题是神经网络的学习。这里所说的“学习”是指从训练数据中自动获取最优权重参数的过程。本章中，为了使神经网络能进行学习，将引入损失函数这一指标。而学习的目的就是以该损失函数为基准，找出能使它的值达到最小的权重参数。为了找出尽可能小的损失函数的值，本章我们将介绍利用了函数斜率的梯度法。

## 4.1 从数据中学习

神经网络的特征就是可以从数据中学习。所谓“从数据中学习”​，是指可以由数据自动决定权重参数的值。这是非常了不起的事情！因为如果所有的参数都需要人工决定的话，工作量就太大了。在实际的神经网络中，参数的数量成千上万，在层数更深的深度学习中，参数的数量甚至可以上亿，想要人工决定这些参数的值是不可能的。本章将介绍神经网络的学习，即利用数据决定参数值的方法，并用 Python 实现对 MNIST 手写数字数据集的学习。

### 4.1.1 数据驱动

数据是机器学习的命根子。从数据中寻找答案、从数据中发现模式、根据数据讲故事……这些机器学习所做的事情，如果没有数据的话，就无从谈起。因此，数据是机器学习的核心。这种数据驱动的方法，也可以说脱离了过往以人为中心的方法。

通常要解决某个问题，特别是需要发现某种模式时，人们一般会综合考虑各种因素后再给出回答。​“这个问题好像有这样的规律性？​”​“不对，可能原因在别的地方。​”——类似这样，人们以自己的经验和直觉为线索，通过反复试验推进工作。而机器学习的方法则极力避免人为介入，尝试从收集到的数据中发现答案（模式）​。神经网络或深度学习则比以往的机器学习方法更能避免人为介入。

深度学习有时也称为端到端机器学习(end-to-end machine learning)。这里所说的端到端是指从一端到另一端的意思，也就是从原始数据（输入）中获得目标结果（输出）的意思。

接下来我们将尝试设计算法实现识别手写数字识别来学习深度学习中**学习**的过程。

### 4.1.2 训练数据和测试数据

机器学习中，一般将数据分为训练数据和测试数据两部分来进行学习和实验等。首先，使用训练数据进行学习，寻找最优的参数；然后，使用测试数据评价训练得到的模型的实际能力。为什么需要将数据分为训练数据和测试数据呢？因为我们追求的是模型的**泛化能力**。为了正确评价模型的泛化能力，就必须划分训练数据和测试数据。另外，训练数据也可以称为**监督数据**。

泛化能力是指处理未被观察过的数据（不包含在训练数据中的数据）的能力。获得泛化能力是机器学习的最终目标。比如，在识别手写数字的问题中，泛化能力可能会被用在自动读取明信片的邮政编码的系统上。此时，手写数字识别就必须具备较高的识别“某个人”写的字的能力。注意这里不是“特定的某个人写的特定的文字”​，而是“任意一个人写的任意文字”​。如果系统只能正确识别已有的训练数据，那有可能是只学习到了训练数据中的个人的习惯写法。

因此，仅仅用一个数据集去学习和评价参数，是无法进行正确评价的。这样会导致可以顺利地处理某个数据集，但无法处理其他数据集的情况。顺便说一下，只对某个数据集过度拟合的状态称为过拟合(over fitting)。避免过拟合也是机器学习的一个重要课题

## 4.2 损失函数

损失函数是表示神经网络性能的“恶劣程度”的指标，即当前的神经网络对监督数据在多大程度上不拟合，在多大程度上不一致。以“性能的恶劣程度”为指标可能会使人感到不太自然，但是如果给损失函数乘上一个负值，就可以解释为“在多大程度上不坏”​，即“性能有多好”​。并且，​“使性能的恶劣程度达到最小”和“使性能的优良程度达到最大”是等价的，不管是用“恶劣程度”还是“优良程度”​，做的事情本质上都是一样的。

### 4.2.1 均方误差

可以用作损失函数的函数有很多，其中最有名的是**均方误差**(mean squared error)。均方误差如下式(4.1)所示。

$$
E=\frac{1}{2}\sum_{k}(y_k-t_k)^2
$$

这里，$y_k$是表示神经网络的输出，$t_k$表示监督数据，$k$表示数据的维数。比如，在 3.6 节手写数字识别的例子中，$y_k$和$t_k$是由如下 10 个元素构成的数据。

```
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
```

数组元素的索引从第一个开始一次对应数字“0”、“1”、“2”...这里，神经网络的输出 y 是 softmax 函数的输出。由于 softmax 函数的输出可以理解为概率，因此上例表示“0”的概率是 0.1，​“1”的概率是 0.05，​“2”的概率是 0.6 等。t 是监督数据，将正确解标签设为 1，其他均设为 0。这里，标签“2”为 1，表示正确解是“2”​。将正确解标签表示为 1，其他标签表示为 0 的表示方法称为**one-hot**表示。

如式(4.1)所示，均方误差会计算神经网络的输出和正确解监督数据的各个元素之差的平方，再求和。现在，我们用 Python 来实现这个均方误差，实现方式如下所示。

```py
def mean_squared_error(y, t):
    """
    均方误差
    """
    return 0.5 * np.sum((y - t) ** 2)
```

这里，参数 $y$ 和 $t$ 是 NumPy 数组。代码实现完全遵照式(4.1)，因此不再具体说明。现在，我们使用这个函数，来实际计算一下：

```py
if __name__ == "__main__":
    # 假设 "2" 为正确解
    y1 = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
    y2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    result = mean_squared_error(y1, t)
    print(result)  # 0.09750000000000003
    result = mean_squared_error(y2, t)
    print(result)  # 0.5975
```

这里举了两个例子。第一个例子中，正确解是“2”，神经网络的输出最大值也是“2”，因为“2”索引对应输出概率是最高的；第二个例子中，正确解是“2”，神经网络的输出最大值是“7”。如实验结果所示，我们发现第一个例子的损失函数值更小，和监督数据之间的误差较小。也就是说，均方误差显示第一个例子的输出结果与监督数据更加吻合。

### 4.2.2 交叉熵误差

除了均方误差之外，**交叉熵误差**(cross entropy error)也经常被用作损失函数。交叉熵误差如下式(4.2)所示。

$$
E=-\sum_{k}{t_k}\log({y_k})
$$

这里 $log$ 表示以 $e$ 为底数的自然对数($log_e$)。$y_k$是神经网络的输出，$t_k$是正确解标签。并且，$t_k$中只有正确解标签的索引为 1，其他均为 0（one-hot 表示）。因此，式(4.2)实际上只计算对应正确解标签的输出的自然对数。比如，假设正确解标签索引是“2”，与之对应的神经网络的输出是 0.6，则交叉熵误差是$-log0.6=0.51$。也就是说，交叉熵误差的值是由正确解标签所对应的输出结果决定的。

自然对数的图像如下图所示：

![](./assets/ln_x.png)

如图所示，x 等于 1 时，y 为 0；随着 x 向 0 靠近，y 逐渐变小。因此，正确解标签对应的输出越大，交叉熵误差的值越接近 0；当输出为 1 时，交叉熵误差为 0。此外，如果正确解标签对应的输出较小，则交叉熵误差的值较大。

下面，我们来用代码实现交叉熵误差。

```py
def cross_entropy_error(y, t):
    """
    交叉熵误差
    """
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
```

这里，参数 $y$ 和 $t$ 都是 NumPy 数组。函数内部在计算 $np.log$时，加上了一个微小值 delta 。这是因为，如果神经网络对应的输出 $y_k$ 为 0 时，即当出现$np.log(0)$时，$np.log(0)$会变成一个负无限大的 $-inf$，这样以来，就会导致后续计算无法进行。作为保护性对策，添加一个微小值可以防止负无限大的发生。下面，我们使用 cross_entropy_error(y, t) 进行一些简单的计算。

```py
if __name__ == "__main__":
    # 假设 "2" 为正确解
    y1 = np.array([0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0])
    y2 = np.array([0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0])
    t = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
    result = cross_entropy_error(y1, t)
    print(result)  # 0.510825457099338
    result = cross_entropy_error(y2, t)
    print(result)  # 2.302584092994546
```

由于我们的标签数据是 "One-hot" 形式，所以我们只需要计算正确解标签与该标签索引对应的神经网络输出值进行计算，其余不需要计算，因为其余的计算都是 0 （$-(0*log(y_k))$）。第一个例子中，正确解标签对应的输出为 0.6，此时的交叉熵误差大约为 0.51。第二个例子中，正确解标签对应的输出为 0.1，此时的交叉熵误差大约为 2.3。由此可以看出，这些结果与我们前面讨论的内容是一致的。

### 4.2.3 mini-batch 学习

机器学习使用训练数据进行学习。使用训练数据进行学习，严格来说，就是针对训练数据计算损失函数的值，找出使该值尽可能小的参数。因此，计算损失函数时必须将所有的训练数据作为对象。也就是说，如果训练数据有 100 个的话，我们就要把这 100 个损失函数的总和作为学习的指标。

前面介绍的损失函数的例子中考虑的都是针对单个数据的损失函数。如果要求所有训练数据的损失函数的总和，以交叉熵误差为例，可以写成下面的式(4.3)。

$$
E=-
\frac{1}{N}\sum_n\sum_kt_{nk}log({y_{nk}})
$$

这里，假设数据有 N 个，$t_{nk}$表示第 n 个数据的第 k 个元素的值($y_{nk}$是神经网络的输出，$t_{nk}$是监督数据)。式子虽然看起来有一些复杂，其实只是把求单个数据的损失函数的式(4.2)扩大到了 N 份数据，不过最后还要除以 N 进行正则化。通过除以 N，可以求单个数据的“平均损失函数”。通过这样的平均化，可以获得和训练数据的数量无关的统一指标。比如，即便训练数据有 1000 个或 10000 个，也可以求得单个数据的平均损失函数。

神经网络的学习是从训练数据中选出一批数据（称为 mini-batch，小批量），然后对每个 mini-batch 进行学习。比如，从 60000 个训练数据中随机选择 100 个，在用这 100 个数据进行学习。这种学习方式称为 mini-batch 学习。

下面我们来编写从训练数据中随机选择指定个数的数据的代码，以进行 mini-batch 学习。在这之前，先来看一下用于读入 MNIST 数据集的代码。

```py
import os
import sys
from mnist import load_mnist
sys.path.append(os.pardir)

sys.path.append(os.pardir)
(x_train, t_train), (x_test, t_test) = load_mnist(
    normalize=True, one_hot_label=True
)
print(x_train.shape)    # (60000, 784)
print(t_train.shape)    # (60000, 10)
```

读入上面的 MNIST 数据后，训练数据有 60000 个，输入数据是 784 维(28 x 28)的图像数据，监督数据时 10 维的数组。因此，上面的 x_train、t_train 的形状分别是 (60000, 784) 和 (60000, 10)。

接下来我们可以使用 Numpy 的 np.random.choice() 函数随机抽取数据：

```py
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size, batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
print(x_batch.shape)    # (10, 784)
print(t_batch.shape)    # (10, 10)
```

使用 np.random.choice()可以从指定的数字中随机选择想要的数字。比如，np.random.choice(60000, 10)会从 0 到 59999 之间随机选择 10 个数字。

之后，我们只需指定这些随机选出的索引，取出 mini-batch，然后使用这个 mini-batch 计算损失函数即可。

> mini-batch 的损失函数是利用一部分样本数据来近似地计算整体。也就是说，用随机选择的小批量数据(mini-batch)作为全体训练数据的近似值。

### 4.2.4 mini-batch 版交叉熵误差实现

我们现在基于之前的交叉熵误差实现代码进行改良，使其支持 mini-batch 模式：

```py
def cross_entropy_error(y: np.array, t):
    """
    交叉熵误差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = t.reshape(1, y.size)
    batch_size = y.shape[0]
    delta = 1e-7
    return -np.sum(t * np.log((y + delta))) / batch_size
```

这里，y 是神经网络的输出，t 是监督数据。y 的维度为 1 时，即求单个数据的交叉熵误差时，需要改变数据的形状。并且，当输入为 mini-batch 时，要用 batch 的个数进行正规化，计算单个数据的平均交叉熵误差。

此外，当监督数据时标签形式(非 one-hot 表示，而是像 “2”、“7” 这样的标签)时，交叉熵误差可通过如下代码实现：

```py
def cross_entropy_error(y, t):
    """
    交叉熵误差计算：
    y: 预测值
    t: 监督数据，非 ont-hot 格式，例如 [2, 7, 0, 9]，而不是 [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], ...] 这种 one-hot 编码格式
    """
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    delta = 1e-7
    batch_size = y.shape[0]
    # 如果 t 不是 one-hot 编码格式，我们可以直接根据 t 的标签值作为索引取对应位置的预测值进行 ln() 计算即可，而不需要将 t 转换为 one-hot 编码格式
    return -np.sum(np.log(y[np.arange(batch_size), t] + delta)) / batch_size
```

实现的要点是，由于 one-hot 表示中 t 为 0 的元素的交叉熵误差也为 0，因此针对这些元素的计算可以忽略。换言之，如果可以获得神经网络在正确解标签处的输出，就可以计算交叉熵误差。因此，t 为 one-hot 表示时通过 `t*np.log(y)` 计算的地方，在 t 为标签形式时，可用 `np.log(y[np.arange(batch_size), t])` 实现相同的处理（为了便于观察，此处省略了微小值 $1e-7$）。

作为参考，简单介绍一下 `np.log(y[np.arange(batch_size), t])`。`np.arange(batch_size)`会生成一个从 0 到 batch_size - 1 的数组。比如当 batch_size 为 5 时，`np.arange(batch_size)`会生成一个 NumPy 数组[0, 1, 2, 3, 4]。因为 t 中标签是以[2, 7, 0, 9, 4]的形式存储的，所以`y[np.arange(batch_size), t]` 会生成 NumPy 数组 `[y[0, 2], y[1, 7], y[2, 0], y[3, 9], y[4, 4]]`。

### 4.2.5 为何要设定损失函数

在神经网络的学习中，寻找最优参数（权重和偏置）时，要寻找使损失函数的值尽可能小的参数。为了找到使损失函数的值尽可能小的地方，需要计算参数的导数（确切地说是梯度），然后以这个导数为指引，逐步更新参数的值。

假设有一个神经网络，现在我们来关注这个神经网络中的某一个权重参数。此时，对该权重参数的损失函数求导，表示的是“如果稍微改变这个权重参数的值，损失函数的值会如何多少”。如果导数的值为负数，通过使该权重参数向正方向改变，可以减小损失函数的值；反过来，如果导数的值为正，则通过使该权重参数向负方向改变，可以减小损失函数的值。不过，当导数的值为 0 时，无论权重参数向哪个方向变化，损失函数的值都不会改变，此时该权重参数的更新会停在此处。

之所以不能以识别精度作为指标，是因为这样一来绝大多数地方的导数都会变为 0，导致参数无法更新。

> 在进行神经网络的学习时，不能将识别精度作为指标。因为如果以识别精度作为指标，则参数的导数在绝大多数地方都会变为 0。

假设某个神经网络正确识别出了 100 笔训练数据中的 32 笔，此时识别精度为 32%。如果以识别精度为指标，即使稍微改变权重参数的值，识别精度也仍将保持在 32%，不会出现变化。也就是说，仅仅微调参数，是无法改善识别精度的。即便识别精度有所改善，它的值也不会像 32.0123...% 这样连续变化，而是变为 33%、34%这样的不连续的、离散的值。而如果把损失函数作为指标，则当前损失函数的值可以表示为 0.92543...这样的值。并且，如果稍微改变一下参数的值，对应的损失函数也像 0.93432...这样发生连续性的变化。

识别精度对微小的参数变化基本上没有什么反应，即便有反应，它的值也是不连续地、突然地变化。作为激活函数的阶跃函数也有同样的情况。出于相同的原因，如果使用阶跃函数作为激活函数，神经网络的学习将无法进行。阶跃函数的导数在绝大多数地方（除了 0 以外的地方）均为 0。也就是说，如果使员工了阶跃函数，那么即便将损失函数作为指标，参数的微小变化也会被阶跃函数抹杀，导致损失函数的值不会产生任何变化。

阶跃函数就像“竹筒敲石”一样，只在某个瞬间产生变化。而 sigmoid 函数，不仅函数的输出是连续变化的，曲线的斜率（导数）也是连续变化的。也就是说，sigmoid 函数的导数在任何地方都不为 0。这对神经网络的学习非常重要。得益于这个斜率不会为 0 的性质，神经网络的学习得以正确进行。

## 4.3 数值微分

梯度法使用梯度的信息决定前进的方向。本节将介绍梯度是什么、有什么性质等内容。

### 4.3.1 导数

导数就是表示某个瞬间的变化量。它可以定义成下面的式子。

$$
\frac{df(x)}{dx} = \lim_{h->0}\frac{f(x+h)-f(x)}{h}
$$

式（4.4）表示的是函数的导数。表示的导数的含义是，x 的“微小变化”将导致函数 f(x)的值在多大程度上发生变化。其中，表示微小变化的 h 无限趋近 0，表示为$\lim_{h->0}$。

接下来，我们参考式（4.4），来实现求函数的导数的程序。如果直接实现式（4.4）的话，向 h 中赋入一个微小值，就可以计算出来了。

```py
def numerical_diff(f, x):
    h = 10e-50
    return (f(x+h)-f(x))/h
```

乍一看这个实现没有问题，但是实际上这段代码有两处需要改进的地方。

在上面的实现中，因为想把尽可能小的值赋给 h（可以的话，想让 h 无限趋近 0），所以 h 使用了 10e-50 这个微小值。但是，这样反而产生了舍入误差。所谓舍入误差，是指因为省略小数的精细部分的数值而造成最终的计算结果上的误差。比如，在 Python 中，舍入误差如下所示：

```py
print(np.float32(10e-50))   # 0.0
```

如上所示，如果用 float32 类型（32 位的浮点数）来表示 10e-50 ，就会变成 0.0，无法正确表示出来。也就是说，使用过小的值会造成计算机出现计算上的问题。这是第一个需要改进的地方，即将微小值 h 改为 $10^{-4}$。使用 $10^{-4}$ 即可计算正确的结果。

第二个需要改进的地方与函数 f 的差分有关。虽然上述实现中计算了函数 f 在 x+h 和 x 之间的差分，但是必须注意到，这个计算从一开始就有误差。“真的导数”对应函数在 x 处的斜率（称为切线）​，但上述实现中计算的导数对应的是(x+h)和 x 之间的斜率。因此，真的导数（真的切线）和上述实现中得到的导数的值在严格意义上并不一致。这个差异的出现是因为 h 不可能无限接近 0。

数值微分含有误差。为了减小这个误差，我们可以计算函数 f 在(x+h)和(x-h)之间的差分。因为这种计算方法以 x 为中心，计算它左右两边的差分，所以也称为**中心差分**（而(x+h)和 x 之间的差分称为**前向差分**）​。下面，我们基于上述两个要改进的点来实现数值微分（数值梯度）​。

```py
def numerical_diff(f, x):
    h = 1e-4
    return (f(x + h) - f(x-h)) / (2 * h)
```

> 利用微小的差分求导数的过程称为数值微分(numerical differentiation)。而基于数学式的推导求导数的过程，则用“解析性”(analytic)一词，称为“解析性求解”或者“解析性求导”​。比如，$y=x^2$的导数，可以通过$\frac{dy}{dx}=2x$解析性地求解出来。因此，当 x= 2 时，y 的导数为 4。解析性求导得到的导数是不含误差的“真的导数”​。

### 4.3.2 数值微分的例子

我们试着用上述的数值微分对简单函数进行求导。

```py
def function_1(x):
    return 0.01 * x**2 + 0.1 * x
```

接下来，我们来绘制这个函数的图像：

```py
def plot_function_1():
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    plt.show()

plot_function_1()
```

我们来计算一下这个函数在 x=5 和 x=10 处的导数：

```py
gradient_5 = numerical_diff(function_1, 5)
print(gradient_5)  # 0.1999999999990898
gradient_10 = numerical_diff(function_1, 10)
print(gradient_10)  # 0.2999999999986347
```

这里计算的导数是 f(x)相对于 x 的变化量，对应函数的斜率。另外，$f(x)=0.01x^2+0.1x$的解析解是$\frac{dy}{dx}=0.02x+0.1$。因此，在 x= 5 和 x= 10 处，​“真的导数”分别为 0.2 和 0.3。和上面的结果相比，我们发现虽然严格意义上它们并不一致，但误差非常小。实际上，误差小到基本上可以认为它们是相等的。

### 4.3.3 偏导数

接下来，我们看一下式(4.6)表示的函数。虽然它只是一个计算参数的平方和的简单函数，但是请注意和上例不同的是，这里有两个变量。

$$
f(x_0, x_1)=x_0^2+x_1^2
$$

这个式子可以用 Python 表示如下：

```py
def funciton_2(x):
    return x[0] ** 2 + x[1] ** 2
    # return np.sum(x**2)
```

现在我们来求式(4.6)的导数。这里需要注意的是，式(4.6)有两个变量，所以有必要区分对哪个变量求导数，即对$x_0$和$x_1$两个变量中的哪一个求导数。另外，我们把这里讨论的有多个变量的函数的导数称为**偏导数**。用数学式表示的话，可以写成$\frac{\partial f}{\partial x_0}$、$\frac{\partial f}{\partial x_1}$。

怎么求解偏导数呢？我们先试着解一下下面两个关于偏导数的问题。

- 问题 1：求$x_0=3,x_1=4$时，关于$x_0$的偏导数$\frac{\partial f}{\partial x_0}$

  ```py
  def funciton_tmp1(x0):
    return x0 **2 + 4.0 ** 2.0
  print(numerical_diff(funciton_tmp1, 3.0))   # 6.00000000000378
  ```

- 问题 2：求$x_0=3,x_1=4$时，关于$x_0$的偏导数$\frac{\partial f}{\partial x_1}$

  ```py
  def function_tmp2(x1):
      return 3.0 **2 + x1 ** 2.0
  print(numerical_diff(function_tmp2, 4.0))   # 7.999999999999119
  ```

在这些问题中，我们定义了一个只有一个变量的函数，并对这个函数进行了求导。例如，问题 1 中，我们定义了一个固定 $x_1=4$ 的新函数，然后对只有变量 $x_0$ 的函数应用了求数值微分的函数。从上面的计算结果可知，问题 1 的答案是 6.00000000000378，问题 2 的答案是 7.999999999999119，和解析解的导数基本一致。

像这样，偏导数和单变量的导数一样，都是求某个地方的斜率。不过，偏导数需要将多个变量中的某一个变量定义为目标变量，并将其他变量固定为某个值。在上例的代码中，为了将目标变量以外的变量固定到某些特定的值上，我们定义了新函数。然后，对新定义的函数应用了之前的求数值微分的函数，得到偏导数。

## 4.4 梯度

在刚才的例子中，我们按变量分别计算了 $x_0$ 和 $x_1$ 的偏导数。现在，我们希望一起计算 $x_0$ 和 $x_1$ 的偏导数。比如，我们来考虑求 $x_0=3, x_1=4$ 时 $(x_0, x_1)$ 的偏导数 $(\frac{\partial{f}}{\partial{x_0}}, \frac{\partial{f}}{\partial{x_1}})$。另外，像$(\frac{\partial{f}}{\partial{x_0}}, \frac{\partial{f}}{\partial{x_1}})$ 这样的由全部变量的偏导数汇总而成的向量称为**梯度**（gradient）。梯度可以像下面这样来实现：

```py
def numerical_gradient(f, x):
    """
    数值求梯度
    f: 目标函数
    x: 目标函数的输入值，numpy 数组
    """
    h = 1e-4
    gradient_x = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        # f(x-h) 的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        gradient_x[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return gradient_x
```

函数 numerical_gradient(f, x)的实现看上去有些复杂，但它执行的处理和求单变量的数值微分基本没有区别。需要补充说明一下的是，np.zeros_like(x)会生成一个形状和 x 相同、所有元素都为 0 的数组。

函数 numerical_gradient(f, x)中，参数 f 为函数，x 为 NumPy 数组，该函数对 NumPy 数组 x 的各个元素求数值微分。现在，我们用这个函数实际计算一下梯度。这里我们求点(3, 4)、(0, 2)、(3, 0)处的梯度。

```py
print(numerical_gradient(function_2, np.array([3.0, 4.0])))    # [6. 8.]
print(numerical_gradient(function_2, np.array([0.0, 2.0])))    # [0. 4.]
print(numerical_gradient(function_2, np.array([3.0, 0.0])))    # [6. 0.]
```

### 4.4.1 梯度法

机器学习的主要任务是在学习时寻找最优参数。同样地，神经网络也必须在学习时找到最优参数（权重和偏置）​。这里所说的最优参数是指损失函数取最小值时的参数。但是，一般而言，损失函数很复杂，参数空间庞大，我们不知道它在何处能取得最小值。而通过巧妙地使用梯度来寻找函数最小值（或者尽可能小的值）的方法就是梯度法。

这里需要注意的是，梯度表示的是各点处的函数值减小最多的方向。因此，无法保证梯度所指的方向就是函数的最小值或者真正应该前进的方向。实际上，在复杂的函数中，梯度指示的方向基本上都不是函数值最小处。

> 函数的极小值、最小值以及被称为鞍点(saddle point)的地方，梯度为 0。极小值是局部最小值，也就是限定在某个范围内的最小值。鞍点是从某个方向上看是极大值，从另一个方向上看则是极小值的点。虽然梯度法是要寻找梯度为 0 的地方，但是那个地方不一定就是最小值（也有可能是极小值或者鞍点）​。此外，当函数很复杂且呈扁平状时，学习可能会进入一个（几乎）平坦的地区，陷入被称为“学习高原”的无法前进的停滞期。

虽然梯度的方向并不一定指向最小值，但沿着它的方向能够最大限度地减小函数的值。因此，在寻找函数的最小值（或者尽可能小的值）的位置的任务中，要以梯度的信息为线索，决定前进的方向。

此时梯度法就派上用场了。在梯度法中，函数的取值从当前位置沿着梯度方向前进一定距离，然后在新的地方重新求梯度，再沿着新梯度方向前进，如此反复，不断地沿梯度方向前进。像这样，通过不断地沿梯度方向前进，逐渐减小函数值的过程就是梯度法(gradient method)。梯度法是解决机器学习中最优化问题的常用方法，特别是在神经网络的学习中经常被使用。

现在，我们尝试用数学式来表示梯度法，如式(4.7)所示。

$$
x_0 = x_0 - η\frac{\partial{f}}{\partial{x_0}}
$$

$$
x_1 = x_1 - η\frac{\partial{f}}{\partial{x_1}}
$$

式(4.7)的 η 表示更新量，在神经网络的学习中，称为学习率(learning rate)。学习率决定在一次学习中，应该学习多少，以及在多大程度上更新参数。

学习率需要事先确定为某个值，比如 0.01 或 0.001。一般而言，这个值过大或过小，都无法抵达一个“好的位置”​。在神经网络的学习中，一般会一边改变学习率的值，一边确认学习是否正确进行了。

下面，我们用 Python 来实现梯度下降法。如下所示，这个实现很简单。

```py
def gradient_descent(f, init_x, learning_rate=0.01, step_num=100):
    x = init_x
    """
    梯度下降
    f: 目标函数
    init_x: 目标函数的输入值，numpy 数组
    learning_rate: 学习率
    step_num: 迭代次数
    """
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= learning_rate * grad
    return x
```

参数 f 是要进行最优化的函数，init_x 是初始值，lr 是学习率 learning rate，step_num 是梯度法的重复次数。numerical_gradient(f,x)会求函数的梯度，用该梯度乘以学习率得到的值进行更新操作，由 step_num 指定重复的次数。

使用这个函数可以求函数的极小值，顺利的话，还可以求函数的最小值。下面，我们就来尝试解决下面这个问题。

问题：请用梯度法求解 $f(x)=x_0^2 + x_1^2$

```py
print(gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=0.1))    # [-6.11110793e-10  8.14814391e-10]
```

这里，设初始值为(-3.0, 4.0)，开始使用梯度法寻找最小值。最终的结果是(-6.1e-10,8.1e-10)，非常接近(0, 0)。实际上，真的最小值就是(0, 0)，所以说通过梯度法我们基本得到了正确结果。

前面说过，学习率过大或者过小都无法得到好的结果。我们来做个实验验证一下。

```py
print(gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=10))
# [-2.58983747e+13 -1.29524862e+12]

print(gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=1e-10))
# [-2.99999994  3.99999992]
```

实验结果表明，学习率过大的话，会发散成一个很大的值；反过来，学习率过小的话，基本上没怎么更新就结束了。也就是说，设定合适的学习率是一个很重要的问题。

> 像学习率这样的参数称为超参数。这是一种和神经网络的参数（权重和偏置）性质不同的参数。相对于神经网络的权重参数是通过训练数据和学习算法自动获得的，学习率这样的超参数则是人工设定的。一般来说，超参数需要尝试多个值，以便找到一种可以使学习顺利进行的设定。

### 4.4.2 神经网络的梯度

神经网络的学习也要求梯度。这里所说的梯度是指损失函数关于权重参数的梯度。比如，有一个只有形状为 2x3 的权重 $W$ 的神经网络，损失函数用 $L$ 表示。此时，梯度可以用 $\frac{\partial{L}}{\partial{W}}$ 表示。用数学式表示的话，如下所示。

$$
W = \begin{pmatrix} w_{11} & w_{12} & w_{13} \\ w_{21} & w_{22} & w_{23} \end{pmatrix}
$$

$$
\frac{\partial{L}}{\partial{W}} = \begin{pmatrix} \frac{\partial{L}}{\partial{w_{11}}} & \frac{\partial{L}}{\partial{w_{12}}} & \frac{\partial{L}}{\partial{w_{13}}} \\ \frac{\partial{L}}{\partial{w_{21}}} & \frac{\partial{L}}{\partial{w_{22}}} & \frac{\partial{L}}{\partial{w_{23}}} \end{pmatrix}
$$

$\frac{\partial{L}}{\partial{W}}$的各元素关于$W$的偏导数。比如，第 1 行第 1 列的元素$\frac{\partial{L}}{\partial{w_{11}}}$表示当$w_{11}$稍微变化时，损失函数 L 会发生多大变化。这里的重点是，$\frac{\partial{L}}{\partial{W}}$的形状和$W$相同。实际上，上式中的 $W$ 和 $\frac{\partial{L}}{\partial{W}}$ 都是 2x3 的形状。

下面，我们以一个简单的神经网络为例，来实现求梯度的代码。为此，我们要实现一个名为 SimpleNet 的类。

```py
import numpy as np

def softmax(x):
    """
    softmax 的 Docstring

    :param x: 说明
    """
    max_x = np.max(x)
    normal_x = np.exp(x - max_x + 1e-4)
    return normal_x / np.sum(normal_x)

def cross_entropy(x, t):
    if x.ndim == 1:
        x = x.reshape(1, x.size)
        t = t.reshape(1, t.size)
    batch_size = t.shape[0]
    return -np.sum(t*np.log(x + 1e-7))/batch_size

def _numerical_gradient_no_batch(f, x):
    """
    数值求梯度
    f: 目标函数
    x: 目标函数的输入值，numpy 数组
    """
    h = 1e-4
    gradient_x = np.zeros_like(x)
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)
        # f(x-h) 的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)
        gradient_x[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return gradient_x

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        return grad


class SimpleNet:

    def __init__(self):
        """
        __init__: 初始化权重参数

        :param self: 说明
        """
        self.W = np.random.randn(2, 3)  # 使用高斯分布进行初始化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        y = self.predict(x)
        z = softmax(y)
        loss = cross_entropy(z, t)

        return loss
```

SimpleNet 类只有一个实例变量，即形状为 2×3 的权重参数。它有两个方法，一个是用于预测的 predict(x)，另一个是用于求损失函数值的 loss(x,t)。这里参数 x 接收输入数据，t 接收正确解标签。现在我们来试着用一下这个 SimpleNet。

```py
if __name__ == '__main__':
    net = SimpleNet()
    net.W = np.array([
        [0.47355232, 0.9977393, 0.84668094],
        [0.85557411, 0.03563661, 0.69422093]
    ])
    print(net.W)
    # [[0.47355232 0.9977393  0.84668094]
    # [0.85557411 0.03563661 0.69422093]]

    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print(p)
    # [1.05414809 0.63071653 1.1328074 ]

    print(np.argmax(p))
    # 2

    t = np.array([0, 0, 1])
    loss = net.loss(x, t)
    print(loss)
    # 0.9280682857864075
```

接下来求梯度。和前面一样，我们使用 numerical_gradient(f, x)求梯度（这里定义的函数 f(W)的参数 W 是一个伪参数。因为 numerical_gradient(f, x)会在内部执行 f(x)，为了与之兼容而定义了 f(W)）​。

```py
loss_w = lambda W: net.loss(x, t)
dw = numerical_gradient(loss_w, net.W)
print(dw)
# [[ 0.21924757  0.14356243 -0.36281   ]
# [ 0.32887136  0.21534364 -0.544215  ]]
```

numerical_gradient(f, x)的参数 f 是函数，x 是传给函数 f 的参数。因此，这里参数 x 取 net.W，并定义一个计算损失函数的新函数 f，然后把这个新定义的函数传递给 numerical_gradient(f, x)。

numerical\*gradient(f, net.W)的结果是 dW，一个形状为 2×3 的二维数组。观察一下 dW 的内容，例如，会发现$\frac{\partial{L}}{\partial{W}}$中的$\frac{\partial{L}}{\partial{w_{11}}}$的值大约是 0.2，这表示如果将$w_{11}$增加 h，那么损失函数的值会增加 0.2h。再如，$\frac{\partial{L}}{\partial{w_{23}}}$对应的值大约是-0.5，这表示如果将$w_{23}$增加 h，损失函数的值将减小 0.5h。因此，从减小损失函数值的观点来看，$w_{23}$应向正方向更新，$w_{11}$应向负方向更新。至于更新的程度，$w_{23}$比$w_{11}$的贡献要大。

求出神经网络的梯度后，接下来只需根据梯度法，更新权重参数即可。在下一节中，我们会以 2 层神经网络为例，实现整个学习过程。

## 4.5 学习算法的实现

关于神经网络学习的基础知识，到这里就全部介绍完了。​“损失函数”​“mini-batch”​“梯度”​“梯度下降法”等关键词已经陆续登场，这里我们来确认一下神经网络的学习步骤，顺便复习一下这些内容。神经网络的学习步骤如下所示。

- 前提
  - 神经网络存在合适的权重和偏置，调整权重和偏置以便拟合训练数据的过程称为“学习”。神经网络的学习分成下面 4 个步骤。
- ## 步骤 1（mini-batch）
  - 从训练数据中随机选出一部分数据，这部分数据成为 mini-batch。我们的目标是减小 mini-batch 损失函数的值。
- 步骤 2（计算梯度）
  - 为了减小 mini-bach 的损失函数的值，需要求出各权重参数的梯度。梯度表示损失函数的值减小最多的方向
- ## 步骤 3（更新参数）
  - 将权重参数沿梯度方向进行微小更新
- 步骤 4（重复）
  - 重复步骤 1、2、3

关于神经网络学习的基础知识，到这里就全部介绍完了。​“损失函数”​“mini-batch”​“梯度”​“梯度下降法”等关键词已经陆续登场，这里我们来确认一下神经网络的学习步骤，顺便复习一下这些内容。神经网络的学习步骤如下所示。

下面，我们来实现手写数字识别的神经网络。这里以 2 层神经网络（隐藏层为 1 层的网络）为对象，使用 MNIST 数据集进行学习。

### 4.5.1 2 层神经网络的类

首先，我们将这个 2 层神经网络实现为一个名为 TwoLayerNet 的类，实现过程如下所示：

```py
import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def softmax(x):
    max_x = np.max(x)
    normal_x = np.exp(x-max_x + 1e-4)
    return normal_x/np.sum(normal_x)

def cross_entropy(x, t):
    if x.ndim == 1:
        x = x.reshape(1, x.size)
        t = t.reshape(1, t.size)
    batch_size = t.shape[0]
    return -np.sum(t*np.log(x + 1e-7))/batch_size

def _numerical_gradient(f, x):
    grad = np.zeros_like(x)
    h = 1e-7
    for i in range(x.size):
        temp_x = x[i]

        x[i] = temp_x + h
        fxh1 = f(x)

        x[i] = temp_x - h
        fxh2 = f(x)

        grad[i] = (fxh2-fxh1)/(2*h)
        x[i] = temp_x

    return grad

def numerical_gradient(f, x):
    if x.ndim == 1:
        return _numerical_gradient(f, x)
    else:
        grads = np.zeros_like(x)
        for i, x_item in enumerate(x):
            grads[i] = _numerical_gradient(f, x_item)
        return grads

class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init=0.01):
        self.params = {}

        self.params['W1'] = np.random.randn(input_size, hidden_size) * weight_init
        self.params['b1'] = np.random.randn(hidden_size)
        self.params['W2'] = np.random.randn(hidden_size, output_size) * weight_init
        self.params['b2'] = np.random.rand(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        z2 = softmax(a2)

        return z2

    def loss(self, x, t):
        y = self.predict(x)
        return cross_entropy(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t)/float(t.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss = lambda w: self.loss(x, t)
        grads = {}
        grads['W1'] = numerical_gradient(loss, self.params['W1'])
        grads['b1'] = numerical_gradient(loss, self.params['b1'])
        grads['W2'] = numerical_gradient(loss, self.params['W2'])
        grads['b2'] = numerical_gradient(loss, self.params['b2'])

        return grads

if __name__ == '__main__':
    net = TwoLayerNet(784, 100, 10)
    # print(net.params['W1'].shape)
    # print(net.params['b1'].shape)
    # print(net.params['W2'].shape)
    # print(net.params['b2'].shape)

    # x = np.random.randn(100, 784)
    # y = net.predict(x)
    # print(y)
    x = np.random.randn(100, 784)
    t = np.random.randn(100, 10)
    grads = net.numerical_gradient(x, t)
    print(grads['W1'].shape)
    print(grads['b1'].shape)
    print(grads['W2'].shape)
    print(grads['b2'].shape)
```

接着，我们来看一下 TwoLayerNet 的方法的实现。首先是**init**(self, input_size,hidden_size, output_size)方法，它是类的初始化方法（所谓初始化方法，就是生成 TwoLayerNet 实例时被调用的方法）​。从第 1 个参数开始，依次表示输入层的神经元数、隐藏层的神经元数、输出层的神经元数。另外，因为进行手写数字识别时，输入图像的大小是 784(28×28)，输出为 10 个类别，所以指定参数 input_size=784、output_size=10，将隐藏层的个数 hidden_size 设置为一个合适的值即可。

此外，这个初始化方法会对权重参数进行初始化。如何设置权重参数的初始值这个问题是关系到神经网络能否成功学习的重要问题。后面我们会详细讨论权重参数的初始化，这里只需要知道，权重使用符合高斯分布的随机数进行初始化，偏置使用 0 进行初始化。predict(self, x)和 accuracy(self, x, t)的实现和上一章的神经网络的推理处理基本一样。如果仍有不明白的地方，请再回顾一下上一章的内容。另外，loss(self, x, t)是计算损失函数值的方法。这个方法会基于 predict()的结果和正确解标签，计算交叉熵误差。

剩下的 numerical_gradient(self, x, t)方法会计算各个参数的梯度。根据数值微分，计算各个参数相对于损失函数的梯度。另外，gradient(self, x, t)是下一章要实现的方法，该方法使用误差反向传播法高效地计算梯度。

### 4.5.2 mini-batch 的实现

神经网络的学习的实现使用的是前面介绍过的 mini-batch 学习。所谓 mini-batch 学习，就是从训练数据中随机选择一部分数据（称为 mini-batch）​，再以这些 mini-batch 为对象，使用梯度法更新参数的过程。

```py
import numpy as np
from mnist import load_mnist
from two_layer_network import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
train_loss_list = []

# 超参数
iters_number = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.01

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

for i in range(iters_number):
    # 获取mini-batch
    train_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[train_mask]
    t_batch = t_train[train_mask]

    # 计算梯度
    grads = net.numerical_gradient(x_batch, t_batch)
    # 更新参数
    for key in ("W1", "b1", "W2", "b2"):
        net.params[key] = net.params[key] - learning_rate * grads[key]

    # 记录学习过程
    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)
```

这里，mini-batch的大小为100，需要每次从60000个训练数据中随机取出100个数据（图像数据和正确解标签数据）​。然后，对这个包含100笔数据的mini-batch求梯度，使用随机梯度下降法(SGD)更新参数。这里，梯度法的更新次数（循环的次数）为10000。每更新一次，都对训练数据计算损失函数的值，并把该值添加到数组中。

### 4.5.3 基于测试数据的评价

我们确认了通过反复学习可以使损失函数的值逐渐减小这一事实。不过这个损失函数的值，严格地讲是“对训练数据的某个mini-batch的损失函数”的值。训练数据的损失函数值减小，虽说是神经网络的学习正常进行的一个信号，但光看这个结果还不能说明该神经网络在其他数据集上也一定能有同等程度的表现。

神经网络的学习中，必须确认是否能够正确识别训练数据以外的其他数据，即确认是否会发生过拟合。过拟合是指，虽然训练数据中的数字图像能被正确辨别，但是不在训练数据中的数字图像却无法被识别的现象。

神经网络学习的最初目标是掌握泛化能力，因此，要评价神经网络的泛化能力，就必须使用不包含在训练数据中的数据。下面的代码在进行学习的过程中，会定期地对训练数据和测试数据记录识别精度。这里，每经过一个epoch，我们都会记录下训练数据和测试数据的识别精度。

> epoch是一个单位。一个epoch表示学习中所有训练数据均被使用过一次时的更新次数。比如，对于10000笔训练数据，用大小为100笔数据的mini-batch进行学习时，重复随机梯度下降法100次，所有的训练数据就都被“看过”了。此时，100次就是一个epoch。

为了正确进行评价，我们来稍稍修改一下前面的代码。

```py
import numpy as np
from mnist import load_mnist
from two_layer_network import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 总训练样本
train_size = x_train.shape[0]
# 批次样本数
batch_size = 100
# epoch 数
epoch_iters_numer = train_size / batch_size
# 学习率
learning_rate = 0.01
# 训练次数
train_iter_number = 10000
# 训练过程中的误差缓存
train_loss_list = []
train_acc_list = []
test_acc_list = []

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10, weight_init=0.01)

for i in range(train_iter_number):
    batch_mask = np.random.choice(train_size, batch_size)
    # 当前批次的训练数据和标记数据
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    grads = net.numerical_gradient(x_train, t_train)

    for key in ("W1", "b1", "W2", "b2"):
        net.params[key] = net.params[key] - learning_rate * grads[key]

    loss = net.loss(x_train, t_train)
    train_loss_list.append(loss)

    if i % epoch_iters_numer == 0:
        train_accuracy = net.accuracy(x_train, t_train)
        test_accuracy = net.accuracy(x_test, t_test)
        train_acc_list.append(train_accuracy)
        test_acc_list.append(test_accuracy)
        print(f"Train acc: {train_accuracy}, test acc: {test_accuracy}")
```

在上面的例子中，每经过一个epoch，就对所有的训练数据和测试数据计算识别精度，并记录结果。之所以要计算每一个epoch的识别精度，是因为如果在for语句的循环中一直计算识别精度，会花费太多时间。并且，也没有必要那么频繁地记录识别精度（只要从大方向上大致把握识别精度的推移就可以了）​。因此，我们才会每经过一个epoch就记录一次训练数据的识别精度。

通过绘制 accuracy 与 epoch 之间的关联关系图，我们发现，随着epoch的前进（学习的进行）​，我们发现使用训练数据和测试数据评价的识别精度都提高了，并且，这两个识别精度基本上没有差异（两条线基本重叠在一起）​。因此，可以说这次的学习中没有发生过拟合的现象。

## 4.6 小结

本章中，我们介绍了神经网络的学习。首先，为了能顺利进行神经网络的学习，我们导入了损失函数这个指标。以这个损失函数为基准，找出使它的值达到最小的权重参数，就是神经网络学习的目标。为了找到尽可能小的损失函数值，我们介绍了使用函数斜率的梯度法。

- 机器学习中使用的数据集分为训练数据和测试数据。
- 神经网络用训练数据进行学习，并用测试数据评价学习到的模型的泛化能力。
- 神经网络的学习以损失函数为指标，更新权重参数，以使损失函数的值减小。
- 利用某个给定的微小值的差分求导数的过程，称为数值微分。
- 利用数值微分，可以计算权重参数的梯度。
- 数值微分虽然费时间，但是实现起来很简单。下一章中要实现的稍微复杂一些的误差反向传播法可以高速地计算梯度。
