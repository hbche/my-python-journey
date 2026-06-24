import matplotlib.pyplot as plt
import numpy as np

# 激活函数

# # 阶跃函数
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0


def step_funciton(x: np.array):
    """
    阶跃函数
    """
    # 将数值型数组转换成 True / False 的数组
    y = x > 0
    # 再将布尔值类型的数值转换成0\1数组
    return y.astype(np.int32)


def plot_step_function(x: np.array):
    y = step_funciton(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.title("Step Funciton")
    plt.show()


def sigmoid(x: np.array):
    """
    sigmoid 激活函数
    """
    return 1 / (1 + np.exp(-x))


def plot_sigmoid(x):
    y = sigmoid(x)
    plt.plot(x, y)
    plt.title("Sigmoid Funciton")
    plt.ylim(0, 1.0)
    plt.show()


def ReLU(x: np.array):
    """
    ReLU 激活函数
    """
    y = x.copy()
    mask = y <= 0
    y[mask] = 0
    return y


def plot_relu(x: np.array):
    y = ReLU(x)
    plt.title("ReLU Function")
    plt.plot(x, y)
    plt.show()

def identify_function(x: np.array):
    return x
