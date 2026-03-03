import matplotlib.pyplot as plt
import numpy as np

# 设置随机种子，确保每次运行生成的随机数相同（便于复现结果）
np.random.seed(42)

for color in ["red", "green", "blue"]:
    n = 100
    x, y = np.random.rand(2, 100)
    scale = 500 * np.random.rand(n) ** 5
    plt.scatter(x, y, s=scale, c=color, alpha=0.3, ec="blue")

plt.grid(True)

# 显示图形
plt.show()
