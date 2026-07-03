class SGD:
    """
    随机梯度下降法计算权重
    """

    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate

    def update(self, params, grads):
        for key in grads.keys():
            params[key] -= self.learning_rate * grads[key]
