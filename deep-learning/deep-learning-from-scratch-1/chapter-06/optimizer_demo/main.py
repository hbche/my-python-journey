import numpy as np
from dataset.mnist import load_mnist
from optimizer import SGD
from two_layer_net import TwoLayerNetwork

if __name__ == "__main__":
    # # 测试softmax
    # x = np.array([[1, 2, 3], [1, 1, 1]])
    # x = softmax_standard(x)
    # print(x)
    # print(np.sum(x, axis=1, keepdims=True))

    (x_train, t_train), (x_test, t_test) = load_mnist(
        normalize=True, one_hot_label=True
    )

    network = TwoLayerNetwork(28 * 28, 100, 10)
    optimizer = SGD()

    # 批处理大小
    batch_size = 100
    # 训练数据总数，用于生成随机索引
    train_size = t_train.shape[0]
    # 训练迭代次数
    train_loop = 10000
    # 每轮训练过程中，根据梯度更新参数的学习率
    learn_rate = 0.01

    # 重点注意：iter_per_epoch的含义，计算误差的轮次
    iter_per_epoch = max(train_size / batch_size, 1)

    # 重点注意：需要记录什么不清楚
    # 记录每次迭代过程中的误差结果
    train_loss_list = []
    # 保存每轮计算的准确率
    train_acc_list = []
    test_acc_list = []

    for i in range(train_loop):
        train_mask = np.random.choice(train_size, batch_size)
        x_train_batch, t_train_batch = x_train[train_mask], t_train[train_mask]

        # 通过误差反向传播法计算梯度
        grads = network.gradient(x_train_batch, t_train_batch)
        # # 根据梯度和学习率更新权重参数
        # for key in grads.keys():
        #     network.params[key] -= learn_rate * grads[key]
        optimizer.update(network.params, grads)

        # 使用新参数计算损失值
        loss = network.loss(x_train_batch, t_train_batch)
        # 保存每轮训练过程中的损失值
        train_loss_list.append(loss)

        if i % iter_per_epoch == 0:
            print(f"Loss: {loss}.")
            # 重点注意： 此处不是使用 batch 训练数据计算准确率，而是使用全量的训练数据
            train_acc = network.accuracy(x_train, t_train)
            train_acc_list.append(train_acc)
            test_acc = network.accuracy(x_test, t_test)
            test_acc_list.append(test_acc)
            print(f"Train Accuracy: {train_acc}, Test Accuracy: {test_acc}")
