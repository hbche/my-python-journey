import numpy as np

def createDataSet():
    group = np.array([
        [1.0, 1.1],
        [1.0, 1.0],
        [0, 0],
        [0, 0.1]
    ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

group, labels = createDataSet()
print(f"Group: {group}")
print(f"Labels: {labels}")

def classify_knn(inX, dataSet, labels, k):
    """
    classify_knn: k近邻算法
    
    :param inX: 输入数据
    :param dataSet: 数据集
    :param labels: 数据集对应的标签
    :param k: 最大近邻数量
    """

    dataSetSize = dataSet.shape[0]
    print(f"dataSetSize: {dataSetSize}")
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    print(f"diffMat: {diffMat}")
    sqDiffMat = diffMat ** 2
    print(f"sqDiffMat: {sqDiffMat}")
    sqDistances = sqDiffMat.sum(axis=1)
    print(f"sqDistances: {sqDistances}")
    distances = sqDistances ** 0.5
    print(f"distances: {distances}")
    sortedDistIndicies = distances.argsort()
    print(f"sortedDistIndicies: {sortedDistIndicies}")
    # classCount = {}

classify_knn([0, 0], group, labels, 3)
    