import numpy as np
from mnist import load_mnist
from two_layer_network import TwoLayerNet

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

# 总训练样本
train_size = x_train.shape[0]
# 批次样本数
batch_size = 100
# epoch 数
epoch_iters_numer = train_size / batch_size
# 学习率
learning_rate = 0.01
# 训练次数
train_iter_number = 10000
# 训练过程中的误差缓存
train_loss_list = []
train_acc_list = []
test_acc_list = []

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10, weight_init=0.01)

for i in range(train_iter_number):
    batch_mask = np.random.choice(train_size, batch_size)
    # 当前批次的训练数据和标记数据
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]
    grads = net.numerical_gradient(x_train, t_train)

    for key in ("W1", "b1", "W2", "b2"):
        net.params[key] = net.params[key] - learning_rate * grads[key]

    loss = net.loss(x_train, t_train)
    train_loss_list.append(loss)

    if i % epoch_iters_numer == 0:
        train_accuracy = net.accuracy(x_train, t_train)
        test_accuracy = net.accuracy(x_test, t_test)
        train_acc_list.append(train_accuracy)
        test_acc_list.append(test_accuracy)
        print(f"Train acc: {train_accuracy}, test acc: {test_accuracy}")
