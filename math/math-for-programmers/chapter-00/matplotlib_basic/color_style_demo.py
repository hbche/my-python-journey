# 颜色与样式：视觉传达的科学
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建图形和坐标轴
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)   # 1行1列，第一个

# 使用不同的线型和颜色
line_styles = ['-', '--', '-.', ':']
colors = ['#FF6B6B', '#4ECDC4', '#FFD166', '#06D6A0']

for i in range(4):
    y = np.sin(x + i * 0.5)
    ax.plot(x, y,
            linewidth=2,
            linestyle=line_styles[i],
            color=colors[i],
            marker='o' if i ==0 else None,  # 只在第一条线加标记
            markersize=4,
            markevery=20,
            label=f'曲线{i+ 1}'
            )
    
# 专业级的图表修饰
ax.set_title('专业图表设计示例', 
             fontsize=16, 
             fontweight='bold', 
             pad=20,    # 标题与图表的间距
            )

ax.set_xlabel('时间（秒）', fontsize=12)
ax.set_ylabel('振幅', fontsize=12)

# 设置坐标轴范围
ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)

# 设置网格
ax.grid(True, which='both', linestyle='--', alpha=0.3)

# 添加图例
ax.legend(loc='upper right', fontsize=10, framealpha=0.9)

# 设置坐标轴刻度
ax.text(2, 1.2, '峰值区域',
        fontsize=10,
        bbox=dict(boxstyle='round,pad=0.3',
                  facecolor='yellow',
                  alpha=0.3
                  )
        )

# 添加箭头标识
ax.annotate('最小值点', 
            xy=(4.7, -1),
            xytext=(6, -1.2),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3'),
            fontsize=10
            )

plt.tight_layout()
plt.show()
