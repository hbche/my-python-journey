import numpy as np


class Affine:
    """
    仿射层：使用线性回归计算单层神经网络的输出
    """

    def __init__(self, w, b):
        self.w = w
        self.b = b

        self.x = None  # 用于反向传播计算w的梯度
        self.dw = None
        self.db = None

    def forward(self, x):
        self.x = x
        out = np.dot(x, self.w) + self.b

        return out

    def backward(self, dout):
        self.dw = np.dot(self.x.T, dout)
        dx = np.dot(dout, self.w.T)
        self.db = np.sum(dout, axis=0)

        return dx


class ReLU:
    """
    Affine层的激活函数
    """

    def __init__(self):
        # 记录 x <= 0 的索引
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


def softmax_standard(x):
    """
    支持矩阵运算的 softmax 函数
    """
    if x.ndim == 2:
        max_x = np.max(x, axis=1, keepdims=True)
        exp_x = np.exp(x - max_x)

        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    else:
        max_x = np.max(x)
        exp_x = np.exp(x - max_x)

        return exp_x / np.sum(exp_x)


def cross_entropy_error(x, t):
    if x.ndim == 1:
        x = x.reshape([1, len(x)])
        t = t.reshape([1, len(x)])
    batch_size = t.shape[0]

    # 防止对数计算溢出，需要加 1e-6
    return -(np.sum(t * np.log(x + 1e-6))) / batch_size


class SoftmaxWithLoss:
    def __init__(self):
        # 输入经过 softmax 处理的输出
        self.y = None
        # 需要记录 标签值 t，用于反向传播法计算梯度时使用
        self.t = None
        # 使用交叉熵误差计算出来的误差
        self.loss = None

    def forward(self, x, t):
        self.y = softmax_standard(x)
        self.t = t
        self.loss = cross_entropy_error(self.y, t)

        return self.loss

    def backward(self, dout=1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size

        return dx


# 需要重新学习
class TwoLayerNetwork:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        w1 = np.random.randn(input_size, hidden_size) * weight_init_std
        b1 = np.zeros(hidden_size)
        w2 = np.random.randn(hidden_size, output_size) * weight_init_std
        b2 = np.zeros(output_size)

        self.params = {"w1": w1, "b1": b1, "w2": w2, "b2": b2}

        # 初始化层
        self.layers = [
            Affine(self.params["w1"], self.params["b1"]),
            ReLU(),
            Affine(self.params["w2"], self.params["b2"]),
        ]
        self.last_layer = SoftmaxWithLoss()

    def predict(self, x):
        # 正向传播，预测输出
        for layer in self.layers:
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        """
        通过正向传播预测输出，然后根据预测输出和标签值计算误差
        """
        out = self.predict(x)
        loss = self.last_layer.forward(out, t)

        return loss

    def accuracy(self, x, t):
        """
        计算准确率
        """
        out = self.predict(x)
        # 重点注意：需要知道如何进行数据对齐，再进行准确率计算
        out = np.argmax(out, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)

        # 重点注意：此处需要将计算结果转换成浮点数
        return np.sum(out == t) / float(t.shape[0])

    def gradient(self, x, t, dout=1):
        # 重点注意：在计算梯度之前，必须先进行正向传播，否则反向传播过程中依赖的参数无法得到初始化
        self.loss(x, t)

        # 反向传播计算梯度
        dout = 1
        dout = self.last_layer.backward(dout)
        for layer in reversed(self.layers):
            dout = layer.backward(dout)

        grads = {}
        dw1 = self.layers[0].dw
        db1 = self.layers[0].db
        dw2 = self.layers[2].dw
        db2 = self.layers[2].db
        grads["w1"] = dw1
        grads["b1"] = db1
        grads["w2"] = dw2
        grads["b2"] = db2

        return grads
