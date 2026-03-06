import matplotlib.pyplot as plt
import numpy as np


def line(x, w):
    return x * w[0] + w[1]


def plot_data(X, T, w):
    """
    plot_data: 绘制数据分布图

    :param X: 年龄数据
    :param T: 身高数据
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_title("Height - Age")
    ax.set_xlabel("Age")
    ax.set_ylabel("Height")
    ax.set_xlim((4, 30))
    ax.plot(
        X,
        T,
        marker="o",
        linestyle="None",
        markeredgecolor="black",
        color="cornflowerblue",
    )

    ax.plot(X, np.array([line(x_i, w) for x_i in X]), color="blue")
    ax.grid(True)

    plt.show()
