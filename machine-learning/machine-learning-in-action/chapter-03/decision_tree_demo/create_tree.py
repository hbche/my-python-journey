# 回顾本章学习的知识点

from calculate_best_feature_split import calculate_best_feature_split
from major_count import major_count
from split_data_set import split_data_set


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
        return major_count(class_list)

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
