# # 折线图 示例
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# x = np.linspace(-math.pi, math.pi, 100)
# y = np.sin(x)

# fig, ax = plt.subplots()
# # 绑定数据，并设置数据样式
# ax.plot(x, y, label="sin(x)", color="blue", linestyle="--", linewidth=2)
# ax.set_xlabel("x")  # 设置 x 轴的标题
# ax.set_ylabel("y")  # 设置 y 轴的标题
# ax.set_title("Sin Function")    # 设置图表的标题
# ax.legend()     # 展示图例

# plt.show()

# 线的魔法
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) # 0到100之间的100个点

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 基础的折线图
ax[0, 0].plot(x, np.sin(x), label='sin(x)')
ax[0, 0].set_title('Sin function')
ax[0, 0].legend()

# 带标记点的折线图
ax[0, 1].plot(x, np.cos(x),
              marker='o',   # 标记形状
              markersize=4, # 标记大小
              markevery=10, # 每10个标记一个
              linewidth=1.5,
              color='coral',
              label='cos(x)'
              )
ax[0, 1].set_title('带标记的余弦函数')
ax[0, 1].legend()

# 多条线对比
ax[1, 0].plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax[1, 0].plot(x, np.sin(2*x), label='sin(2x)', linestyle='--', linewidth=2)
ax[1, 0].plot(x, np.sin(3*x), label='sin(3x)', linestyle=':', linewidth=2)
ax[1, 0].set_title('多条线对比')
ax[1, 0].legend()

# 填充区域图
ax[1, 1].fill_between(x, np.sin(x), alpha=0.3, color='skyblue', label='sin(x) 区域')
ax[1, 1].plot(x, np.sin(x), color='blue', linewidth=2)

plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文
plt.rcParams['axes.unicode_minus'] = False

plt.tight_layout()  # 自动调整子图间距
plt.show()