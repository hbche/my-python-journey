# # 绘制直方图 Histogram
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.randn(1000)
# fig, ax = plt.subplots()
# ax.hist(data, bins=30, edgecolor="black", alpha=0.7)
# plt.show()

# 直方图与箱线图
import matplotlib.pyplot as plt
import numpy as np

# 生成一些正态分布数据
np.random.seed(42)
data1 = np.random.normal(0, 1, 1000)    # 均值0，标准差1
data2 = np.random.normal(3, 1.5, 800)   # 均值3，标准值1.5

# 设置参数
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. 直方图
axes[0].hist(data1, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
axes[0].set_title('直方图 - 单分布')
axes[0].set_xlabel('值')
axes[0].set_ylabel('频数')

# 2. 叠加直方图
axes[1].hist(data1, bins=30, alpha=0.5, color='skyblue', label='分布1')
axes[1].hist(data2, bins=30, alpha=0.5, color='lightcoral', label='分布2')
axes[1].set_title('双分布')
axes[1].set_xlabel('值')
axes[1].set_ylabel('频数')
axes[1].legend()

# 3. 箱线图
box_data = [data1, data2, np.concatenate([data1, data2])]
box = axes[2].boxplot(box_data, patch_artist=True,  # 填充色
                      tick_labels=['分布1', '分布2', '分布3'],
                      medianprops={'color': 'red', 'linewidth': 2}  # 中位数线属性
                      )

# 为箱线图添加颜色
colors = ['lightblue', 'lightcoral', 'lightgreen']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    
axes[2].set_title('箱线图')
axes[2].set_ylabel('值')

plt.tight_layout()
plt.show()