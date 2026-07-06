# 使用等高线研究SGD的缺陷
import matplotlib.pyplot as plt
import numpy as np

# 创建网格数据
x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

Z = X**2 / 20 + Y**2

plt.figure(figsize=(7, 6))
# 绘制等高线
contour = plt.contour(X, Y, Z, levels=20, cmap="viridis")

# 添加数值标签
plt.clabel(contour, inline=True, fontsize=8)

plt.xlabel("x")
plt.ylabel("y")
plt.title(r"$f(x, y)=\frac{1}{20}x^2+y^2$")

plt.axis("equal")

plt.show()
