# from sigmoid import plot_sigmoid
import matplotlib.pyplot as plt
import numpy as np
from logistic import gradient_descent, load_data_set, random_gradient_descent


def plot_classify_line(
    data_set: list[list[float]], label_set: list[float], weights: np.ndarray
) -> None:
    print(weights)
    print(weights.shape)
    n = len(label_set)
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in range(n):
        if label_set[i] == 1.0:
            x1.append(data_set[i][1])
            y1.append(data_set[i][2])
        else:
            x2.append(data_set[i][1])
            y2.append(data_set[i][2])
    plt.scatter(x1, y1, s=30, c="red", marker="s")
    plt.scatter(x2, y2, s=30, c="green")
    x = np.arange(-3.0, 3.0, 0.1)
    # y = (-weights[0])
    # y = w0 + w1x1 + w2x2 -> x2 = (-w0-w1x1)/w2
    y = (-weights[0] - weights[1] * x) / weights[2]
    print(x, y)
    plt.plot(x, y)
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()


if __name__ == "__main__":
    data_set, labels = load_data_set("test_set.txt")
    weights1 = gradient_descent(data_set, labels)
    weights2 = random_gradient_descent(data_set, labels)
    print(weights2)
    plot_classify_line(data_set, labels, weights2)
