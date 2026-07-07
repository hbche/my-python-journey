from collections import OrderedDict

import numpy as np


class Sigmoid:
    def __init__(self):
        self.out = None

    def forward(self, x):
        self.out = 1 / (1 + np.exp(-x))

        return self.out

    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out

        return dx


class ReLu:
    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = x <= 0
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dx = dout.copy()
        dx[self.mask] = 0

        return dx


class Affine:
    def __init__(self, w, b):
        self.w = w
        self.b = b
        self.x = None

        # 用于后续进行参数更新时使用，w = w - dw，b = b - db
        self.dw = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(self.x, self.w) + self.b

        return out

    def backward(self, dout):
        dx = np.dot(dout, self.w.T)
        self.dw = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)

        return dx


def softmax(x):
    if x.ndim == 1:
        x = x.reshape(1, len(x))
    max_x = np.max(x, axis=1, keepdims=True)
    normal_x = x - max_x
    exp_x = np.exp(normal_x)

    return exp_x / np.sum(exp_x, axis=1, keepdims=True)


def cross_entropy_error(x, t):
    if x.ndim == 1:
        x = x.reshape(1, len(x))
        t = t.reshape(1, len(t))
    batch_size = t.shape[0]

    return -np.sum(t * np.log(x + 1e-7)) / batch_size


class SoftmaxWithLoss:
    def __init__(self):
        self.y = None
        self.t = None
        self.loss = None

    def forward(self, x, t):
        self.y = softmax(x)
        self.t = t
        self.loss = cross_entropy_error(self.y, t)

        return self.loss

    def backward(self, dout):
        batch_size = self.t.shape[0]
        return (self.y - self.t) / batch_size


class MultiLayerNet:
    def __init__(
        self,
        input_size,
        hidden_size_list,
        output_size,
        activation="relu",
        weight_init_std="relu",
        weight_decay_lambda=0,
    ):
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size_list = hidden_size_list
        self.hidden_layer_num = len(hidden_size_list)
        self.weight_decay_lambda = weight_decay_lambda
        self.params = {}

        # 初始化参数
        self.__init_weight(weight_init_std)

        # 激活函数
        activation_layer = {"sigmoid": Sigmoid, "relu": ReLu}
        self.layers = OrderedDict()
        for idx in range(1, self.hidden_layer_num + 1):
            self.layers["Affine" + str(idx)] = Affine(
                self.params["W" + str(idx)], self.params["b" + str(idx)]
            )
            self.layers["Activation_function" + str(idx)] = activation_layer[
                activation
            ]()
        idx = self.hidden_layer_num + 1
        self.layers["Affine" + str(idx)] = Affine(
            self.params["W" + str(idx)], self.params["b" + str(idx)]
        )

        self.last_layer = SoftmaxWithLoss()

    def __init_weight(self, weight_init_std):
        """
        初始化权重参数
        """
        all_size_list = [self.input_size] + self.hidden_size_list + [self.output_size]
        for idx in range(1, len(all_size_list)):
            scale = weight_init_std
            if str(weight_init_std).lower() in ("relu", "he"):
                scale = np.sqrt(2.0 / all_size_list[idx - 1])
            elif str(weight_init_std).lower() in ("sigmoid", "xavier"):
                scale = np.sqrt(1.0 / all_size_list[idx - 1])

            self.params["W" + str(idx)] = scale * np.random.randn(
                all_size_list[idx - 1], all_size_list[idx]
            )
            self.params["b" + str(idx)] = np.zeros(all_size_list[idx])

    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])

        return accuracy

    def gradient(self, x, t):
        # forward
        loss = self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)
        for layer in reversed(self.layers.values()):
            dout = layer.backward(dout)

        grads = {}
        for idx in range(1, self.hidden_layer_num + 2):
            grads["W" + str(idx)] = self.layers["Affine" + str(idx)].dw
            grads["b" + str(idx)] = self.layers["Affine" + str(idx)].db

        return grads, loss
