import numpy as np
from activation_function import identify_function, sigmoid


def init_network():
    """
    初始化神经网络的参数
    """
    network = {}
    # 第一层参数
    network["w1"] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network["b1"] = np.array([0.1, 0.2, 0.3])
    # 第二层参数
    network["w2"] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network["b2"] = np.array([0.1, 0.2])
    # 第三层参数
    network["w3"] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network["b3"] = np.array([0.1, 0.2])

    return network


def forward(network, x):
    """
    神经网络的前向计算
    """
    w1, w2, w3 = network["w1"], network["w2"], network["w3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]
    a1 = np.dot(x, w1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, w2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, w3) + b3
    y = identify_function(a3)

    return y


if __name__ == "__main__":
    x = np.array([1.0, 0.5])
    network = init_network()
    y = forward(network, x)
    print(y)
    # [0.31682708 0.69627909]
