import numpy as np
from mnist import load_mnist
from two_layer_network import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)
train_loss_list = []

# 超参数
iters_number = 10000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.01

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

for i in range(iters_number):
    # 获取mini-batch
    train_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[train_mask]
    t_batch = t_train[train_mask]

    # 计算梯度
    grads = net.numerical_gradient(x_batch, t_batch)
    # 更新参数
    for key in ("W1", "b1", "W2", "b2"):
        net.params[key] = net.params[key] - learning_rate * grads[key]

    # 记录学习过程
    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)

print(train_loss_list[0])
print(train_loss_list[iters_number - 1])
# plt.plot(np.arange(iter_total), loss_list)
# plt.show()
