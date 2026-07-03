# SGD

class SGD:

    def __init__(self, lr=0.01):
        """
        初始化 SGD 实现的优化器
        """
        self.lr = lr

    def update(self, params, grads):
        for key in params.keys():
            params[key] -= grads[key]

        return params

