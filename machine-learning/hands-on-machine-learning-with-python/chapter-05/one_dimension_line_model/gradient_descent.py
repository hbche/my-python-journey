import matplotlib.pyplot as plt
import numpy as np
from line_regression import mse


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


def plot_gradient(x, t):
    plt.figure(figsize=(4, 4))
    # 等高线的分辨率
    wn = 100
    # 限定参数w的范围
    w0_range = [-25, 25]
    w1_range = [120, 170]
    w0 = np.linspace(w0_range[0], w0_range[1], wn)
    w1 = np.linspace(w1_range[0], w1_range[1], wn)
    ww0, ww1 = np.meshgrid(w0, w1)
    # 初始化均方误差列表
    J = np.zeros((wn, wn))
    for i0 in range(len(w0)):
        for i1 in range(len(w1)):
            # 计算均方误差
            J[i0, i1] = mse(x, t, [w0[i0], w1[i1]])
    # 绘制梯度等高线
    cont = plt.contour(
        ww0, ww1, J, 30, colors="black", levels=(100, 1000, 10000, 100000)
    )
    cont.clabel(fmt="%1.0f", fontsize=8)
    # 计算梯度历史
    w0, w1, gradient, w_history = gradient_descent(x, t)
    print(f"重复次数：{w_history.shape[0]}")
    # 重复次数：9998
    print(f"W=[{w0}, {w1}]")
    # W=[1.496581522905986, 136.9255117819269]
    print(f"Gradient: {gradient}")
    # Gradient: (np.float64(-0.020353130126313346), np.float64(0.3512744578786453))
    print(f"MSE: {mse(x, t, [w0, w1])}")
    # MSE: 49.239532206524785
    # 绘制梯度路径
    plt.plot(
        w_history[:, 0],
        w_history[:, 1],
        ".-",
        color="gray",
        markersize=10,
        markeredgecolor="cornflowerblue",
    )
    plt.grid(True)
    plt.xlabel = "w0"
    plt.ylabel = "w1"
    plt.show()
