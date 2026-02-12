import math

import matplotlib.pyplot as plt
import numpy as np

test_data = [
    (-1.0, -2.0137862606487387),
    (-0.9, -1.7730222478628337),
    (-0.8, -1.5510125944820812),
    (-0.7, -1.6071832453434687),
    (-0.6, -0.7530149734137868),
    (-0.5, -1.4185018340443283),
    (-0.4, -0.6055579756271128),
    (-0.3, -1.0067254915961406),
    (-0.2, -0.4382360549665138),
    (-0.1, -0.17621952751051906),
    (0.0, -0.12218090884626329),
    (0.1, 0.07428573423209717),
    (0.2, 0.4268795998864943),
    (0.3, 0.7254661223608084),
    (0.4, 0.04798697977420063),
    (0.5, 1.1578103735448106),
    (0.6, 1.5684111061340824),
    (0.7, 1.157745051031345),
    (0.8, 2.1744401978240675),
    (0.9, 1.6380001974121732),
    (1.0, 2.538951262545233),
]


def linear_1(x):
    """
    拟合函数
    """
    return 2 * x


def linear_2(x):
    return 1 - x


def plot_distance(f, data):
    """
    绘制拟合函数到实际数据的距离
    """
    for x, y in data:
        plt.plot([x, x], [y, f(x)], c="r")


def plot_test_data(f, data):
    """
    绘制测试数据与拟合函数
    """
    x_min_limit = min((x for (x, _) in data))
    x_max_limit = max((x for (x, _) in data))
    x_data = np.linspace(x_min_limit, x_max_limit, 100)
    plt.plot(x_data, [f(i) for i in x_data], c="k")
    plt.scatter([x for x, _ in data], [y for _, y in data], marker="o")
    plot_distance(f, data)


# 绘制拟合线与原始数据
# plot_test_data(linear_2, test_data)


# 寻找最佳拟合函数
def secant_slope(f, xmin, xmax):
    """
    计算在xmin和xmax之间的割线f(x)的斜率
    """
    return (f(xmax) - f(xmin)) / (xmax - xmin)


def approx_derivative(f, x, dx=1e-6):
    """
    计算[x-10**(-6), x+10**(-6)]近似导数
    """
    return secant_slope(f, x - dx, x + dx)


def approx_gradient(f, x0, y0, dx=1e-6):
    """
    梯度计算
    """
    # 计算y=y0对应的x的偏导数
    partial_x = approx_derivative(lambda x: f(x, y0), x0, dx=dx)
    # 计算x=x0对应的y的偏导数
    partial_y = approx_derivative(lambda y: f(x0, y), y0, dx=dx)

    # 返回梯度
    return (partial_x, partial_y)


def length(vector):
    x, y = vector
    return math.sqrt(x**2 + y**2)


def gradient_ascent(f, xstart, ystart, tolerance=1e-6):
    """
    实现梯度上升算法：
    """
    # x，x 的初始值作为梯度计算的起点，告诉我们如何从当前点处上坡
    x = xstart
    y = ystart
    grad = approx_gradient(f, x, y)
    # 仅当梯度大于容忍值时，才前进至新点
    while length(grad) > tolerance:
        x += grad[0]
        y += grad[1]
        grad = approx_gradient(f, x, y)
    # 当无上坡路可走时，返回x和y
    return x, y


def sum_quare_error(f, data):
    """
    根据拟合函数计算代价
    """

    def quare_error(f, x, y):
        return (f(x) - y) ** 2

    return sum(quare_error(f, x, y) for x, y in data)


# 假设拟合函数为 y = a*x + b
def get_sum_cost(a, b):
    def get_cost(x):
        return a * x + b

    sum_cost = sum_quare_error(get_cost, test_data)
    return sum_cost


def get_neartest_args(xrange, yrange):
    a_data = np.linspace(0, xrange, 1000)
    b_data = np.linspace(0, yrange, 1000)
    min_a, min_b = a_data[0], b_data[0]
    min_cost = get_sum_cost(min_a, min_b)
    data = []
    for b in b_data:
        row = []
        for a in a_data:
            current_cost = get_sum_cost(a, b)
            if current_cost < min_cost:
                min_a = a
                min_b = b
                min_cost = current_cost
            row.append((current_cost))
        data.append(row)

    return min_a, min_b, min_cost, data


min_a, min_b, min_cost, data = get_neartest_args(10, 10)
print(f"min_a: {min_a}, min_b: {min_b}, min_cost: {min_cost}")


# def cal_args_cost():
#     a_data = np.linspace(0, 4, 100)
#     b_data = np.linspace(0, 4, 100)
#     data = []
#     for b in b_data:
#         row = []
#         for a in a_data:
#             row.append((get_sum_cost(a, b)))
#         data.append(row)
#     fig, ax = plt.subplots()
#     ax.imshow(data, cmap="viridis")


# cal_args_cost()

plt.show()
