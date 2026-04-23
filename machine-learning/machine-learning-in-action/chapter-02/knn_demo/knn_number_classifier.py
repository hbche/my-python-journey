from os import listdir
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from knn import classifyKNN

def plot_number(number_matrix: np.ndarray) -> None:
    """显示单个数字图像。

    Args:
        number_matrix: 32x32 二值图像矩阵。
    """
    plt.imshow(number_matrix, cmap='binary')
    plt.show()

def image_to_vector(filename: str) -> np.ndarray:
    """将 32x32 文本数字图像转换为 1x1024 向量。

    Args:
        filename: 图像文件路径，文件内容为 32 行 32 列的 '0'/'1' 字符。

    Returns:
        1x1024 的 NumPy 向量。
    """
    image_vector = np.zeros((1, 1024), dtype=int)
    with open(filename, 'r') as fr:
        for i in range(32):
            line_str = fr.readline().strip()
            for j in range(32):
                image_vector[0, 32 * i + j] = int(line_str[j])
    return image_vector

def handle_writing_number_classifier():
    label_set = []
    training_file_list = listdir('digits/trainingDigits')
    data_size = len(training_file_list)
    data_set = np.zeros((data_size, 1024))
    for i in range(data_size):
        file_name_str = training_file_list[i]
        number_label = int(file_name_str.split('.')[0].split('_')[0])
        label_set.append(number_label)
        data_set[i, :] = image_to_vector(f'digits/trainingDigits/{file_name_str}')

    test_file_list = listdir('digits/testDigits')
    errorCount = 0.0
    test_data_size = len(test_file_list)
    for i in range(test_data_size):
        file_name_str = test_file_list[i]
        test_label = int(file_name_str.split('.')[0].split('_')[0])
        test_vector = image_to_vector(f'digits/testDigits/{file_name_str}')
        test_target = classifyKNN(test_vector, data_set, label_set, 3)
        print(f'The classifier came back with: {test_target}, the real answer is: {test_label}')
        if test_target != test_label:
            errorCount += 1.0
    print(f"\nThe total number of errors is: {errorCount}")
    print(f"\nThe total error rate is: {errorCount/float(test_data_size)}")

if __name__ == '__main__':
    # number_vector = image_to_vector('digits/trainingDigits/0_13.txt')
    # plot_number(number_vector.reshape((32, 32)))

    handle_writing_number_classifier()