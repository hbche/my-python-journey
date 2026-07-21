import numpy as np
from util.cos_similarity import cos_similarity


def most_similar(query, word_to_id, id_to_word, word_matrix, top=5):
    """
    查找与 query 相似度最高的前 top 个单词
    """
    # 取出查询词
    if query not in word_to_id:
        print(f"{query} not exists.")
        return
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]

    # 计算余弦相似度
    vocab_size = len(id_to_word)
    simarity_list = np.zeros(vocab_size)
    for i in range(vocab_size):
        simarity_list[i] = cos_similarity(word_matrix[i], query_vec)

    # 基于余弦相似度，按降序输出值
    count = 0
    for i in (-1 * simarity_list).argsort():
        if i == query_id:
            continue
        print(f"{id_to_word[i]}: {simarity_list[i]}")
        count += 1
        if count >= top:
            return
