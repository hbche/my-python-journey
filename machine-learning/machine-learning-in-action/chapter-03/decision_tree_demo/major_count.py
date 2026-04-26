import operator

def major_count(class_list):
    """
    major_count: 计算分类占比最高的分类
    
    :param class_list: 分类列表
    """
    class_count_map = {}
    for item in class_list:
        if item not in class_count_map:
            class_count_map[item] = 0
        class_count_map[item] += 1
    sorted_class_count_map = sorted(class_count_map.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count_map[0][0]