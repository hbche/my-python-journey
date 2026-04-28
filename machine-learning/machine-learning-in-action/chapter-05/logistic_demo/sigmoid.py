import math


def sigmoid(x):
    """sigmoid函数"""
    return 1.0 / (1 + (math.e) ** (-x))


def plot_sigmoid(range):
    """
    使用指定范围绘制sigmoid图像
    """

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(range[0], range[1], 0.1)
    y = sigmoid(x)

    plt.plot(x, y)
    plt.title("Sigmoid Function")
    plt.xlabel("x")
    plt.ylabel("sigmoid(x)")
    plt.grid()
    plt.show()
