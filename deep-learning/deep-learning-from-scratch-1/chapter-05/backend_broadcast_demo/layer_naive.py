import numpy as np


class MulLayer:
    """
    乘法层
    """

    def __init__(self):
        """
        因为是在forward 阶段才传入输入参数，所以构造函数中不进行暂存逻辑
        """
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x * y

    def backward(self, dout):
        dx = self.y * dout
        dy = self.x * dout
        return dx, dy


class AddLayer:
    """
    加法层
    """

    def __init__(self):
        pass

    def forward(self, x, y):
        return x + y

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy


class ReLU:
    """
    ReLU 层激活函数
    """

    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = x <= 0
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx


class Sigmoid:
    """
    sigmoid 激活层
    """

    def __init__(self):
        self.out = None

    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out

        return out

    def backward(self, dout):
        dx = dout * self.out * (1.0 - self.out)

        return dx


class Affine:
    """
    Affine 仿射层，计算权重参数的总和
    """

    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None
        self.dw = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.w) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx


def softmax(x):
    """
    softmax函数
    """

    max_x = np.max(x)
    normal_x = np.exp(x - max_x)

    return normal_x / np.sum(normal_x)


def cross_entropy_error(y: np.array, t):
    """
    交叉熵误差
    """
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = t.reshape(1, y.size)
    batch_size = y.shape[0]
    delta = 1e-7
    print(y)
    return -np.sum(t * np.log(y + delta)) / batch_size


class SoftmaxWithLoss:
    """
    基于交叉熵误差作为损失函数的Softmax层
    """

    def __init__(self):
        # 经过 Softmax 计算之后的结果
        self.y = None
        self.t = None
        self.loss = None

    def forward(self, x, t):
        self.y = softmax(x)
        self.t = t
        self.loss = cross_entropy_error(x, t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx


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
