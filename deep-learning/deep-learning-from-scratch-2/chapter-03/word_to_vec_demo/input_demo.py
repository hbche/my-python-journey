import sys

sys.path.append("../..")
import numpy as np
from common.layer import MatMul

c = np.array([[1, 0, 0, 0, 0, 0, 0]])
W = np.random.randn(7, 3)
layer = MatMul(W)
h = layer.forward(c)
print(h)    # [[ 1.35718901 -1.00301849 -1.05657724]]
