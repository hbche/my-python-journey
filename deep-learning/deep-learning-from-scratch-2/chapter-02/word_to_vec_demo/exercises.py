import numpy as np


def preprocess(message):
    words = message.lower().replace(".", " .").split(" ")
    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    # 将语句映射成词汇ID列表
    corpus = np.array([word_to_id[word] for word in words])

    return corpus, word_to_id, id_to_word


def create_vovab_matrix(corpus, vocab_size, windows_size=1):
    # 生成词汇矩阵，初始值都为0
    corpus_size = len(corpus)
    # 类似一个空白的字典， corpus 类似一个记录词汇页码的索引
    vo_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)
    # 我们根据语句来跟新字典
    for i, word_id in enumerate(corpus):
        for idx in range(1, windows_size + 1):
            left_idx = i - idx
            if left_idx >= 0:
                vo_matrix[word_id, corpus[left_idx]] += 1
            right_idx = i + idx
            if right_idx < corpus_size:
                vo_matrix[word_id, corpus[right_idx]] += 1

    return vo_matrix


def cross_similarity(x, y, eps=1e-7):
    nx = x / np.sqrt(np.sum(x**2) + eps)
    ny = y / np.sqrt(np.sum(y**2) + eps)

    return np.dot(nx, ny)


# def most_similarity(query, word_to_id, vo_matrix, top=5):
#     if query not in word_to_id:
#         print(f"{query} not found.")
#         return
#     word_size = len(word_to_id)
#     for i in range(word_size):


if __name__ == "__main__":
    message = "You say boodbye and i say hello."
    corpus, word_to_id, id_to_word = preprocess(message)
    print(corpus)
    print(word_to_id)
    print(id_to_word)
    vo_matrix = create_vovab_matrix(corpus, len(word_to_id), windows_size=1)
    print(vo_matrix)
    similarity = cross_similarity(
        vo_matrix[word_to_id["i"]], vo_matrix[word_to_id["you"]]
    )
    print(similarity)
