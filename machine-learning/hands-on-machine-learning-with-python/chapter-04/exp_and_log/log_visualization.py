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
