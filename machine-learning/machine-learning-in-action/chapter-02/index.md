# 第 2 章 K 近邻算法

## 2.1 K近邻算法概述

定义：K-近邻采用特征值之间的距离方法进行分类。

优点：精度高、对异常值不敏感、无数据输入设定

缺点：计算复杂度高、空间复杂度高

适用数据范围：数值型和标称型

### 2.1.1 准备：使用Python导入数据

```py
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

对未知类别属性的数据集中的每个点依次执行以下操作：

1. 计算已知类别数据集中的点与当前点之间的距离
2. 按照距离递增次序排序
3. 选区与当前点距离最小的k个点
4. 确定前k个点所在类别的出现评率
5. 返回前k个点出现评率最高的列表作为当前点的预测分类

```py
def classifyKNN(
    input_vector: list[float],
    dataset: np.ndarray,
    labels: list[str],
    k: int = 3,
) -> tuple[str, int]:
    """使用 KNN 算法对输入向量进行分类。

    计算输入向量与数据集中每个样本的欧氏距离，
    选取距离最近的 k 个样本，通过多数投票决定分类结果。

    Args:
        input_vector: 待分类的特征向量，如 [0.4, 0.2]
        dataset: 形状为 (n, m) 的训练集特征矩阵，n 为样本数，m 为特征维度
        labels: 长度为 n 的标签列表，与 dataset 各行一一对应
        k: 选取的最近邻数量，默认为 3

    Returns:
        得票最多的 (标签, 票数) 元组，如 ('B', 2)
    """
    # 将输入向量广播为与数据集相同的形状，便于逐元素求差
    diff = np.tile(input_vector, (dataset.shape[0], 1)) - dataset
    # 计算输入向量到每个样本的欧氏距离
    distances = np.sum(diff**2, axis=1) ** 0.5
    # 按距离从小到大排序，返回排序后的样本索引
    sorted_indices = distances.argsort()
    # 统计前 k 个最近邻中各标签的出现次数
    label_count = {}
    for i in range(k):
        label = labels[sorted_indices[i]]
        label_count[label] = label_count.get(label, 0) + 1
    # 按票数降序排序，返回得票最多的标签
    sorted_label_count = sorted(
        label_count.items(), key=operator.itemgetter(1), reverse=True
    )
    return sorted_label_count[0][0]
```

### 2.1.3 如何测试分类器

基于 k-近邻 算法实现的分类并不能保证百分百分类正确，我们可以使用多种方法检测分类器的正确率。分类器的性能也会受到多种因素的影响，如分类器设置和数据集等。

为了测试分类器的效果，我们可以准备一些已知答案的数据，但是答案不能告诉分类器，检验分类器给出的结果是否符合预期结果。通过大量的测试数据，我们可以得到分类器的错误率——分类器给出错误结果的次数除以测试执行的总数。

## 2.2 示例：使用k-近邻算法改进约会网站的配对效果

流程：

1. 收集数据：提供文本文件
2. 准备数据：使用 Python 解析文本文件
3. 分析数据：使用matplotlib画二维扩散图
4. 训练算法：k-近邻算法没有此步骤
5. 测试算法：使用数据集的部分数据作为训练数据，使用数据集的部分数据作为测试数据
6. 使用算法：产生简单的命令行程序

### 2.2.1 准备数据：从文本文件中解析数据

将每年获得的飞行常客里程数、玩视频游戏所耗时间百分比、每周消耗的冰淇淋公升数作为特征，学习其受欢迎程度。

```py
def file_to_matrix(filename):
    file_reader = open(filename, encoding="utf-8")
    file_lines = file_reader.readlines()
    line_total = len(file_lines)
    data_set = np.zeros((line_total, 3))
    label_set = []
    for index in range(line_total):
        line = file_lines[index]
        line = line.strip()
        line_content = line.split("\t")
        data_set[index, :] = line_content[0:3]
        label_set.append(line_content[-1])
    return data_set, label_set
