import numpy as np


class SGD:
    """
    随机梯度下降法
    """

    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for i in range(len(params)):
            # 根据当前梯度更新参数，缺点：对梯度变化敏感，震荡严重
            params[i] -= grads[i] * self.lr


class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        # 结合动能计算叠加上一次的梯度更新参数。缺点：还是存在震荡
        if self.v is None:
            self.v = []
            for param in params:
                self.v.append(np.zeros_like(param))
        for i in range(len(params)):
            self.v[i] = self.momentum * self.v[i] - self.lr * grads[i]
            params[i] += self.v[i]


class AdaGrad:
    def __init__(self, lr):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            # 保存历史梯度数据
            self.h = []
            for param in params:
                self.h.append(np.zeros_like(param))

        for i in range(len(params)):
            # 更新历史梯度数据
            self.h[i] += grads[i] * grads[i]
            # 根据所有历史梯度更新权重参数
            params[i] -= self.lr * (np.sqrt(self.h[i]) + 1e-7)


class RMSProp:
    def __init__(self, lr=0.01, decay_rate=0.99):
        self.lr = lr
        self.decay_rate = decay_rate
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = []
            for param in params:
                self.h.append(np.zeros_like(param))
        for i in range(len(params)):
            # 按照一定比例计算
            self.h[i] *= self.decay_rate
            self.h[i] += (1 - self.decay_rate) * grads[i] * grads[i]
            params[i] -= grads[i] * self.lr / (np.sqrt(self.h[i]) + 1e-7)


class Adam:
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.iter = 0
        self.m = None
        self.v = None

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = [], []
            for param in params:
                self.m.append(np.zeros_like(param))
                self.v.append(np.zeros_like(param))

        self.iter += 1
        lr_t = (
            self.lr
            * np.sqrt(1.0 - self.beta2**self.iter)
            / (1.0 - self.beta1**self.iter)
        )

        for i in range(len(params)):
            self.m[i] += (1 - self.beta1) * (grads[i] - self.m[i])
            self.v[i] += (1 - self.beta2) * (grads[i] ** 2 - self.v[i])

            params[i] -= lr_t * self.m[i] / (np.sqrt(self.v[i]) + 1e-7)
