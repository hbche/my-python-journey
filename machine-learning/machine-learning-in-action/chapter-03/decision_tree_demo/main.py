from create_tree import create_decision_tree


def create_data_set():
    data_set = [
        [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"],
    ]
    labels = ["no surfacing", "flippers"]
    return data_set, labels


# if __name__ == "__main__":
#     data_set, label_set = create_data_set()
#     if Path("decision_tree.pkl").exists():
#         decision_tree = grab_decision_tree("decision_tree.pkl")
#     else:
#         decision_tree = create_decision_tree(data_set, label_set[:])
#         store_decision_tree(decision_tree, "decision_tree.pkl")
#     print(decision_tree)
#     # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
#     classify_result = classify(decision_tree, label_set[:], [1, 0])
#     print(classify_result)  # no
#     classify_result = classify(decision_tree, label_set[:], [1, 1])
#     print(classify_result)  # yes


def get_lenses_data_set():
    data_set = []
    labels = ["age", "prescript", "astigmatic", "tearRate"]
    with open("lenses.txt") as fr:
        for line in fr.readlines():
            line = line.strip().split("\t")
            data_set.append(line)
    return data_set, labels


if __name__ == "__main__":
    # 示例：预测隐形眼镜类型
    data_set, labels = get_lenses_data_set()
    print(data_set, labels)
    decision_tree = create_decision_tree(data_set, labels)
    print(decision_tree)
