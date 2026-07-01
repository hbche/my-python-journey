import numpy as np
from dataset.mnist import load_mnist
from two_layer_net import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

network = TwoLayerNet(784, 50, 10)

batch_size = 100
train_size = x_train.shape[0]
learning_rate = 0.1
train_loop = 10000

train_loss_list = []
train_acc_list = []
test_acc_list = []

item_per_epoch = max(train_size / batch_size, 1)

for i in range(train_loop):
    batch_mask = np.random.choice(train_size, batch_size)
    x_train_batch = x_train[batch_mask]
    t_train_batch = t_train[batch_mask]
    # 通过反向传播求梯度
    grads = network.gradient(x_train_batch, t_train_batch)

    # 更新权重参数
    for key in ("w1", "b1", "w2", "b2"):
        network.params[key] -= grads[key] * learning_rate

    loss = network.loss(x_train_batch, t_train_batch)
    train_loss_list.append(loss)

    # 以 epoch 为单位，计算当前权重的准确率
    if i % item_per_epoch == 0:
        train_acc = network.accuracy(x_train_batch, t_train_batch)
        test_acc = network.accuracy(x_test, t_test)
        train_acc_list.append(train_acc)
        test_acc_list.append(test_acc)
        print(train_acc, test_acc)

# 0.13 0.1097
# 0.91 0.9016
# 0.93 0.9251
# 0.97 0.9341
# 0.95 0.9437
# 0.95 0.9494
# 0.98 0.952
# 0.97 0.9568
# 0.98 0.9596
# 1.0 0.9626
# 0.99 0.9629
# 0.99 0.9648
# 0.99 0.9661
# 1.0 0.9667
# 0.99 0.9678
# 1.0 0.9692
# 1.0 0.9702
