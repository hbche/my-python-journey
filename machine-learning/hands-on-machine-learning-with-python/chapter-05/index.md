# 第 5 章 有监督学习：回归

## 5.1 一维输入的直线模型

### 5.1.1 直线模型

$y=w_0x+w_1$

### 5.1.2 平方误差函数

平均方差误差（MSE）

### 5.1.3 求参数（梯度法）

$$
J=\frac{1}{N}\sum_{i=0}^{N-1}(y_n-t_n)^2
$$

$$
J=\frac{1}{N}\sum_{i=0}^{N-1}(w_0x_n + w_1 - t_n)^2
$$

分别对 $w0$ 和 $w1$ 进行求偏导：

$$
\frac{\partial{J}}{\partial{w_0}}=\frac{2}{N}\sum_{i=0}^{N-1}(w_0x_n + w_1 - t_n)x_n
$$

$$
\frac{\partial{J}}{\partial{w_1}}=\frac{2}{N}\sum_{i=0}^{N-1}(w_0x_n + w_1 - t_n)
$$

梯度算法核心代码：

```py
def calculate_gradient(x, t, w):
    """
    基于最小二乘法计算的均方误差的梯度计算:
    """
    # w0 平均方差函数的偏导
    dw0 = 2 * np.mean((x * w[0] + w[1] - t) * x)
    # w1 平均方差函数的偏导
    dw1 = 2 * np.mean(x * w[0] + w[1] - t)
    return (dw0, dw1)


def gradient_descent(x, t):
    """
    梯度下降算法
    """
    w_init = [10.0, 165.0]  # w的初始值
    min_delta_gradient = 0.1  # 当梯度绝对值达到0.01之后，停止遍历
    alpha = 0.001  # 学习率，调整
    iter_count = 10_000  # 循环遍历次数
    w_list = np.zeros((iter_count, 2))  # 初始化梯度列表
    w_list[0, :] = w_init
    for i in range(1, iter_count - 1):
        # 根据前一个w参数计算梯度
        gradient = calculate_gradient(x, t, [w_list[i - 1, 0], w_list[i - 1, 1]])
        w_list[i, 0] = w_list[i - 1, 0] - alpha * gradient[0]
        w_list[i, 1] = w_list[i - 1, 1] - alpha * gradient[1]
        # 如果梯度下降到一定坡度之后，就停止计算
        if max(np.absolute(gradient)) < min_delta_gradient:
            break
    w0 = w_list[i, 0]
    w1 = w_list[i, 1]
    w_list = w_list[:i, :]  # 将有效的w进行重新赋值，移除后续没有迭代更新的[0, 0]

    # 返回当前梯度对应的 w0、w1、当前梯度和历史w参数列表
    return w0, w1, gradient, w_list
```

### 5.1.4 直线模型参数解析解

通过令参数偏导为零，计算最小均方误差：

$$
\frac{\partial{J}}{\partial{w_0}} = 0
$$

$$
\frac{\partial{J}}{\partial{w_1}} = 0
$$

$$
\frac{2}{N}\sum_{i=0}^{N-1}(w_0x_n + w_1 - t_n)x_n=0
$$

$$
\frac{2}{N}\sum_{i=0}^{N-1}(w_0x_n + w_1 - t_n)=0
$$

利用消元法，计算$w_0$和$w_1$的值。

$$
w_0\sum_{i=0}^{N-1}(x_nx_n) + w_1\sum_{i=0}^{N-1}(x_n) - \sum_{i=0}^{N-1}(t_nx_n)=0
$$

$$
w_0\sum_{i=0}^{N-1}x_n + \sum_{i=0}^{N-1}w_1 - \sum_{i=0}^{N-1}(t_n)=0
$$

计算得，w1为：

$$
w_1 = <t> - w_0<x>
$$

$$
w_0<x^2>+<t><x> - w_0<x><x>= <tx>
$$

从而得到最终结果：

$$
w_0 = \frac{<tx> - <t><x>}{<x^2> - <x><x>}
$$

$$
w_1 = <t> - \frac{<tx> - <t><x>}{<x^2> - <x><x>}<x>
$$

以下是代码实现的解析解计算最佳参数：

```py
def analytical_solution(x, t):
    """
    计算均方误差最下值对应的解析解
    """
    x_mean = np.mean(x)
    t_mean = np.mean(t)
    tx_mean = np.mean(t * x)
    xsquare_mean = np.mean(x * x)

    w0 = (tx_mean - t_mean * x_mean) / (xsquare_mean - x_mean * x_mean)
    w1 = t_mean - w0 * x_mean
    return w0, w1
```

## 5.2 二维输入的平面模型

## 5.4 线性基底函数模型

曲线比直线对训练数据的拟合程度更好。加入我们将直线函数改为曲线函数，能提高拟合度。基底函数中的 $x$ 是一个以 $x$ 为参数的函数$f(x)$。

使用曲线拟合的模型称为线性基底函数模型。

我们先以高斯函数作为基底来探索基底函数。

绘制高斯函数的图像：

```py

```
