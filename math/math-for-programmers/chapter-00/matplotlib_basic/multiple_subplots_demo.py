# 多子图布局示例
import matplotlib.pyplot as plt

# 声明 2 行 2 列 布局的画板
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 声明每个区域中的画布
axes[0, 0].plot([1, 2, 3], [1, 2, 3])
axes[0, 0].set_title("Top Left")

axes[0, 1].scatter([1, 2, 3], [1, 2, 3])
axes[0, 1].set_title("Top Right")

axes[1, 0].bar(['A', 'B', 'C'], [4, 2, 3])
axes[1, 0].set_title("Bottom Left")

axes[1, 1].hist([1, 2, 2, 3, 3, 3], bins=3)
axes[1, 1].set_title('Bottom Right')

plt.tight_layout()
plt.show()
