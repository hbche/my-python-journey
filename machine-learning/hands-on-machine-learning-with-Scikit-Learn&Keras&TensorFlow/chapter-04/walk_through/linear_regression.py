import numpy as np
from matplotlib.axes import Axes
from sklearn.linear_model import LinearRegression


def generate_data():
    """
    generate_data: 生成数据
    """
    np.random.seed(42)
    m = 100
    X = 2 * np.random.rand(m, 1)
    # 引入噪声
    Y = 4 + 3 * X + np.random.rand(m, 1)
    return X, Y


def plot_data(ax, X, Y):
    """
    plot_data: 绘制数据

    :param ax: 说明
    :param X: 说明
    :param Y: 说明
    """
    ax.scatter(X, Y, marker="o")
    ax.grid(True)
    ax.set_xlabel("$x_1$")
    ax.set_ylabel("y")


def calc_theta(X, Y):
    """
    calc_theta: 利用 MSE 标准方程的解，直接求解最佳参数

    :param X: 特征数据
    :param Y: 目标值
    """
    return np.linalg.inv((X.T @ X)) @ X.T @ Y


def plot_regression(ax: Axes, X, W):
    """
    plot_regression: 绘制线性回归函数

    :param ax: 说明
    :type ax: Axes
    :param X: 说明
    :param W: 说明
    """
    w0 = W[0]  # 偏置项
    w1 = W[1]
    Y = w0 + w1 * X
    (line,) = ax.plot(X, Y, color="black")
    line.set_label("Predict")
    ax.legend()


def calc_theta_by_scikit(X, Y):
    """
    calc_theta_by_scikit: 利用sklearn库中的线性回归模型计算参数

    :param X: 说明
    :param Y: 说明
    """
    lin_reg = LinearRegression()
    lin_reg.fit(X, Y)
    # 返回特征权重和偏置量
    return lin_reg.intercept_, lin_reg.coef_
