import sys

sys.path.append("../..")
import numpy as np
from common.layer import MatMul

# 样本的上下文
c0 = np.array([[1, 0, 0, 0, 0, 0, 0]])  # you
c1 = np.array([[0, 0, 1, 0, 0, 0, 0]])  # goodbye

# 生成权重初始值
W_in = np.random.randn(7, 3)
W_out = np.random.randn(3, 7)

# 生成层
in_layer0 = MatMul(W_in)
in_layer1 = MatMul(W_in)
out_layer = MatMul(W_out)

# 正向传播
h0 = in_layer0.forward(c0)
h1 = in_layer1.forward(c1)
h = 0.5 * (h0 + h1)
s = out_layer.forward(h)  # 计算得分

print(s)
# [[-1.01633624 -0.08948416  0.33510525  0.47603671  1.065994   -0.40313444
#    0.09719371]]
