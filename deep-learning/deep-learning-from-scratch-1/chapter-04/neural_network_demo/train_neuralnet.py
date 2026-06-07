from mnist import load_mnist
from two_layer_network import TwoLayerNet
import numpy as np
import matplotlib.pyplot as plt


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

iters_num = 10000
train_size =x_train.shape[0]
batch_size = 100
learning_rate = 0.01

net = TwoLayerNet(784, 100, 10)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    # 计算梯度
    grad = net.numerical_gradient(x_batch, t_batch)
    for key in ('W1', 'b1', 'W2', 'b2'):
        net.params[key] -= learning_rate * grad[key]

    # 记录学习过程
    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)

plt.plot(np.arange(iters_num), train_loss_list)
plt.show()
