# SGD 训练法缺陷

import matplotlib.pyplot as plt
import numpy as np

# 创建网格
x = np.arange(-10, 10.0, 0.1)
y = np.arange(-10, 10.0, 0.1)

X, Y = np.meshgrid(x, y)
print(X.shape)  # (100, 200)
print(Y.shape)  # (100, 200)
Z = X**2 / 20 + Y**2

# 创建三维坐标系
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")

# # 绘制曲面
# ax.plot_surface(X, Y, Z)
# 绘制网格（不填充颜色）
ax.plot_wireframe(
    X,
    Y,
    Z,
    color="black",  # 网格颜色
    linewidth=0.6,  # 网格线宽
    rstride=5,  # 行方向每隔5个点绘制一条线
    cstride=5,  # 列方向每隔5个点绘制一条线
)

# 设置坐标轴标签
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
ax.set_title(r"$f(x, y)=\frac{1}{20}x^2+y^2$")
# 设置坐标轴刻度
ax.set_xticks(np.arange(-10, 10, 5))
ax.set_yticks(np.arange(-10, 10, 5))

plt.show()
