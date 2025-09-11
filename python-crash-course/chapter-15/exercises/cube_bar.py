# 练习15.1：立方　数的三次方称为立方。请先绘图显示前5个正整数的立方值，再绘图显示前5000个正整数的立方值。

import matplotlib.pyplot as plt

# 生成1~5之间的整数列表
numbers = list(range(1, 6))
# 生成1~5之间整数的立方列表
cube_numbers = [n ** 3 for n in numbers]
# 根据 x 的值生成立柱的颜色
colors = [(0.9, 0, 0), (0, 0.9, 0), (0, 0, 0.9)]
bar_colors = [colors[i % 3] for i in range(len(numbers))]

fix, ax = plt.subplots()
# 绘制 数值->立方 的直方图，并指定颜色
ax.bar(numbers, cube_numbers, color=bar_colors)

# 设置标题及字体大小
ax.set_title("Cube Numbers", fontsize=24)
# 设置X轴副标题及字体大小
ax.set_xlabel("Number", fontsize=14)
# 设置Y轴副标题及字体大小
ax.set_ylabel("Cube of Number", fontsize=14)

plt.show()

# 练习15.2：彩色立方　给前面绘制的立方图指定颜色映射。