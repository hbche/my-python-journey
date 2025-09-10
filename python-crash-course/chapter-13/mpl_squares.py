# # 使用Matplotlib绘制平方数据
# # 首先导入pyplot模块，并指定别名
# import matplotlib.pyplot as plt

# squares = [n ** 2 for n in range(1, 6)]

# fig, ax = plt.subplots()
# ax.plot(squares)

# plt.show()

# # 设置标题和连线粗细
# import matplotlib.pyplot as plt

# squares = [n ** 2 for n in range(1, 6)]

# fig, ax = plt.subplots()
# # 设置连线粗细
# ax.plot(squares, linewidth=3)
# # 设置标题以及标题的字体
# ax.set_title("Squares Numbers", fontsize=24)
# # 设置X轴的说明文字
# ax.set_xlabel("Value", fontsize=14)
# # 设置Y轴的说明文字
# ax.set_ylabel("Squares of Value", fontsize=14)
# # 设置刻度标记的样式
# ax.tick_params(labelsize=14)

# plt.show()

# # 校正绘图
# import matplotlib.pyplot as plt

# input_values = list(range(1, 6))
# squares = [n ** 2 for n in input_values]

# # 在一个图形中绘制一个或多个绘图，fig为图形，ax为绘图
# fix, ax = plt.subplots()
# # 绘制连线图，并设置连线宽度
# ax.plot(input_values, squares, linewidth=3)
# # 设置绘图的标题
# ax.set_title("Square Numbers", fontsize=24)
# # 设置x轴标题及字体大小
# ax.set_xlabel("Value", fontsize=14)
# # 设置y轴标题及字体大小
# ax.set_ylabel("Squares of Value", fontsize=14)
# # 设置刻度线样式，x轴和y轴的字体大小
# ax.tick_params(labelsize=14)

# # 启动图形终端展示绘图
# plt.show()

# 使用Matplotlib内置样式
import matplotlib.pyplot as plt

input_values = list(range(1, 6))
squares = [n ** 2 for n in input_values]

# 在调用subplots()之前设置内置样式
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()