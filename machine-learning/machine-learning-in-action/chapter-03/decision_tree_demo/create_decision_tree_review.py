import math
import operator

def info_entropy(data_set):
    """
    info_entropy: 计算熵值
    
    :param data_set: 数据集，每一项索引最后一个为数据的标签，其余列为特征
    """
    # 记录每个标签的统计数
    label_count_map = {}
    data_size = len(data_set)
    # 遍历数据集计算每个标签的统计数
    for item in data_set:
        if item[-1] not in label_count_map:
            label_count_map[item[-1]] = 0
        label_count_map[item[-1]] += 1
    # 遍历每个标签，计算熵
    total_info_entry = 0.0
    for count in label_count_map.values():
        probability = float(count / data_size)
        total_info_entry += -(probability * math.log2(probability))

    return total_info_entry


def split_data_by_feature(data_set, axis, value):
    """
    split_data_by_feature: 根据给定特征及特征值对数据集进行拆分
    
    :param data_set: 说明
    :param axis: 说明
    :param value: 说明
    """
    sub_data_set = []
    for item in data_set:
        if item[axis] == value:
            sub_data_set.append(item[:axis] + item[axis+1:])

    return sub_data_set


def calculate_best_feature(data_set):
    """
    calculate_best_feature_to_split: 遍历每个特征，分别计算每个特征分类对应的信息增益，找到最高增益对应的特征索引，其对应最佳分类对应的标签索引
    
    :param data_set: 数据集
    """
    # 原始数据的信息熵，作为计算信息增益的基准
    base_info_entropy = info_entropy(data_set)
    best_info_gain = 0.0
    best_feature_index = -1
    data_size = len(data_set)
    # 特征总数：每个数据长度减一，因为最后一个索引是数据分类，不参与最佳特征的计算
    feature_total = len(data_set[0]) - 1
    # 遍历每个特征，计算每个特征分类对应的信息熵
    for feature_index in range(feature_total):
        # 计算每个特征的总数
        feature_count_map = {}
        for item in data_set:
            feature_value = item[feature_index]
            if feature_value not in feature_count_map:
                feature_count_map[feature_value] = 0
            feature_count_map[feature_value] += 1

        # 计算当前特征的信息熵
        # 当前特征分类获取的信息熵
        feature_info_entropy = 0.0
        # 计算当前特征索引对应的值列表
        feature_value_set = set([item[feature_index] for item in data_set])
        for feature_value in feature_value_set:
            feature_probability = float(feature_count_map[feature_value] / data_size)
            feature_info_entropy += feature_probability * info_entropy(split_data_by_feature(data_set, feature_index, feature_value))

        # 计算当前特征的信息增益
        info_gain = base_info_entropy - feature_info_entropy
        if info_gain > best_info_gain:
            best_feature_index = feature_index
            best_info_gain = info_gain

        return best_feature_index
    

def label_count(class_list):
    """
    label_count: 当只有一个特征时，取标签概率最高的作为分类标签
    
    :param class_list: 说明
    """
    class_count_map = {}
    for item in class_list:
        if item not in class_count_map:
            class_count_map[item] = 0
        class_count_map[item] += 1
    class_sort_list = sorted(class_count_map.items(), key=operator.itemgetter(1), reverse=True)
    return class_sort_list[0][0]

def create_decision_tree(data_set, labels):
    """
    create_decision_tree: 使用递归思想构建决策树进行数据分类
    
    :param data_set: 原始数据集
    :param labels: 每个特征对应标签
    """
    # 如果当前数据集的分类标签只有一个，即全部数据都是一种类别，则不需要递归遍历，就此终止
    class_list = [item[-1] for item in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 如果当前数据项就剩标签数据了，则返回标签数据，同时终止递归
    if len(data_set[0]) == 1:
        return label_count(class_list)
    best_feature = calculate_best_feature(data_set)
    best_label = labels[best_feature]
    classify_tree = {best_label: {}}
    del labels[best_feature]
    best_feature_value_set = set([item[best_feature] for item in data_set])
    for best_feature_value in best_feature_value_set:
        sub_labels = labels[:]
        classify_tree[best_label][best_feature_value] = create_decision_tree(split_data_by_feature(data_set, best_feature, best_feature_value), sub_labels)

    return classify_tree

def create_data_set():
    data_set = [
        [1, 1, 'yes'],
        [1, 1, 'yes'],
        [1, 0, 'no'],
        [0, 1, 'no'],
        [0, 1, 'no'],
    ]
    labels = ['no surfacing', 'flippers']
    return data_set, labels

if __name__ == '__main__':
    data_set, labels = create_data_set()
    print(create_decision_tree(data_set, labels))   # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}