# 第 4 章 机器学习中的数学

## 4.7 指数函数和对数函数

### 4.7.1 指数

指数函数的定义：

$$
y=a^x
$$

我们称之为以a为底数的指数函数。

当 $a > 0$，$n$为正整数时: $a^0=1$、$a^{-n}=\frac{1}{a^n}$、$a^{\frac{1}{n}}=\sqrt[n]{a}$。

当 $a>0$，$b>0$，m、n为实数时，常见的指数运算：${a^n}\times{a^m}=a^{n+m}$、$\frac{a^n}{a^m}=a^{n-m}$、$(a^n)^m=a^{n\times{m}}$、$(ab)^n=a^nb^n$

以下是指数函数的函数图形：

``` py
import matplotlib.pyplot as plt
import numpy as np


def exp_visualization(a, **kwargs):
    X = np.linspace(-4, 4, 100)
    Y = a**X
    plt.plot(X, Y, **kwargs)


plt.figure(figsize=(5, 5))
exp_visualization(2, c="black", linewidth=3, label="$y=2^x$")
exp_visualization(3, c="cornflowerblue", linewidth=3, label="$y=3^x$")
exp_visualization(0.5, c="gray", linewidth=3, label="$y=0.5^x$")
plt.grid(True)
plt.xlim(-4, 4)
plt.ylim(-2, 6)
plt.legend(loc="lower right")
plt.show()
```
我们发现：

1. 以a为底数的指数函数为$y=a^x$，当a>1时，指数函数是一个“x增大，则y必然增大”的单调递增函数；当$0<a<1$时，则为单调递减函数，底数a越大，图形越陡。

2. 图形总是在0的上方，因此指数函数是一个无论x是整数还是负数，结果为整数的函数。

### 4.7.2 对数

把指数函数的输入和输出反过来就是对数函数。对数函数的形式如下：

$x=a^y$，转换成标准函数形式为$y=\log_a{x}$。也就是说对数函数是指数函数的反函数。

对数的定义：

当a为不等于1的正实数是，令$x=a^y$，得到$y=\log_a{x}$。特殊情况，$\log_a{a}=1$、$\log_a{1}=0$。

对数的公式：

当a、b为不等于1的正实数时：$\log_a{xy}=\log_a{x}+\log_a{y}$、$\log_a{\frac{x}{y}}=\log_a{x}-\log_x{y}$、$\log_a{x^y}=y\log_a{x}$、$\log_a{x}=\frac{\log_b{x}}{\log_b{a}}$

以下是我们绘制底数相同情况下，指数函数和对数函数的图形。

``` py
import matplotlib.pyplot as plt
import numpy as np


def exp_visualization(a, **kwargs):
    """
    绘制指数函数图形
    """
    X = np.linspace(-8, 8, 100)
    Y = a**X
    plt.plot(X, Y, **kwargs)


def log_visualization(a, **kwargs):
    """
    绘制对数函数图形
    """
    X = np.linspace(0.001, 8, 100)
    Y = np.log(X) / np.log(a)  # 由对数的除法运算可只，此函数表示以a为底x的对数运算

    plt.plot(X, Y, **kwargs)


plt.figure(figsize=(5, 5))
exp_visualization(2, c="black", linewidth=3, label="$y=2^x$")
exp_visualization(
    0.5, c="cornflowerblue", linewidth=3, linestyle="--", label="$y=0.5^x$"
)
log_visualization(2, c="black", linewidth=3, label="$y=log_2{x}$")
log_visualization(
    0.5, c="cornflowerblue", linewidth=3, linestyle="--", label="$y=log_0.5{x}$"
)
X = np.linspace(-8, 8, 100)
# 绘制分割线
plt.plot(X, X, c="black", linestyle="--")
plt.grid(True)
plt.xlim(-8, 8)
plt.ylim(-8, 8)
plt.legend(loc="lower right")
plt.show()
```
我们发现：
1. 底数相同情况下，指数函数和对数函数的图形呈$y=x$对称。
2. 以a为底数的对数函数为$y=a^x$，当a>1时，对数函数是一个“x增大，则y必然增大”的单调递增函数；当$0<a<1$时，则为单调递减函数，底数a越大，图形越陡。

对数函数可以把过大或过小的数值转换为便于处理的大小。比如，$100 000 000 = 10^8$可以表示为$a=10$的对数，即$\log_{10}{10^8}=8$，$0.000 000 001=10^{-8}$可以表示为$\log_{10}{10^{-8}}=-8$。