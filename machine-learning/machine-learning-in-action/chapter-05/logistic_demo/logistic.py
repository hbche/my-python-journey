import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    """sigmoid函数"""
    return 1.0 / (1 + np.exp(-x))


def plot_sigmoid(range: list[float]) -> None:
    """
    使用指定范围绘制sigmoid图像
    """

    import matplotlib.pyplot as plt
    import numpy as np

    x = np.arange(range[0], range[1], 0.1)
    y = sigmoid(x)

    plt.plot(x, y)
    plt.title("Sigmoid Function")
    plt.xlabel("x")
    plt.ylabel("sigmoid(x)")
    plt.grid()
    plt.show()


def load_data_set(file_name: str) -> tuple[list[list[float]], list[float]]:
    """
    加载数据集
    """
    data_matrix: list[list[float]] = []
    label_matrix: list[float] = []
    with open(file_name) as fr:
        lines = fr.readlines()
        for line in lines:
            data_list = line.strip().split("\t")
            # 为了便于计算系数，在特征向量的索引为0的位置添加了一个1.0特征值
            data_matrix.append([1.0, float(data_list[0]), float(data_list[1])])
            label_matrix.append(float(data_list[2]))
    return data_matrix, label_matrix


def gradient_descent(
    data_matrix_in: list[list[float]], label_matrix_in: list[float]
) -> np.matrix:
    """
    梯度上升算法
    """
    data_matrix = np.matrix(data_matrix_in)
    # 转置，从行向量转换成列向量
    label_matrix = np.matrix(label_matrix_in).transpose()
    max_cycles = 500
    step = 0.001
    m, n = data_matrix.shape
    # 创建权重列向量
    weights = np.ones((n, 1))
    # 根据给定遍历次数，计算每次权重对应的预测值
    for i in range(max_cycles):
        h = sigmoid(data_matrix * weights)
        # 计算标签值与预测值之间的误差
        error = label_matrix - h

        # 根据梯度上升公式更新权重: w = w + α * X^T * error
        # data_matrix.transpose() * error 衡量每个特征对预测误差的贡献度。某个特征值越大且对应的误差越大，该特征的权重就需要更大幅度的调整。这正是梯度上升中梯度 ∂L/∂w = X^T(y - h) 的矩阵形式。
        weights = weights + step * data_matrix.transpose() * error
    return np.array(weights).flatten()


def random_gradient_descent(data_matrix: list[list[float]], label_matrix: list[float]):
    """
    随机梯度上升算法
    """
    m, n = np.shape(data_matrix)
    step = 0.01
    weights = np.ones(n)
    for i in range(m):
        h = sigmoid(data_matrix[i] * weights)
        error = label_matrix[i] - h
        weights = weights + step * error * data_matrix[i]
    return weights
