import math


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
