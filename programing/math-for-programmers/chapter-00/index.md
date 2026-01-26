# 前置知识

本书是使用 Python 学习数学知识，其中涉及到使用 Matplotlib 进行二维三维绘图，本章
节记录学习了 Matplotlib 的使用。

## 1.1 Matplotlib 快速入门

### 1.1.1 Matplotlib 是什么

Matplotlib 是 Python 最流行的 2D/3D 绘图库，广泛用于数据可视化、科学计算和数学分
析。

安装方式：

```bash
pip install matplotlib
```

### 1.1.2 两种绑定方式

方式一： pyplot 快捷方式（推荐新手入门）

```py
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])   # 绑定数据
plt.show()  # 展示绘图
```

方式二：面向对象（推荐实际项目）

```py
import matplotlib.pyplot as plt

x_list = list(range(1, 5))
y_list = [x ** 2 for x in x_list]

fig, ax = plt.subplots()
ax.plot(x_list, y_list) # 绑定数据
plt.show()  # 调用 plt.show 展示绘图
```

> 区别：pyplot 隐式管理 figure，适合简单脚本；面向对象更清晰，适合复杂项目。

### 1.1.3 核心概念： Figure 和 Axes

- Figure: 代表整个画布，可以包含多个子图
- Axes：代表单个子图（包括坐标轴、标题等）
- Axis: 坐标轴（x 轴、y 轴）

### 1.1.4 创建图表的几种方式

```py
import matplotlib.pyplot as plt
import numpy as np

# 方式1：创建单个子图
fig, ax = plt.subplots()

# 方式2：创建多个子图（2行2列）
fig, ax = plt.subplots(2, 2)

# 方式3：手动创建子图（指定位置）
ax = fig.add_subplot(221)

# 方式4：创建画布
fig = plt.figure()
```

### 1.1.5 创建图表类型

#### 1.1.5.1 折线图（Line Plot）

```py
# 折线图 示例
import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-math.pi, math.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
# 绑定数据，并设置数据样式
ax.plot(x, y, label="sin(x)", color="blue", linestyle="--", linewidth=2)
ax.set_xlabel("x")  # 设置 x 轴的标题
ax.set_ylabel("y")  # 设置 y 轴的标题
ax.set_title("Sin Function")    # 设置图表的标题
ax.legend()     # 展示图例

plt.show()
```

#### 1.1.5.2 散点图（Scatter Plot）

```py
# 绘制散点图
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

fig, ax = plt.subplots()
ax.scatter(x, y, c='red', s=50, alpha=0.6)
plt.show()
```

#### 1.1.5.3 柱状图（Bar Chart）

```py
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 2, 5]
fig, ax = plt.subplots()
ax.bar(categories, values, color=['red', 'green', 'blue', 'orange'])
plt.show()
```

#### 1.1.5.4 直方图（Histogram）

```py
data = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(data, bins=30, edgecolor="black", alpha=0.7)
plt.show()
```

#### 1.1.5.5 饼图（Pie Chart）

```py
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()
```

#### 1.1.5.6 3D 绘图

mpl_toolkits 是 matplotlib 绘图库自带的工具箱，在安装 matplotlib 时会一起安装，
所以不需要单独安装 mpl_toolkits。

```py
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

ax.plot_surface(X, Y, Z, cmap="viridis")
plt.show()
```

> 需要深入了解 3D

### 1.1.6 图表元素定制

| 元素     | 设置方法                         |
| -------- | -------------------------------- |
| 标题     | `ax.set_title()`                 |
| x 轴标签 | `ax.set_xlabel()`                |
| y 轴标签 | `ax.set_ylabel()`                |
| 图例     | `ax.legend()`                    |
| 坐标范围 | `ax.set_xlim()`、`ax.set_ylim()` |
| 网格线   | `ax.grid(True)`                  |
| 刻度标签 | `ax.set_xticklabels()`           |

### 1.1.7 多子图布局

```py
# 多子图布局示例
import matplotlib.pyplot as plt

# 声明 2 行 2 列 布局的画板
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 声明每个区域中的画布
axes[0, 0].plot([1, 2, 3], [1, 2, 3])
axes[0, 0].set_title("Top Left")

axes[0, 1].scatter([1, 2, 3], [1, 2, 3])
axes[0, 1].set_title("Top Right")

axes[1, 0].bar(['A', 'B', 'C'], [4, 2, 3])
axes[1, 0].set_title("Bottom Left")

axes[1, 1].hist([1, 2, 2, 3, 3, 3], bins=3)
axes[1, 1].set_title('Bottom Right')

plt.tight_layout()
plt.show()
```

### 1.1.8 常用样式设置

```py
# 使用内置样式
plt.style.use('seaborn-v0_8-darkgrid')

# 手动设置
plt.rcParams['font.size'] = 12
plt.rcParams['figure.figsize'] = (10, 6)
```

## 1.2 Matplotlib 深入浅出指南

### 1.2.1 基础理念

#### 1.2.1.1 三层架构

Matplotlib 采用三层架构，这就像画画一样：

- 画板(Figure)：最底层，承载一切
- 画布(Axes)：在画板上，可以有多张画布
- 画笔(Artist)：在画布上作画的具体元素

基础示例：

```py
import matplotlib.pyplot as plt

# 一句话画图
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("The simplest line chart")
plt.show()
```

#### 1.2.1.2 两种编程风格：MATLIB 风格 vs 面向对象风格

风格一：MATLIB 风格

