# # 绘制柱状图 Bar Chart
# import matplotlib.pyplot as plt

# categories = ['A', 'B', 'C', 'D']
# values = [3, 7, 2, 5]
# fig, ax = plt.subplots()
# ax.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
# plt.show()

# # categories = ['A', 'B', 'C', 'D']
# # values = [3, 7, 2, 5]

# # fig, ax = plt.subplots()
# # ax.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
# # plt.show()

# 柱状图家族
import matplotlib.pyplot as plt
import numpy as np

# 解决中文乱码
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']    # 用来正常显示中公文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 准备数据
categories = ['产品A', '产品B', '产品C', '产品D', '产品E']
sales_2023 = [23, 45, 56, 78, 33]
sales_2024 = [34, 56, 64, 89, 45]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. 分组柱状图
x = np.arange(len(categories))
width = 0.35

axes[0].bar(x - width / 2, sales_2023, width, label='2023', color='skyblue', alpha=0.8)
axes[0].bar(x + width / 2, sales_2024, width, label='2024', color='lightcoral', alpha=0.8)
axes[0].set_xticks(x)
axes[0].set_xticklabels(categories)
axes[0].set_title('分组柱状图')
axes[0].legend()
axes[0].set_ylabel('销量额（万元）')

# 2. 堆叠柱状图
axes[1].bar(categories, sales_2023, label='2023', color='lightblue')
axes[1].bar(categories, sales_2024, bottom=sales_2023, label='2024', color='lightcoral')
axes[1].set_title('堆叠柱状图')
axes[1].legend()

axes[2].barh(categories, sales_2024, color='lightgreen', alpha=0.7)
axes[2].set_title('水平柱状图')
axes[2].set_xlabel('销量额（万元）')

# 为每个柱子添加数值标签
for i, v in enumerate(sales_2024):
    axes[2].text(v + 1, i, str(v), va='center')
    
plt.tight_layout()
plt.show()