import matplotlib.pyplot as plt
import numpy as np
import math
# from car_data import priuses

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


def length(vector):
    x, y = vector
    return math.sqrt(x**2 + y**2)

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

def gradient_descent(f, xstart, ystart, tolerance=1e-6):
    """
    gradient_ascent: 梯度下降
    """
    x = xstart
    y = ystart
    grad = approx_gradient(f, x, y)
    while length(grad) > tolerance:
        x -= 0.01 * grad[0]
        y -= 0.01 * grad[1]
        grad = approx_gradient(f, x, y)
    return x, y


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

def sum_squared_error(f, data):
    """
    sum_squared_error: 计算代价值
    
    :param f: 拟合函数
    :param data: 训练数据
    """
    return sum((f(x)-y) ** 2 for x, y in data)

# 假设拟合函数为 y = a*x + b
def test_data_linear_cost(a, b):
    """
    coefficient_cost: 计算系数对应线性拟合函数的代价值
    
    :param a: 斜率系数
    :param b: 截距系数
    """
    def p(x):
        return a * x + b

    return sum_squared_error(p, test_data)


def scalar_field_heatmap(f, xmin, xmax, ymin, ymax, xsteps=100, ysteps=100):
    """
    plot_field_heatmap: 热力图
    
    :param f: 说明
    :param xmin: 说明
    :param xmax: 说明
    :param ymin: 说明
    :param ymax: 说明
    :param steps: 说明
    :param ysteps: 说明
    """
    fig, ax = plt.subplots()
    # fig = plt.figure()
    fig.set_size_inches(7, 7)
    fv = np.vectorize(f)
    X = np.linspace(xmin, xmax, xsteps)
    Y = np.linspace(ymin, ymax, ysteps)
    X, Y = np.meshgrid(X, Y)
    z = fv(X, Y)
    c = ax.pcolormesh(X, Y, z, cmap='plasma')
    ax.axis([X.min(), X.max(), Y.min(), Y.max()])
    fig.colorbar(c, ax=ax)
    plt.show()

# 绘制系数的热力图，查看代价最低区域
scalar_field_heatmap(test_data_linear_cost, 0, 4, -2, 2)
# 利用梯度下降计算最优系数
a, b = gradient_descent(test_data_linear_cost,0, 20000)
# 根据最优系数计算最小代价
min_cost = test_data_linear_cost(a, b)

print(f"min_a: {a}, min_b: {b}, min_cost: {min_cost}")
#  min_a: 2.103718206153014, min_b: 0.002120738585544603, min_cost: 2.0222480750049545
