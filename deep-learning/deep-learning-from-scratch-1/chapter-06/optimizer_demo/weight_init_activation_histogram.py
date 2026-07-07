import matplotlib.pyplot as plt
import numpy as np

# 探索 权重初始值 与激活函数的输出值的分布关系


def relu(x):
    return np.maximum(0, x)


x = np.random.randn(1000, 100)
node_num = 100
hidden_layer_size = 5

scales = {
    "std=0.01": lambda: 0.01,
    "Xavier": lambda: np.sqrt(1.0 / node_num),
    "He": lambda: np.sqrt(2.0 / node_num),
}

plt.figure(figsize=(9, 6))
for row, (name, scale_func) in enumerate(scales.items()):
    layer_input = x
    for col in range(hidden_layer_size):
        w = np.random.randn(node_num, node_num) * scale_func()
        z = np.dot(layer_input, w)
        a = relu(z)
        ax = plt.subplot(
            len(scales), hidden_layer_size, row * hidden_layer_size + col + 1
        )
        ax.hist(a.flatten(), bins=30, range=(0, 1.5))
        ax.set_title(f"{col + 1}-layer" if row == 0 else "")
        # 动态设置 y 轴刻度
        y_lim = ax.get_ylim()
        step = 10000
        y_ticks = np.arange(0, y_lim[1] + step, step)
        ax.set_yticks(y_ticks)
        layer_input = a
        ax.set_ylabel(name)  # 在每行最左侧加标签（可通过 subplot 定位，这里简单演示）

plt.tight_layout()
plt.show()
