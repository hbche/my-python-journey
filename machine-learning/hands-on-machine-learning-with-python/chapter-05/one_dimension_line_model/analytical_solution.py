import numpy as np


def analytical_solution(x, t):
    """
    计算均方误差最下值对应的解析解
    """
    x_mean = np.mean(x)
    t_mean = np.mean(t)
    tx_mean = np.mean(t * x)
    xsquare_mean = np.mean(x * x)

    w0 = (tx_mean - t_mean * x_mean) / (xsquare_mean - x_mean * x_mean)
    w1 = t_mean - w0 * x_mean
    return w0, w1
