import matplotlib.pyplot as plt
import numpy as np
from dataset.mnist import load_mnist
from multi_layer_net import MultiLayerNet
from optimizer import SGD, AdaGrad, Adam, Momentum, RMSProp


def smooth_curve(x):
    """用于平滑损失函数的图像。

    参考：http://glowingpython.blogspot.jp/2012/02/convolution-with-numpy.html
    """
    window_len = 11
    s = np.r_[x[window_len - 1 : 0 : -1], x, x[-1:-window_len:-1]]
    w = np.kaiser(window_len, 2)
    y = np.convolve(w / w.sum(), s, mode="valid")
    return y[5 : len(y) - 5]


if __name__ == "__main__":
    (t_train, t_test), (x_train, x_test) = load_mnist(
        normalize=True, one_hot_label=True
    )
    train_size = t_train.shape[0]
    batch_size = 128
    max_iterations = 2000

    optimizers = {}
    optimizers["SGD"] = SGD()
    optimizers["Momentum"] = Momentum()
    optimizers["AdaGrad"] = AdaGrad()
    optimizers["RMSProp"] = RMSProp()
    optimizers["Adam"] = Adam()

    networks = {}
    train_loss = {}
    for key in optimizers.keys():
        networks[key] = MultiLayerNet(
            input_size=784, hidden_size_list=[100, 100, 100, 100], output_size=10
        )
        train_loss[key] = []

    for i in range(max_iterations):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch, t_batch = t_train[batch_mask], t_test[batch_mask]

        for key in optimizers.keys():
            grads, loss = networks[key].gradient(x_batch, t_batch)
            optimizers[key].update(networks[key].params, grads)
            # loss = networks[key].loss(x_batch, t_batch)
            train_loss[key].append(loss)

        if i % 100 == 0:
            print("===========" + "iteration:" + str(i) + "===========")
            for key in optimizers.keys():
                loss = networks[key].loss(x_batch, t_batch)
                print(key + ":" + str(loss))

    markers = {"SGD": "o", "Momentum": "x", "AdaGrad": "s", "RMSProp": "*", "Adam": "D"}
    x = np.arange(max_iterations)
    for key in optimizers.keys():
        plt.plot(
            x,
            smooth_curve(train_loss[key]),
            marker=markers[key],
            markevery=100,
            label=key,
        )
    plt.xlabel("iterations")
    plt.ylabel("loss")
    plt.ylim(0, 1)
    plt.legend()
    plt.show()
