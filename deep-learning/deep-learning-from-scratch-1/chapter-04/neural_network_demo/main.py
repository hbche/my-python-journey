import os
import sys

import numpy as np
from mnist import load_mnist


def mean_squared_error(y, t):
    """
    均方误差
    """
    return 0.5 * np.sum((y - t) ** 2)


# def cross_entropy_error(y, t):
#     """
#     单数数值的交叉熵误差计算，
#     y: 预测值
#     t: 监督数据，需要是one-hot编码
#     """
#     delta = 1e-7
#     return t*np.log(y + delta)


# def cross_entropy_error(y: np.array, t):
#     """
#     交叉熵误差
#     y: 预测值
#     t: 监督数据，需要是one-hot编码
#     """
#     if y.ndim == 1:
#         t = t.reshape(1, t.size)
#         y = t.reshape(1, y.size)
#     batch_size = y.shape[0]
#     delta = 1e-7
#     return -np.sum(t * np.log((y + delta))) / batch_size


def cross_entropy_error(y, t):
    """
    交叉熵误差计算：
    y: 预测值
    t: 监督数据，非 ont-hot 格式，例如 [2, 7, 0, 9]，而不是 [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], ...] 这种 one-hot 编码格式
    """
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    delta = 1e-7
    batch_size = y.shape[0]
    # 如果 t 不是 one-hot 编码格式，我们可以直接根据 t 的标签值作为索引取对应位置的预测值进行 ln() 计算即可，而不需要将 t 转换为 one-hot 编码格式
    return -np.sum(np.log(y[np.arange(batch_size, t)] + delta)) / batch_size


def get_data_set():
    sys.path.append(os.pardir)
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, one_hot_label=True
    )
    train_size = x_train.shape[0]
    batch_size = 10
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    print(x_batch.shape)  # (10, 784)
    print(t_batch.shape)  # (10, 10)


if __name__ == "__main__":
    get_data_set()
