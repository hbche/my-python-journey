from information_entropy import information_entropy
from split_data_set import split_data_set

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
        print(f"Current feature index is: {feature_index}, current info gain is : {current_info_gain}\n")
        # 比较当前特征所有值信息增益对信息熵产生的影响，去最低的信息熵作为最优分类
        if current_info_gain > best_info_gain:
            best_info_gain = current_info_gain
            best_feature_index = feature_index
    # 返回最佳特征索引
    return best_feature_index