import numpy as np

result = np.array([[1, 2], [3, 4]])
print(result)
# [[1 2]
#  [3 4]]
# 在上下边填1个元素，在左右边填2个元素
result = np.pad(result, pad_width=((1, 1), (2, 2)), mode="constant", constant_values=0)
print(result)
# [[0 0 0 0 0 0]
#  [0 0 1 2 0 0]
#  [0 0 3 4 0 0]
#  [0 0 0 0 0 0]]
