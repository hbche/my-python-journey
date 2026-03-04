# Numpy 教程

NumPy 是 Python 科学计算的基础库。NumPy 的核心是一个强大的 N 维数组对象，它还包含有用的线性代数、傅里叶变换和随机数函数。

## 创建数组

现在我们来导入 `numpy`。大多数人会将其导入为 `np`：

```py
import numpy as np
```

### `np.zeros`

`zeros` 函数可创建一个包含任意数量零的数组：

```py
print(np.zeros(5))  # [0. 0. 0. 0. 0.]
```

只需提供一个包含所需行数和列数的元组，就可以同样轻松地创建一个二维数组（即矩阵）。例如，这是一个3x4矩阵：

```py
print(np.zeros((3, 4)))

# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
```

### 一些词汇

- 在 NumPy 中，每个维度被称为一个轴。
- 轴的数量称为秩。
  - 例如，上面的3×4矩阵是一个秩为2的数组（它是二维的）。
  - 第一条轴长度为3，第二条轴长度为4。
- 数组各轴长度的列表称为数组的形状。
  - 例如，上述矩阵的形状是 `(3, 4)`。
  - 该等级等于形状的长度。
- 数组的大小是元素的总数，即所有轴长度的乘积（例如 3×4=12）。

```py
a = np.zeros((3, 4))
print(a.shape)  # 数组的形状，(3, 4)
print(a.ndim)  # 秩(维度) 为 2
print(a.size)   # 总长度为 12
```

### N 维数组

我们还可以创建任意秩的N维数组。例如，这是一个三维数组（秩=3），形状为`(2,3,4)`：

```py
a = np.zeros((3, 4, 5))
print(a)

# [[[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]

#  [[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]

#  [[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]]
```

### 数组的类型

NumPy 数组的类型是 `ndarray`:

```py
import numpy as np

print(type(np.zeros((3, 4))))   # <class 'numpy.ndarray'>
```

### `np.ones`

许多其他NumPy函数可创建ndarray。

这是一个 3x4 的全 1 矩阵：

```py
print(np.ones((3, 4)))

# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]
```

### `np.full`

创建一个指定形状并用给定值初始化的数组。这是一个 3x4 的全 `π` 矩阵。

```py
print(np.full((3, 4), np.pi))

# [[3.14159265 3.14159265 3.14159265 3.14159265]
#  [3.14159265 3.14159265 3.14159265 3.14159265]
#  [3.14159265 3.14159265 3.14159265 3.14159265]]
```

### `np.empty`

一个未初始化的 2x3 数组（其内容不可预测，因为它就是该内存位置当时的数据）。

```py
print(np.empty((2, 3)))

# [[4.24399158e-314 0.00000000e+000 0.00000000e+000]
#  [0.00000000e+000 0.00000000e+000 0.00000000e+000]]
```

> `np.empty` 的内容是随机的，不可预测的。

### `np.array`

当然，我们可以用一个普通的Python数组来初始化一个ndarray。只需调用array函数：

```py
py_array = [[1, 2, 3, 4], [10, 20, 30, 40]]
print(type(py_array))   # <class 'list'>

np_array = np.array(py_array)
print(type(np_array))   # <class 'numpy.ndarray'>
```

### `np.arange`

我们可以使用NumPy的`arange`函数创建`ndarray`，该函数类似于Python内置的`range`函数：

```py
print(np.arange(1, 5))  # [1, 2, 3, 4]
```

它也适用于浮点数：

```py
print(np.arange(1.0, 5.0))  # [1., 2., 3., 4.]
```

当然，我们可以提供一个步长参数。

```py
print(np.arange(1, 5, 0.5))  # [1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5]
```

然而，在处理浮点数时，数组中元素的确切个数并不总是可预测的。例如，考虑以下情况：

```py
print(np.arange(0, 5/3, 1/3))
print(np.arange(0, 5/3, 0.333333333))
print(np.arange(0, 5/3, 0.333333334))

# [0., 0.33333333, 0.66666667, 1., 1.33333333, 1.66666667]
# [0., 0.33333333, 0.66666667, 1., 1.33333333, 1.66666667]
# [0., 0.33333333, 0.66666667, 1., 1.33333334]
```

