import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


def softmax(x):
    if x.ndim == 2:
        x = x - x.max(axis=1, keepdims=True)
        x = np.exp(x)
        x /= np.sum(x, axis=1, keepdims=True)
    elif x.ndim == 1:
        x = x - np.max(x)
        x = np.exp(x)
        x /= np.sum(x)

    return x


def cross_entropy_error(y, t, eps=1e-7):
    if y.ndim == 1:
        y = y.reshape(1, y.size)
        t = t.reshape(1, t.size)
    if t.size == y.size:
        t = t.argmax(axis=1)

    batch_size = y.shape[0]

    return -(np.sum(np.log(y[np.arange(batch_size), t] + eps))) / batch_size
