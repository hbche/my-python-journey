import matplotlib.pyplot as plt
import numpy as np

# 将起点改为 0.1（严格大于 0）
x = np.arange(0.1, 5, 0.1)
y = np.log(x)

plt.plot(x, y)
plt.title("y = ln(x)")
plt.grid(True)
plt.show()
