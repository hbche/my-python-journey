import numpy as np
from functions import cross_entropy_error, softmax


class MatMul:
    def __init__(self, W):
        self.params = [W]
        self.grads = []

    def forward(self, x):
        [W] = self.params
        self.x = x
        out = np.dot(x, W)

        return out

    def backward(self, dout):
        [W] = self.params
        dx = np.dot(dout, W.T)
        dw = np.dot(self.x.T, dout)
        self.grads[0][...] = dw

        return dx


class SoftmaxWithLoss:
    def __init__(self):
        self.params, self.grads = [], []
        self.y = None
        self.t = None

    def forward(self, x, t):
        self.y = softmax(x)
        self.t = t

        if self.t.size == self.y.size:
            self.t = self.t.argmax(axis=1)

        loss = cross_entropy_error(self.y, t)

        return loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]

        dx = self.y.copy()
        dx[np.range(batch_size, self.t)] -= 1
        dx *= dout
        dx = dx / batch_size

        return dx