### `np.linspace`

因此，在涉及浮点数运算时，通常更推荐使用 `linspace` 函数而不是 `arange`。`linspace` 函数会返回一个数组，其中包含均匀分布在两个指定值之间的特定数量的点（注意与 `arange` 不同，其最大值是包含在内的）：

```py
print(np.linspace(0, 5 / 3, 6))
# [0.         0.33333333 0.66666667 1.         1.33333333 1.66666667]
```

| 特性       | `np.arange`                   | `np.linspace`                 |
| ---------- | ----------------------------- | ----------------------------- |
| 含义       | Arange (类似 Python 的 range) | Linear Space (线性空间)       |
| 参数       | start, stop, step             | start, stop, num              |
| 控制方式   | 指定步长                      | 指定样本数量                  |
| 终点       | 不包含 stop                   | 默认包含 stop (endpoint=True) |
| 返回值类型 | 整数或浮点数                  | 浮点数                        |
| 适用场景   | 整数序列、固定步长            | 连续区间、固定采样点数        |

### `np.rand`和`np.randn`

NumPy的随机模块 `random` 提供了多种函数，可用于创建以随机值初始化的 `ndarray`。例如，下面是一个3x4的矩阵，其中的随机浮点数在0到1之间（均匀分布）初始化：

```py
# 生成3行4列，数值在0~1之间的二维数组
print(np.random.rand(3, 4))
# [[0.6506603  0.86503881 0.51304567 0.6778842 ]
#  [0.14299061 0.07071637 0.58358256 0.24915843]
#  [0.90849076 0.27504763 0.53199679 0.09339026]]
```

