import numpy as np

g = np.arange(24)
print(g)
g1 = np.reshape(g, (4, 6))
print(g1)
print(g1.shape) # (4, 6)
g2 = np.ravel(g1)
print(g2)
print(g2.shape) # (24,)