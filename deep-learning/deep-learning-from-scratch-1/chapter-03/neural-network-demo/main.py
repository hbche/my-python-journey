import numpy as np

def init_network():
    """
    init_network 的 初始化权重和偏置
    """
    network = {}
    network['W1'] = np.array([
        [0.1, 0.3, 0.5],
        [0.2, 0.4, 0.6]
    ])
    network['B1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([
        [0.1, 0.4],
        [0.2, 0.5],
        [0.3, 0.6]
    ])
    network['B2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([
        [0.1, 0.3],
        [0.2, 0.4]
    ])
    network['B3'] = np.array([0.1, 0.2])
    return network


def sigmoid(x):
    """
    sigmoid 的 激活函数
    
    :param x: np.array 数组
    """
    return 1/(1 + np.exp(-x))


def identity_function(x):
    """
    identity_function 的 恒等式
    
    :param x: 说明
    """
    return x

def forward(network, x):
    """
    forward 的 前向传播
    
    :param network: 说明
    :param x: 说明
    """
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    B1, B2, B3 = network['B1'], network['B2'], network['B3']
    a1 = np.dot(x, W1) + B1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + B2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + B3
    y = identity_function(a3)
    return y

if __name__ == '__main__':
    network = init_network()
    x = np.array([1.0, 0.5])
    y = forward(network, x)
    print(y)    # [0.31682708 0.69627909]