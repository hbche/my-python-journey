class MulLayer:
    """
    乘法层
    """

    def __init__(self):
        """
        因为是在forward 阶段才传入输入参数，所以构造函数中不进行暂存逻辑
        """
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x * y

    def backward(self, dout):
        dx = self.y * dout
        dy = self.x * dout
        return dx, dy


class AddLayer:
    """
    加法层
    """

    def __init__(self):
        pass

    def forward(self, x, y):
        return x + y

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy


class ReLULayer:
    """
    ReLU 层激活函数
    """

    def __init__(self):
        self.mask = None

    def forward(self, x):
        self.mask = x <= 0
        out = x.copy()
        out[self.mask] = 0

        return out

    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout

        return dx
