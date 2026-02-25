# 使用logistic回归对数据分类

目标：
- 理解分类器，评估分类器
- 寻找决策边界来对两种数据分类
- 用logistic函数逼近分类数据集
- 为logistic回归编写代价函数
- 采用梯度下降法寻找最佳拟合的logistic函数

分类是机器学习中最重要的问题之一。本节将利用对二手车数据的特征分析来实现分类算法。

在构建用于分类的机器学习算法时，使用的真是数据越多，算法学到的就越多，在分类任务重表现得也越好。

尽管分类模型的输入和输出与回归算法模型的不同，但实际上可以使用一种回归类型来构建分类器。我们将本章中实现的算法称为**logistic回归**。为了训练这个算法，我们需要从数据集开始着手：如果二手车是宝马，标记为1；如果是普锐斯，标记为0。

| 里程     | 价格     | 是宝马吗 |
| -------- | -------- | -------- |
| 110890.0 | 13995.00 | 1        |
| 94133.0  | 13982.00 | 1        |
| 70000.0  | 9900.00  | 0        |
| 46778.0  | 14599.00 | 1        |
| 84507.0  | 14998.00 | 0        |
| ...      | ...      | ...      |

我们将借助 logistic 函数基于这些数据的前两列，生成一个介于0和1之间的值。

## 15.1 用真实数据测试分类函数

下面编写一个简单的函数来识别数据中的宝马。

``` py
def bmw_finder(price):
    """
    基于价格特征对车辆进行分类，当价格大于25000时，认为是宝马
    """
    if price > 25000:
        return 1
    else:
        return 0
```
这个分类器的表现可能没有那么好，因为行驶里程多的宝马可能卖不到25000美元。但是我们可以用真实数据来衡量这个分类器。

### 15.1.1 加载汽车数据

我们预先准备好了汽车数据，编写 tets_classifier 函数会更容易。

``` py
from car_data import bmws, priuses
all_car_data = []
for bmw in bmws:
    all_car_data.append((bmw.mileage, bmw.price))
for prius in priuses:
    all_car_data.append((prius.mileage, prius.price))
```

### 15.1.2 测试分类函数

``` py
def test_classifier(f, data: tuple[Car]):
    """
    测试分类器的准确率
    """
    trues = 0
    falses = 0
    for mileage, price, is_bmw in data:
        if bmw_finder(price) == is_bmw:
            trues += 1
        else:
            falses += 1

    return trues / (trues + falses)
```

测试分类器的准确率：

``` py
print(test_classifier(bmw_finder, all_car_data))    # 0.59
```

## 15.2 绘制决策边界

我们使用Matplotlib绘制数据节点，并且查看分类器对应分界线的效果。

### 15.2.1 绘制汽车的向量空间

``` py
import matplotlib.pyplot as plt

def plot_data(ds):
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题
    plt.xlabel("里程数（英里）", fontsize=16)
    plt.ylabel("价格（美元）", fontsize=16)
    plt.scatter(
        [d[0] for d in ds if d[2] == 0], [d[1] for d in ds if d[2] == 0], c="C1"
    )
    plt.scatter(
        [d[0] for d in ds if d[2] == 1],
        [d[1] for d in ds if d[2] == 1],
        c="C0",
        marker="x",
    )
```