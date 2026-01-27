# # 绘制散点图
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.rand(50)
# y = np.random.rand(50)

# fig, ax = plt.subplots()
# ax.scatter(x, y, c='red', s=50, alpha=0.6)
# plt.show()

# 散点图的艺术
import numpy as np
import matplotlib.pyplot as plt

# 创建一些随机数据
np.random.seed(42)   # 设置随机种子，确保可重复性
x = np.random.randn(50)
y = x + np.random.randn(50) * 0.5

fig, ax = plt.subplots(figsize=(8, 6))

# 基础散点图
ax.scatter(x, y, s=50, # 点的大小
           c='royalblue',   # 颜色
           alpha=0.7,   # 透明度
           edgecolors='black',  # 边框的颜色
           linewidth=0.5    # 边框的宽度
           )

# 添加趋势线
z = np.polyfit(x, y, 1) # 线性拟合
p = np.poly1d(z)
ax.plot(x, p(x), 'r--', alpha=0.8, label='趋势线')

ax.set_title("Scatter Example", fontsize=14, fontweight='bold')
ax.set_xlabel("X axis", fontsize=12)
ax.set_ylabel("Y axis", fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)
# 设置字体，否则中文会显示乱码
plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文
# 关闭unicode减号
# 否则会报错：Glyph 8722 (\N{MINUS SIGN}) missing from font(s) SimHei.
# Glyph 8722对应字符为数学字符中的减号，matplotlib在画坐标轴负数时，用 U+2212 → SimHei 没这个字 → 警告
plt.rcParams['axes.unicode_minus'] = False    # 关键

plt.show()