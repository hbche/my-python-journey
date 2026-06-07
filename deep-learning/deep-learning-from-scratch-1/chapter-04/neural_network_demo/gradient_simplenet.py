import numpy as np

def softmax(x):
    """
    softmax 的 Docstring

    :param x: 说明
    """
    max_x = np.max(x)
    normal_x = np.exp(x - max_x + 1e-4)
    return normal_x / np.sum(normal_x)

def cross_entropy(x, t):
    if x.ndim == 1:
        x = x.reshape(1, x.size)
        t = t.reshape(1, t.size)
    batch_size = t.shape[0]
    return -np.sum(t*np.log(x + 1e-7))/batch_size

def _numerical_gradient_no_batch(f, x):
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

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = np.zeros_like(X)
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)
        return grad


class SimpleNet:

    def __init__(self):
        """
        __init__: 初始化权重参数

        :param self: 说明
        """
        self.W = np.random.randn(2, 3)  # 使用高斯分布进行初始化

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        y = self.predict(x)
        z = softmax(y)
        loss = cross_entropy(z, t)

        return loss

if __name__ == '__main__':
    net = SimpleNet()
    net.W = np.array([
        [0.47355232, 0.9977393, 0.84668094],
        [0.85557411, 0.03563661, 0.69422093]
    ])
    print(net.W)
    # [[0.47355232 0.9977393  0.84668094]
    # [0.85557411 0.03563661 0.69422093]]

    x = np.array([0.6, 0.9])
    p = net.predict(x)
    print(p)
    # [1.05414809 0.63071653 1.1328074 ]

    print(np.argmax(p))
    # 2

    t = np.array([0, 0, 1])
    loss = net.loss(x, t)
    print(loss)
    # 0.9280682857864075

    loss_w = lambda W: net.loss(x, t)
    gard = numerical_gradient(loss_w, net.W)
    print(gard)
    # [[ 0.21924757  0.14356243 -0.36281   ]
    # [ 0.32887136  0.21534364 -0.544215  ]]
