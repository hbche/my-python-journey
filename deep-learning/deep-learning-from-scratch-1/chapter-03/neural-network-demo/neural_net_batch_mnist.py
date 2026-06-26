# 批处理实现高效计算
import pickle
import time

import numpy as np
from dataset.mnist import load_mnist


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    max_x = np.max(x)
    # 防止溢出，将所有数据进行正则化处理，都减去一个最大值
    normal_x = np.exp(x - max_x)
    return normal_x / np.sum(normal_x)


def load_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, flatten=True, one_hot_label=False
    )
    return x_test, t_test


def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network


def predict(network, x):
    """
    根据给定权重参数，识别数据x
    """
    W1, W2, W3 = network["W1"], network["W2"], network["W3"]
    b1, b2, b3 = network["b1"], network["b2"], network["b3"]

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3

    result = softmax(a3)
    return result


# 批量数据大小
batch_size = 200
# 识别正确计数
accuracy_count = 0

if __name__ == "__main__":
    x_test, t_test = load_data()
    network = init_network()
    start = time.time()
    for i in range(0, len(x_test), batch_size):
        batch_test = x_test[i : i + batch_size]
        batch_predict = predict(network, batch_test)
        # 计算每个数据中概率最大的数据的索引作为最终处理结果，将二维数组转换为一维数组
        preduct_result = np.argmax(batch_predict, axis=1)
        accuracy_count += np.sum(t_test[i : i + batch_size] == preduct_result)
    print(f"Accuracy {float(accuracy_count) / len(x_test)}")
    end = time.time()
    # Accuracy 0.9352
    print(f"Total time: {end - start}")
    # Total time: 0.019620418548583984
