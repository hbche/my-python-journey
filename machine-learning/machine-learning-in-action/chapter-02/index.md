# 第 2 章 K 近邻算法

## 2.1 K近邻算法概述

定义：K-近邻采用特征值之间的距离方法进行分类。

优点：精度高、对异常值不敏感、无数据输入设定

缺点：计算复杂度高、空间复杂度高

适用数据范围：数值型和标称型

### 2.1.1 准备：使用Python导入数据

``` py
import numpy as np

def createDataSet():
    group = np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = createDataSet()
print(f"Group: {group}")
print(f"Labels: {labels}")
```

### 2.1.2 实施KNN算法

``` py

```
