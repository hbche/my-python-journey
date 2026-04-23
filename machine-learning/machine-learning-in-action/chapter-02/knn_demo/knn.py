from typing import Any, Sequence, Tuple

import operator
import matplotlib.pyplot as plt
import numpy as np


def create_data_set() -> tuple[np.ndarray, list[str]]:
    """创建用于 KNN 演示的样本数据集。

    Returns:
        包含两个元素的元组：
        - group: 形状为 (4, 2) 的特征矩阵，每行是一个样本的二维坐标
        - labels: 每个样本对应的分类标签列表
    """
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A", "A", "B", "B"]
    return group, labels


def classifyKNN(
    input_vector: np.ndarray,
    dataset: np.ndarray,
    labels: np.ndarray | Sequence[Any],
    k: int = 3,
) -> Tuple[Any, int]:
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
    return sorted_label_count[0]


def file_to_matrix(filename: str) -> tuple[np.ndarray, np.ndarray]:
    with open(filename, encoding="utf-8") as file_reader:
        file_lines = file_reader.readlines()
    line_total = len(file_lines)
    data_set = np.zeros((line_total, 3), dtype=float)
    label_set = np.zeros((line_total,), dtype=int)
    for index in range(line_total):
        line = file_lines[index]
        line = line.strip()
        line_content = line.split("\t")
        data_set[index, :] = line_content[0:3]
        label_set[index] = line_content[-1]
    return data_set, label_set


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


def auto_norm(data_set):
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


dating_class_test()

# group, label = file_to_matrix("dating_test_set.txt")
# normal_data_set, ranges, min_value = autoNorm(group)
# print(normal_data_set)
# print(ranges)
# print(min_value)