这是一个3x4矩阵，其中包含从均值为0、方差为1的单变量[正态分布](https://en.wikipedia.org/wiki/Normal_distribution)（高斯分布）中抽取的随机浮点数：

```py
print(np.random.randn(3, 4))

# [[ 1.87901903 -0.75014818 -0.39074093  0.49900705]
#  [ 0.05578551 -0.0355835  -0.55133104 -0.34105085]
#  [-0.51246015 -1.01400438  1.23387943  0.80598619]]
```

| 特性       | `rand`                                                  | `randn` |
| ---------- | ------------------------------------------------------- | ------- |
| 分布       | 均匀分布 (Uniform) 正态分布/高斯分布 (Normal/Gaussian)  |
| 返回值范围 | `[0, 1)` 之间的数 `(-∞, +∞)`，均值为 0，方差为 1        |
| 含义       | Random After Discrete (均匀) Random After Normal (正态) |

为了对这些分布的样子有个直观感受，我们来用一下 [matplotlib（详见 matplotlib 教程）](../tools-matplotlib/index.md)：

```py
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体，防止中文乱码
# Windows 系统使用 'SimHei'（黑体），macOS 使用 'Arial Unicode MS'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号

# 创建图形和坐标轴
fig, ax = plt.subplots()

# 绘制 rand() 生成的均匀分布直方图
# - np.random.rand(100000): 生成 10 万个 [0, 1) 区间均匀分布的随机数
# - density=True: 将直方图归一化为概率密度函数
# - bins=100: 使用 100 个柱子
# - histtype="step": 绘制阶梯线图
ax.hist(
    np.random.rand(100000),
    density=True,
    bins=100,
    histtype="step",
    color="blue",
    label="rand (均匀分布)",
)

# 绘制 randn() 生成的正态分布直方图
# - np.random.randn(100000): 生成 10 万个标准正态分布的随机数（均值=0，方差=1）
ax.hist(
    np.random.randn(100000),
    density=True,
    bins=100,
    histtype="step",
    color="red",
    label="randn (正态分布)",
)

# 设置坐标轴范围：x 轴 [-2.5, 2.5], y 轴 [0, 1.1]
ax.axis([-2.5, 2.5, 0, 1.1])

# 添加图例，位置在左上角
ax.legend(loc="upper left")

# 设置标题和坐标轴标签
ax.set_title("Random distributions (随机数分布对比)")
ax.set_xlabel("Value (值)")
ax.set_ylabel("Density (密度)")

# 显示图形
plt.show()
```

### `np.fromfunction`

我们也可以使用函数来初始化一个 ndarray：

```py
def my_function(x, y, z):
    return x + 10 * y + 100 * z

print(np.fromfunction(my_function, (3, 2, 10)))

# [[[  0. 100. 200. 300. 400. 500. 600. 700. 800. 900.]
#   [ 10. 110. 210. 310. 410. 510. 610. 710. 810. 910.]]

#  [[  1. 101. 201. 301. 401. 501. 601. 701. 801. 901.]
#   [ 11. 111. 211. 311. 411. 511. 611. 711. 811. 911.]]

#  [[  2. 102. 202. 302. 402. 502. 602. 702. 802. 902.]
#   [ 12. 112. 212. 312. 412. 512. 612. 712. 812. 912.]]]
```

NumPy 首先创建三个 `ndarray` 数组（每个维度一个），每个数组的形状为 `(3, 2, 10)`。每个数组的值等于沿着特定轴的坐标。例如，`z` 数组中的所有元素都等于它们的 z 坐标：

```py
[[[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
  [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]]

 [[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]
  [ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]]

 [[ 2.  2.  2.  2.  2.  2.  2.  2.  2.  2.]
  [ 2.  2.  2.  2.  2.  2.  2.  2.  2.  2.]]]
```

因此，上述表达式 $x + 10 \times y + 100 \times z$ 中的 x 、 y 和 z 其实是 ndarray 对象（我们将在下文中讨论数组的算术运算）。关键在于，my_function 函数只被调用了一次，而不是针对每个元素调用一次。这使得初始化过程非常高效。

## 数组数据

### `dtype`

NumPy 的 ndarray 之所以高效，部分原因是其所有元素必须具有相同类型（通常为数字）。我们可以通过 dtype 属性查看数据类型：

```py
a = np.arange(1, 5)
print(a.dtype, a)   # int64 [1 2 3 4]

a = np.arange(1.0, 5.0)
print(a.dtype, a)   # float64 [1. 2. 3. 4.]
```

与其让 NumPy 猜测应该使用哪种数据类型，我们可以在设置数组时明确指定类型，通过设置 dtype 参数实现：

```py
a = np.arange(1, 5, dtype=np.complex64)
print(a.dtype, a)   # complex64 [1.+0.j 2.+0.j 3.+0.j 4.+0.j]
```

支持的数据类型包括有符号整型int8、int16、int32、int64，无符号整型uint8/16/32/64，浮点数float16/32/64以及复数complex64/128。关于[基本数据类型](https://numpy.org/doc/stable/user/basics.types.html)及其[明确别名](https://numpy.org/doc/stable/reference/arrays.scalars.html#sized-aliases)的完整列表，请查阅相关文档。

### `itemsize`

`itemsize` 属性返回每个条目的大小（以字节为单位）。

```py
a = np.arange(1, 5, dtype=np.complex64)
print(a.itemsize)   # 8
```

### `data` 缓存

数组的数据实际上在内存中是以扁平（一维）字节缓冲区形式存储的，可通过 `data` 属性访问（不过我们很少会用到它）。

```py
f = np.array([[1, 2], [1000, 2000]], dtype=np.int32)
print(f.data)   # <memory at 0x000001A103D9B100>
```

在 Python 2 中，`f.data` 是一个缓冲区。在 Python 3 中，它是一个内存视图。

```py
f = np.array([[1, 2], [1000, 2000]], dtype=np.int32)
if hasattr(f.data, "tobytes"):
    data_types = f.data.tobytes()  # python 3
else:
    data_types = memoryview(f.data).tobytes()  # python 2

print(data_types)
# b'\x01\x00\x00\x00\x02\x00\x00\x00\xe8\x03\x00\x00\xd0\x07\x00\x00'
```

多个 ndarray 可以共享相同的数据缓冲区，这意味着修改其中一个也会修改其他数组。我们稍后将看到一个例子。

## 重塑数组

### 替换

### 散开
