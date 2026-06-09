import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
from mnist import load_mnist
from two_layer_network import TwoLayerNet

dataset_dir = os.path.dirname(os.path.abspath(__file__))
weight_file = dataset_dir + "/two_layer_weight.pkl"


def train_model():
    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, one_hot_label=True
    )

    train_loss_list = []

    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.01

    net = TwoLayerNet(784, 100, 10)

    print("Training...")
    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        # 计算梯度
        grad = net.numerical_gradient(x_batch, t_batch)
        for key in ("W1", "b1", "W2", "b2"):
            net.params[key] -= learning_rate * grad[key]

        # 记录学习过程
        loss = net.loss(x_batch, t_batch)
        train_loss_list.append(loss)

    print(train_loss_list[0])
    print(train_loss_list[iters_num - 1])
    print("Training Done!")
    save_weight(net.params)

    plt.plot(np.arange(iters_num), np.random.randn(train_loss_list))
    plt.show()

    return net.params


def load_weight():
    with open(weight_file, "rb") as f:
        dataset = pickle.load(f)
        return dataset


def save_weight(weight_info):
    print("Creating pickle file ...")
    with open(weight_file, "wb") as f:
        pickle.dump(weight_info, f, -1)
    print("Done!")


def get_weight():
    if not os.path.exists(weight_file):
        params = load_weight()
        return params
    else:
        params = train_model()
        save_weight(params)
        return params


if __name__ == "__main__":
    train_model()
