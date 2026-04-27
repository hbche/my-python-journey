# 回顾本章学习的知识点
import math
import operator


def information_entropy(data_set):
    """
    计算数据集的信息熵：H=sum_{i=1}^{n}p(x_i)(-log_{2}{p(x_i)})
    """
    print(f"Current data set: {data_set}")
    # 数据集总数
    data_size = len(data_set)
    # 各个标签统计对应的数目
    label_count_map = {}
    for item in data_set:
        current_label = item[-1]
        if current_label not in label_count_map:
            label_count_map[current_label] = 1
        else:
            label_count_map[current_label] += 1
    entropy = 0.0
    for label, count in label_count_map.items():
        # 计算每个 标签 的概率
        label_probability = float(count / data_size)
        print(f"Current label is: {label}, probability is: {label_probability}.")
        entropy += -(label_probability * math.log2(label_probability))
    return entropy


def split_data_set(data_set, axis, value):
    """
    根据给定的数据集、分类特征及特征值来划分数据
    """
    # 由于 list 类型是引用传递，所以需要重新生成列表，不可对原始 data_set 进行修改，否则会影响原始数据集
    rest_data_set = []
    for item in data_set:
        if item[axis] == value:
            rest_item = item[:axis] + item[axis + 1 :]
            rest_data_set.append(rest_item)
    return rest_data_set


def calculate_best_feature_split(data_set):
    """
    calculate_best_feature_split 的 计算最好特征划分方式

    :param data_set: 数据集
    """
    # 特征总数
    feature_total = len(data_set[0]) - 1
    # 当前数据集的信息熵
    base_entropy = information_entropy(data_set)
    print(f"Base info entropy: {base_entropy}\n")
    # 最佳信息增益
    best_info_gain = 0.0
    # 最佳特征索引
    best_feature_index = -1
    # 遍历每个特征划分数据集的信息增益
    for feature_index in range(feature_total):
        # 获取当前属性对应的所有去重之后的值
        feature_values = set([item[feature_index] for item in data_set])
        # 计算当前属性不同值计算出来的熵
        current_entropy = 0.0
        # 遍历特征所有标签分类的信息熵
        for feature_value in feature_values:
            # 计算每一个属性分类对应的信息熵
            sub_data_set = split_data_set(data_set, feature_index, feature_value)
            probability = len(sub_data_set) / len(data_set)
            current_entropy += probability * information_entropy(sub_data_set)
        # 当前特征所有标签产生的信息增益
        current_info_gain = base_entropy - current_entropy
        print(
            f"Current feature index is: {feature_index}, current info gain is : {current_info_gain}\n"
        )
        # 比较当前特征所有值信息增益对信息熵产生的影响，去最低的信息熵作为最优分类
        if current_info_gain > best_info_gain:
            best_info_gain = current_info_gain
            best_feature_index = feature_index
    # 返回最佳特征索引
    return best_feature_index


def majority_count(class_list):
    """
    majority_count: 计算分类占比最高的分类

    :param class_list: 分类列表
    """
    class_count_map = {}
    for item in class_list:
        if item not in class_count_map:
            class_count_map[item] = 0
        class_count_map[item] += 1
    sorted_class_count_map = sorted(
        class_count_map.items(), key=operator.itemgetter(1), reverse=True
    )
    return sorted_class_count_map[0][0]


def create_decision_tree(data_set, labels):
    """
    递归构建决策树

    Args:
        data_set: 数据集，每条记录最后一列为类别标签
        labels:  特征名称列表

    Returns:
        dict: 嵌套字典表示的决策树，叶子节点为类别标签
    """
    # 提取所有样本的类别标签
    class_list = [item[-1] for item in data_set]

    # 终止条件1: 当前数据集所有样本类别相同，返回该类别作为叶子节点
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]

    # 终止条件2: 所有特征已用完（只剩类别列），返回出现次数最多的类别
    if len(data_set[0]) == 1:
        return majority_count(class_list)

    # 选择信息增益最大的特征作为当前划分特征
    best_feature_index = calculate_best_feature_split(data_set)
    best_feature_label = labels[best_feature_index]

    # 以最佳特征为根节点构建子树
    my_tree = {best_feature_label: {}}

    # 从特征列表中移除已使用的特征（注意：这会修改传入的 labels 列表）
    del labels[best_feature_index]

    # 获取该特征的所有可能取值
    feature_values = set([item[best_feature_index] for item in data_set])

    # 对每个取值递归构建子树
    for value in feature_values:
        sub_labels = labels[:]  # 复制一份标签列表，避免递归分支间相互干扰
        my_tree[best_feature_label][value] = create_decision_tree(
            split_data_set(data_set, best_feature_index, value), sub_labels
        )

    return my_tree
