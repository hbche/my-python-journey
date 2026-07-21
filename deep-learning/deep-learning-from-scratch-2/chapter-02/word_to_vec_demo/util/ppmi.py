import numpy as np


def ppmi(C, verbose=False, eps=1e-8):
    """
    将共现矩阵C转换为PPMI矩阵
    """
    # 初始化PPMI矩阵
    M = np.zeros_like(C, dtype=np.float32)
    # 统计共现矩阵中单词出现的总次数
    N = np.sum(C)
    # 计算在共现矩阵中每个单词单独出现的总次数
    S = np.sum(C, axis=0)
    cnt = 0
    total = C.shape[0] * C.shape[1]

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi = np.log((C[i, j] * N) / (S[j] * S[i]) + eps)
            M[i, j] = max(0, pmi)

            if verbose:
                cnt += 1
                if cnt % (total // 100 + 1) == 0:
                    # 打印进度
                    print("%.1f%% done") % (100 * cnt / total)

    return M
