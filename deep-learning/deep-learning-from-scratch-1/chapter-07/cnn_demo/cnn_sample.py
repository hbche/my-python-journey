import numpy as np

x = np.random.rand(10, 1, 28, 28)
print(x.shape)
# (10, 1, 28, 28)

# 访问第一个元素
print(x[0].shape)
# (1, 28, 28)
# 访问第二个元素
print(x[1].shape)
# (1, 28, 28)

# 要访问第一个数据的第一个通道数数据
print(x[0, 0].shape)    # (28, 28)
# 或
print(x[0][0].shape)    # (28, 28)
