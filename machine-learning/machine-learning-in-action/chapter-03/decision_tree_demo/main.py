# from information_entropy import information_entropy
from split_data_set import split_data_set

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
    result = split_data_set(data_set, 0, 1)
    print(result)
    result = split_data_set(data_set, 0, 0)
    print(result)
