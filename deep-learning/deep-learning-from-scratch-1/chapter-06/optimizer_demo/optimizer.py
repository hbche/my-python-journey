import numpy as np


class SGD:
    """
    随机梯度下降法计算权重
    """

    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def update(self, params, grads):
        for key in grads.keys():
            params[key] -= self.learning_rate * grads[key]


class Momentum:
    def __init__(self, learning_rate=0.01, momentum=0.9):
        """
        在SGD的基础上增加 momentum 系数，控制加速度
        """
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, value in params.items():
                self.v[key] = np.zeros_like(value)
        for key in params.keys():
            self.v[key] = self.v[key] * self.momentum - self.learning_rate * grads[key]
            params[key] += self.v[key]


class AdaGrad:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, value in grads.items():
                self.h[key] = np.zeros_like(value)
        for key in params.keys():
            self.h[key] = self.h[key] + grads[key] * grads[key]
            params[key] -= (
                self.learning_rate * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            )


class RMSProp:
    def __init__(self, ratio=0.9, learning_rate=0.01):
        self.ratio = ratio
        self.learning_rate = learning_rate
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, value in grads.items():
                self.h[key] = np.zeros_like(value)

        for key in params.keys():
            self.h[key] = (
                self.ratio * self.h[key] + (1 - self.ratio) * grads[key] * grads[key]
            )
            params[key] -= (
                self.learning_rate * grads[key] / (np.sqrt(self.h[key]) + 1e-7)
            )