```py
import matplotlib.pyplot as plt

# 就像在MATLIB 中一样，直接使用plt.*
plt.figure(figsize=(8, 4))  # 创建画布
plt.plot([1, 2, 3], [2, 4, 1])  # 在第一张画布上画线
plt.title("MATLIB Style")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()
```

风格二：面向对象风格（推荐，更灵活）

```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))  # fig是画板，ax是画布
ax.plot([1, 2, 3], [2, 4, 1])   # 在 ax 上画线
ax.set_title("OOP Style")
ax.set_xlabel("X axis")
ax.set_ylabel("y axis")
ax.grid(True)
plt.show()
```

### 1.2.2 基础图表绘制

#### 1.2.2.1 点的艺术：散点图

```py
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
```

#### 1.2.2.2 线的魔法：折线图的各种变化

```py
# # 折线图 示例
# import matplotlib.pyplot as plt
# import numpy as np
# import math

# x = np.linspace(-math.pi, math.pi, 100)
# y = np.sin(x)

# fig, ax = plt.subplots()
# # 绑定数据，并设置数据样式
# ax.plot(x, y, label="sin(x)", color="blue", linestyle="--", linewidth=2)
# ax.set_xlabel("x")  # 设置 x 轴的标题
# ax.set_ylabel("y")  # 设置 y 轴的标题
# ax.set_title("Sin Function")    # 设置图表的标题
# ax.legend()     # 展示图例

# plt.show()

# 线的魔法
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) # 0到100之间的100个点

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 基础的折线图
ax[0, 0].plot(x, np.sin(x), label='sin(x)')
ax[0, 0].set_title('Sin function')
ax[0, 0].legend()

# 带标记点的折线图
ax[0, 1].plot(x, np.cos(x),
              marker='o',   # 标记形状
              markersize=4, # 标记大小
              markevery=10, # 每10个标记一个
              linewidth=1.5,
              color='coral',
              label='cos(x)'
              )
ax[0, 1].set_title('带标记的余弦函数')
ax[0, 1].legend()

# 多条线对比
ax[1, 0].plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax[1, 0].plot(x, np.sin(2*x), label='sin(2x)', linestyle='--', linewidth=2)
ax[1, 0].plot(x, np.sin(3*x), label='sin(3x)', linestyle=':', linewidth=2)
ax[1, 0].set_title('多条线对比')
ax[1, 0].legend()

# 填充区域图
ax[1, 1].fill_between(x, np.sin(x), alpha=0.3, color='skyblue', label='sin(x) 区域')
ax[1, 1].plot(x, np.sin(x), color='blue', linewidth=2)

plt.rcParams['font.sans-serif'] = ['SimHei']    # 显示中文
plt.rcParams['axes.unicode_minus'] = False

plt.tight_layout()  # 自动调整子图间距
plt.show()
```

### 1.2.3 进阶图表绘制

#### 1.2.3.1 柱状图家族：比较的艺术

```py
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
```

#### 1.2.3.2 分布可视化：直方图与箱线图

```py
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
```

### 1.2.4 专业图表定制（让图表说话）

#### 1.2.4.1 颜色与样式：视觉传达的科学

```py
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
```

#### 1.2.4.2 多子图与布局管理

### 1.2.5 实战项目

#### 1.2.5.1 绘制直角坐标系

```py
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig, axes = plt.subplots()

# 设置坐标轴的范围
axes.set_xlim(-6, 7)
axes.set_ylim(-5, 6)

# 设置 水平和垂直 坐标轴
axes.axhline(y=0, color='black', linewidth=0.8)
axes.axvline(x=0, color='black', linewidth=0.8)

# # 将 x轴 y轴 主刻度器定位器设置为间隔1.0
axes.xaxis.set_major_locator(MultipleLocator(1.0))
axes.yaxis.set_major_locator(MultipleLocator(1.0))
# # 开启网格线，默认与主刻度对齐
axes.grid(True, which='major', linestyle='--', linewidth=0.8, color='lightgray')

# 绘制原点
plt.scatter([0], [0], marker='x', color='black')

# 绘制散点
points = [
    (5, 1),
    (6, 4),
    (3, 1),
    (1, 2),
    (-1, 5),
    (-2, 5),
    (-3, 4),
    (-4, 4),
    (-5, 3),
    (-5, 2),
    (-2, 2),
    (-5, 1),
    (-4, 0),
    (-2, 1),
    (-1, 0),
    (0, -3),
    (-1, -4),
    (1, -4),
    (2, -3),
    (2, -3),
    (1, -2),
    (3, -1),
    (5, 1),
]
# 绘制连线
plt.plot([x for (x, _) in points], [y for (_, y) in points])
# 绘制端点
plt.scatter([x for (x, _) in points], [y for (_, y) in points], marker='o', color='black')

plt.tight_layout()
plt.show()
```

### 1.2.6 实用小技巧

```py
# 1. 保存高清图片
plt.savefig('chart.png', dpr=300, bbox_inches='tight')

# 2. 使用内置样式
print(plt.style.available)  # 查看所有可用样式
plt.style.use('seaborn-v0_8-whitegrid') # 使用样式

# 3. 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中公文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示坐标轴中的负号
# 全量的rcParams可以使用rcParams.keys()查看
print(plt.rcParams.keys())

# 4. 创建循环颜色
colors = plt.cm.tab10(np.linspace(0, 1, 10))    # 获取10种颜色
```

> 注意：Matplotlib 中的规则是 `rcParms` 只对 “之后创建的对象”生效，所以我们设置
> 字体需要在创建对象之前设置，否则这些参数对后续生成的对象不生效。
