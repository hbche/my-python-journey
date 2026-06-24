from dataset.mnist import load_mnist

# 第一次调用需要花费一些时间
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各个数据的形状
print(x_train.shape)
# (60000, 784)
print(t_train.shape)
# (60000,)
print(x_test.shape)
# (10000, 784)
print(t_test.shape)
# (10000,)
