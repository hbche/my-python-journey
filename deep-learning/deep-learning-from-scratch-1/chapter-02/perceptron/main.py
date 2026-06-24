# 实现感知机
import numpy as np


def and_logic(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def not_and_logic(x1, x2):
    """
    与非门
    """
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def or_logic(x1, x2):
    """
    或门
    """
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    if np.sum(w * x) + b <= 0:
        return 0
    else:
        return 1


def not_or_logic(x1, x2):
    s1 = not_and_logic(x1, x2)
    s2 = or_logic(x1, x2)
    return and_logic(s1, s2)


if __name__ == "__main__":
    input_data = [
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1],
    ]

    and_result = [and_logic(x1, x2) for [x1, x2] in input_data]
    print(and_result)
    # [0, 0, 0, 1]
    not_and_result = [not_and_logic(x1, x2) for [x1, x2] in input_data]
    print(not_and_result)
    # [1, 1, 1, 0]
    or_result = [or_logic(x1, x2) for [x1, x2] in input_data]
    print(or_result)
    # [0, 1, 1, 1]
    not_or_result = [not_or_logic(x1, x2) for [x1, x2] in input_data]
    print(not_or_result)
    # [0, 1, 1, 0]
