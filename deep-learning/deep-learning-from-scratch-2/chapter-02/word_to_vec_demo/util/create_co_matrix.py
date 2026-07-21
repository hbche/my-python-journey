import numpy as np


def create_co_matrix(corpus, voc_size, window_size=1):
    """
    创建共现矩阵：根据当前语料对应的ID列表，统计当前单词左右窗口范围内的单词总数
    """
    co_matrix = np.zeros((voc_size, voc_size), dtype=np.int32)
    corpus_size = len(corpus)

    for idx, word_id in enumerate(corpus):
        for index in range(1, window_size + 1):
            left_index = idx - index
            right_index = idx + index

            if left_index >= 0:
                left_word_id = corpus[left_index]
                co_matrix[word_id, left_word_id] += 1
            if right_index < corpus_size:
                right_word_id = corpus[right_index]
                co_matrix[word_id, right_word_id] += 1

    return co_matrix
