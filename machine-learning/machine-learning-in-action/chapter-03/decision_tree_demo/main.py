# from information_entropy import information_entropy
# from split_data_set import split_data_set
# from calculate_best_feature_split import calculate_best_feature_split
# from major_count import major_count
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


if __name__ == "__main__":
    data_set, label_set = create_data_set()
    result = create_decision_tree(data_set, label_set)
    print(result)
    # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}