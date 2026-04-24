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