```

### 2.2.2 分析数据：使用 Matplotlib 创建散点图

根据玩视频游戏所耗时间百分比和每周消耗的冰淇淋公升数两个特征作为坐标绘制散点图来分析数据

```py
def plot_data_set(data_set, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # 将 labels（字符串列表）通过 np.array(labels, dtype=float) 转为数值数组，否则 15.0 * 运算会报错
    label_values = np.array(labels, dtype=float)
    # 绘制玩视频游戏所耗时间百分比和每周消耗的冰淇淋公升数的散点图
    # 使用标签值，给每个点设置颜色和大小
    ax.scatter(data_set[:, 1], data_set[:, 2], s=15.0 * label_values, c=label_values)
    ax.axis([-2, 25, -0.2, 2.0])
    plt.xlabel("Percentage of Time Spent Playing Video Games")
    plt.ylabel("Liters of Ice Cream Consumed Per Week")
    plt.show()
```

根据每年获得的飞行常客里程数和玩视频游戏所耗时间百分比这两个特征作为坐标绘制散点图再来分析数据：

```py
def plot_data_set(data_set, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    label_values = np.array(labels, dtype=float)
    unique_labels = np.unique(label_values)
    label_names = {1: "不喜欢", 2: "魅力一般", 3: "极具魅力"}
    # 按标签分组绘制，每组生成独立的图例条目
    for lbl in unique_labels:
        mask = label_values == lbl
        ax.scatter(
            data_set[mask, 0],
            data_set[mask, 1],
            s=15.0 * lbl,
            label=label_names.get(int(lbl), str(int(lbl))),
        )
    ax.legend(loc="upper left", fontsize=10, framealpha=0.9)
    # Windows 系统使用 'SimHei'（黑体），macOS 使用 'Arial Unicode MS'
    plt.rcParams["font.sans-serif"] = ["SimHei"]  # 正常显示中文
    plt.rcParams["axes.unicode_minus"] = False  # 正常显示负号
    plt.xlabel("每年获取的飞行常客里程数")
    plt.ylabel("玩视频游戏所耗时间百分比")
    plt.show()
```

### 2.2.3 准备数据：归一化数值

我们发现，每年 "获取的飞行常客里程数" 与另外两个特征值相差较大，当计算距离时，后两个特征基本被忽略了。

$$
\sqrt{(0 - 67)^2 + (20 000 - 32 000)^2 + (1.1 - 0.1)^2}
$$

使得另外两个特征被淡化了，为了使得每个特征都发挥效果，我们对数据集进行归一化处理：

```py
def autoNorm(data_set):
    # 取每一列中的最小值、最大值
    min_value = np.min(data_set, axis=0)
    max_value = np.max(data_set, axis=0)
    ranges = max_value - min_value
    data_size = data_set.shape[0]
    # 根据数据集，将其每一行数据的每个特征减去各自的最小值，再除以特征的范围，得到每个特征的占比
    normal_data_set = (data_set - np.tile(min_value, (data_size, 1))) / (
        np.tile(ranges, (data_size, 1))
    )
    return normal_data_set, ranges, min_value
```

### 2.2.4 测试算法

```py
def dating_class_test():
    # 一般测试数据占比 10%
    hoRatio = 0.1
    data_set, label_set = file_to_matrix("dating_test_set.txt")
    normal_set, ranges, minValue = auto_norm(data_set)
    m = normal_set.shape[0]
    num_test_vecs = int(m * hoRatio)
    error_count = 0.0
    for index in range(num_test_vecs):
        classifier_result = classifyKNN(
            normal_set[index, :],
            # 使用其余 90% 的数据作为学习数据
            normal_set[num_test_vecs:m, :],
            label_set[num_test_vecs:m],
            3,
        )
        print(
            f"The classifier came back with: {classifier_result}, the real answer is: {label_set[index]}."
        )
        if classifier_result != label_set[index]:
            error_count += 1.0
    print(f"The total error rate is: {error_count / float(num_test_vecs)}")
```

还可以通过修改 hoRatio 和变量 k 来降低错误率。

### 2.2.5 使用算法：构建完整可用系统

## 2.3 示例：手写数字识别系统

使用 k-近邻 算法实现手写数字识别系统步骤：

1. 收集数据
2.
