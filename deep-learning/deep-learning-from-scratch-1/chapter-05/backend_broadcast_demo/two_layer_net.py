# 两层神经网络实现
from collections import OrderedDict

import numpy as np
from layer_naive import Affine, ReLU, SoftmaxWithLoss, numerical_gradient


class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重参数
        w1 = np.random.randn(input_size, hidden_size) * weight_init_std
        b1 = np.zeros(hidden_size)
        w2 = np.random.randn(hidden_size, output_size) * weight_init_std
        b2 = np.zeros(output_size)
        self.params = {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

        # 生成层
        self.layers = OrderedDict()
        self.layers["Affine1"] = Affine(self.params["w1"], self.params["b1"])
        self.layers["Relu1"] = ReLU()
        self.layers["Affine2"] = Affine(self.params["w2"], self.params["b2"])

        self.last_layer = SoftmaxWithLoss()

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
        accuracy = np.sum(y == t) / float(t.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_w = lambda W: self.loss(x, t)

        grads = {}
        grads["w1"] = numerical_gradient(loss_w, self.params["w1"])
        grads["b1"] = numerical_gradient(loss_w, self.params["b1"])
        grads["w2"] = numerical_gradient(loss_w, self.params["w2"])
        grads["b2"] = numerical_gradient(loss_w, self.params["b2"])

        return grads

    def gradient(self, x, t):
        self.loss(x, t)

        dout = 1
        dout = self.last_layer.backward(dout)

        for layer in list(self.layers.values()).reverse():
            dout = layer.backward(dout)

        grads = {}
        grads["w1"] = self.layers["Affine1"].dw
        grads["b1"] = self.layers["Affine1"].db
        grads["w2"] = self.layers["Affine2"].dw
        grads["b2"] = self.layers["Affine2"].db

        return grads
