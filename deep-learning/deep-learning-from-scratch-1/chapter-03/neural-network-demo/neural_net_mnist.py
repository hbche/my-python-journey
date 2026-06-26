import pickle
from time import time

import numpy as np
from activation_function import sigmoid, softmax
from dataset.mnist import load_mnist


def init_network():
    """
    加载参数文件，解析参数，生成默认的权重和偏置参数
    """
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    result = softmax(a3)

    return result


def get_data():
    # 第一次调用需要花费一些时间
    # 此处一定要记住，必须进行归一化处理，否则大数值会导致 np.exp 函数计算溢出。 Python 中 float64 的最大上限（约 $1.79 \times 10^{308}$），np.exp(1000)就是超过该阈值的一个例子
    (x_train, t_train), (x_test, t_test) = load_mnist(
        flatten=True, normalize=True, one_hot_label=False
    )

    return (x_train, t_train)


if __name__ == "__main__":
    network = init_network()
    x_test, t_test = get_data()

    accracy_cnt = 0
    start = time()
    for i in range(len(x_test)):
        predict_label = np.argmax(predict(network, x_test[i]))
        if predict_label == t_test[i]:
            accracy_cnt += 1
    print(f"Accracy: {float(accracy_cnt) / len(x_test)}.")
    # Accracy: 0.9357666666666666.
    end = time()
    print(f"Total time: {end - start}")
    # Total time: 1.7309372425079346

    # # 输出各个数据的形状
    # print(x_train.shape)
    # # (60000, 784)
    # print(t_train.shape)
    # # (60000,)
    # print(x_test.shape)
    # # (10000, 784)
    # print(t_test.shape)
    # # (10000,)
