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
    def __init__(self, learning_rate=0.01, decay=0.9, eps=1e-7):
        self.learning_rate = learning_rate
        self.decay = decay
        self.eps = eps
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {key: np.zeros_like(value) for key, value in params.items()}

        for key in params.keys():
            self.h[key] = self.decay * self.h[key] + (1 - self.decay) * grads[key] ** 2

            params[key] -= (
                self.learning_rate * grads[key] / (np.sqrt(self.h[key]) + self.eps)
            )


class Adam:
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999):
        self.lr = learning_rate
        self.beta1 = beta1  # 一阶矩衰减率（动量）
        self.beta2 = beta2  # 二阶矩衰减率（自适应）
        self.iter = 0
        self.m = None  # 一阶矩（动量）
        self.v = None  # 二阶矩（自适应）

    def update(self, params, grads):
        if self.m is None:
            self.m, self.v = {}, {}
            for key in params.keys():
                self.m[key] = np.zeros_like(params[key])
                self.v[key] = np.zeros_like(params[key])
                self.iter += 1
        for key in params.keys():
            # 1. 更新一阶矩（类似Momentum）
            self.m[key] = self.beta1 * self.m[key] + (1 - self.beta1) * grads[key]
            # 2. 更新二阶矩（类似AdaGrad）
            self.v[key] = self.beta2 * self.v[key] + (1 - self.beta2) * grads[key] ** 2
            # 3. 偏差修正（初始时避免偏向0）
            m_hat = self.m[key] / (1 - self.beta1**self.iter)
            v_hat = self.v[key] / (1 - self.beta2**self.iter)
            # 4. 更新参数
            params[key] -= self.lr * m_hat / (np.sqrt(v_hat) + 1e-7)
