# Pandas 教程

_`pandas` 库提供了高性能、易用的数据结构和数据分析工具。其主要数据结构是 `DataFrame`，可以将其视为内存中的二维表格（类似电子表格，有列名和行标签）。Excel中的许多功能均可通过编程方式实现，例如，创建数据透视表、基于其他列计算新列、绘制图表等。我们还可以按列值对行进行分组，或执行类似SQL的表连接操作。Pandas同样擅长处理时间序列数据。_

前置条件：

- NumPy - 如果不熟悉 NumPy ，我们可以先学习 [NumPy教程](../tools-numpy/index.md)

## 设置

首先，导入 `pandas`。通常大家用 `pd` 作为别名：

```py
import pandas as pd
```

## `Series` 对象

`pandas` 库包含以下有用的数据结构：

- `Series` 对象。序列对象，我们将在此进行讨论。它是一种一维数组，类似于电子表格中的一列（具有列名和行标签）。
- `DataFrame` 对象。这是一个二维表格，类似于电子表格（包含列名和行标签）。
- `Panel` 对象。我们可以将 `Panel` 视作一个由多个 `DataFrame` 组成的字典。由于使用频率较低，这里不做详细讨论。

### 创建 `Series`

让我们从创建第一个 `Series` 对象开始吧！

```py
series_data = pd.Series([2, -1, 3, 5])
print(series_data)
# 0    2
# 1   -1
# 2    3
# 3    5
# dtype: int64
```

### 类似于1维 `ndarray`

`Series` 对象的行为与一维的 NumPy `ndarray` 非常相似，我们通常可以将它们作为参数传递给 `NumPy` 函数。

```py
print(np.exp(series_data))
# 0      7.389056
# 1      0.367879
# 2     20.085537
# 3    148.413159
# dtype: float64
```

对 `Series` 进行算术运算也是可以的，这些运算会逐元素应用，就像处理 `ndarray` 一样。

```py
print(series_data + [1000, 2000, 3000, 4000])
# 0    1002
# 1    1999
# 2    3003
# 3    4005
# dtype: int64
```

与 NumPy 类似，如果我们将一个单一数字与一个 `Series` 相加，这个数字会被加到 `Series` 中的所有元素上。这被称为*广播*。

```py
print(series_data + 1000)
# 0    1002
# 1     999
# 2    1003
# 3    1005
# dtype: int64
```

对于所有二进制运算，如乘法 `*` 或除法 `/`，甚至是条件运算，也是如此。

```py
print(series_data < 0)
# 0    False
# 1     True
# 2    False
# 3    False
# dtype: bool
```

### 索引标签

`Series` 对象中的每个元素都有一个唯一的标识符，称为索引标签。默认情况下，索引标签是元素在 `Series` 中的序号（从 `0` 开始），但我们也可以手动设置索引标签。

```py
s2 = pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "darwin"])
print(s2)
# alice       68
# bob         83
# charles    112
# darwin      68
# dtype: int64
```

然后，我们可以像使用字典一样使用这个 `Series`：

```py
print(s2["bob"])    # 83
```

为了明确区分通过标签索引和整数位置索引，建议始终在通过标签访问时使用 `loc` 属性，在通过整数位置访问时使用 `iloc` 属性。

```py
print(s2.loc["bob"])    # 使用标签索引
print(s2.iloc[1])       # 使用整数索引
```

切片操作 `Series` 时也会对索引标签进行切片。

```py
print(s2.iloc[1:3])
# bob         83
# charles    112
# dtype: int64
```

使用默认数值标签时，这可能导致意外结果，请务必谨慎。

```py
surprise = pd.Series([1000, 1001, 1002, 1003])
print(surprise)
# 0    1000
# 1    1001
# 2    1002
# 3    1003
# dtype: int64
```

```py
surprise_slice = surprise[2:]
print(surprise_slice)
# 2    1002
# 3    1003
# dtype: int64
```

哦，看！第一个元素的索引标签是 `2` 。索引标签为 `0` 的元素不在切片中。

```py
try:
    surprise_slice[0]
except KeyError as e:
    print("Key error: ", e)
# Key error:  0
```

但请记住，我们可以通过 `iloc` 属性使用整数位置来访问元素。这也说明了为什么通过 `loc` 和 `iloc` 访问 `Series` 对象始终更为可取的另一层原因。

```py
print(surprise_slice.iloc[0])   # 1002
```

### 从 `dict` 初始化

我们也可以从一个 `dict` 创建一个 `Series` 对象。字典的 key 将作为所以标签使用。

```py
weight = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
s3 = pd.Series(weight)
print(s3)
# alice     68
# bob       83
# colin     86
# darwin    68
# dtype: int64
```

我们可以通过明确指定所需的索引，来控制我们希望包含在系列中的元素及其顺序。

```py
weight = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
s3 = pd.Series(weight, index=["colin", "alice"])
print(s3)
# colin    86
# alice    68
# dtype: int64
```

### 自动对齐
