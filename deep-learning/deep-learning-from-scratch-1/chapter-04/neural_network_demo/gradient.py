import matplotlib.pyplot as plt
import numpy as np


def numerical_diff(f, x):
    """
    利用中心差分实现函数求导
    """
    h = 1e-4
    return (f(x + h) - f(x - h)) / (2 * h)


# print(np.float32(10e-50))  # 0.0


def function_1(x):
    return 0.01 * x**2 + 0.1 * x


def plot_function_1():
    x = np.arange(0.0, 20.0, 0.1)
    y = function_1(x)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.plot(x, y)
    plt.show()


# plot_function_1()

# gradient_5 = numerical_diff(function_1, 5)
# print(gradient_5)  # 0.1999999999990898
# gradient_10 = numerical_diff(function_1, 10)
# print(gradient_10)  # 0.2999999999986347


def function_2(x):
    return x[0] ** 2 + x[1] ** 2
    # return np.sum(x**2)


# def function_tmp1(x0):
#     return x0 **2 + 4.0 ** 2.0
# print(numerical_diff(function_tmp1, 3.0))   # 6.00000000000378

# def function_tmp2(x1):
#     return 3.0 **2 + x1 ** 2.0
# print(numerical_diff(function_tmp2, 4.0))   # 7.999999999999119


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


# print(numerical_gradient(function_2, np.array([3.0, 4.0])))    # [6. 8.]
# print(numerical_gradient(function_2, np.array([0.0, 2.0])))    # [0. 4.]
# print(numerical_gradient(function_2, np.array([3.0, 0.0])))    # [6. 0.]


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


print(
    gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=0.1)
)  # [-6.11110793e-10  8.14814391e-10]

print(gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=10))
# [-2.58983747e+13 -1.29524862e+12]

print(gradient_descent(function_2, np.array([-3.0, 4.0]), learning_rate=1e-10))
# [-2.99999994  3.99999992]
