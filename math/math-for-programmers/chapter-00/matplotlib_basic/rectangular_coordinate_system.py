# 绘制直角坐标系
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()

ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)

# 设置坐标轴
ax.axhline(y=0, color='black', linewidth=0.8)
ax.axvline(x=0, color='black', linewidth=0.8)

# 设置坐标轴刻度，刻度单位间距为1.0
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
ax.grid(True, which='major', linestyle='-', linewidth=0.8, color='black')

# 绘制原点
plt.scatter([0], [0], marker='x')

plt.tight_layout()
plt.show()

