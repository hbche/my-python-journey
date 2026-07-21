import numpy as np


def cos_similarity(x, y, eps=1e-8):
    """
    余弦相似度：比较两个单词向量的余弦值
    eps: 是为了防止除数为0的情况
    """
    nx = x / (np.sqrt(np.sum(x**2) + eps))
    ny = y / (np.sqrt(np.sum(y**2) + eps))

    return np.dot(nx, ny)
