import numpy as np


def gauss(x, mu, sigma):
    """
    高斯函数
    """
    return np.exp(-((x - mu) ** 2 / (2 * sigma**2)))
