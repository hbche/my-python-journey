# # 绘制单个点
# import matplotlib.pyplot as plt

# plt.style.use("seaborn-v0_8")
# fig, ax = plt.subplots()
# # 使用 scatter() 方法绘制单个点，传入x,y坐标，同时可使用可选的参数s设置点的尺寸
# ax.scatter(2, 4, s=200)
# # 设置样式
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# ax.tick_params(labelsize=14)

# plt.show()

# 使用scotter()绘制多个点
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [n **2 for n in x_values]

# 使用内置样式作为默认样式
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# # 绘制散点并指定点的颜色和尺寸
# ax.scatter(x_values, y_values, color='red', s=10)
# # 使用 rbg 格式的颜色值
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)
# 使用颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 设置样式
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)
# 设置每个坐标的取值范围
ax.axis([0, 1100, 0, 1_100_000])
# 由于默认情况下matplotlib在数值比较大时采用科学计数法，我们可以修改这个默认行为，使其展示原始数值，即使数值较大
ax.ticklabel_format(style='plain')

# # 展示绘图
# plt.show()
# 保存绘图
plt.savefig('squares_plot.png', bbox_inches="tight")