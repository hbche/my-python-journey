import numpy as np


def clip_grads(grads, max_norm):
    total_norm = 0
    for grad in grads:
        total_norm += np.sum(grad * grad)
    total_norm = np.sqrt(total_norm)

    rate = max_norm / (total_norm + 1e-6)
    if rate < 1:
        for grad in grads:
            grad *= rate


def preprocess(message):
    """
    将 message 语句转换成语料库
    """
    text = message.lower()
    text = text.replace(".", " .")
    words = text.split(" ")

    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = [word_to_id[word] for word in words]
    corpus = np.array(corpus)

    return corpus, word_to_id, id_to_word


def create_co_matrix(corpus, vocab_size, windows_size=1):
    """
    计算词向量
    corpus：语料库id列表
    vocab_size：词汇数量
    window_size：计算窗口大小
    """
    corpus_size = len(corpus)
    co_matrix = np.zeros((vocab_size, vocab_size), dtype=np.int32)

    for idx, word_id in enumerate(corpus):
        # 以当前遍历的词汇为中心轴，再结合窗口大小，计算当前词汇左右两侧窗口范围内的词汇表
        for i in range(1, windows_size + 1):
            left_idx = idx - i
            right_idx = idx + i
            # 根据语料id列表获取词汇id，根据词汇id更新值
            if right_idx < corpus_size:
                right_word_id = corpus[right_idx]
                co_matrix[word_id, right_word_id] += 1

            if left_idx >= 0:
                left_word_id = corpus[left_idx]
                co_matrix[word_id, left_word_id] += 1

    return co_matrix


def cos_similarity(x, y, eps=1e-8):
    """
    根据余弦相似度计算向量相似度
    x：第一个向量
    y：第二个向量
    eps：防止除数为零
    """
    nx = x / np.sqrt(np.sum(x**2) + eps)  # x 的正则化
    ny = y / np.sqrt(np.sum(y**2) + eps)  # y 的正则化

    return np.dot(nx, ny)


def most_similarity(query, word_to_id, id_to_word, word_matrix, top=5):
    """
    计算给定词汇相似排名前top的词汇
    query: 查询的词
    word_to_id: 单词到单词ID的字典
    id_to_word: 单词ID到单词的字典
    top: 显示到前几位
    """
    # 首先需要保证查询的词汇在我们的语料库中
    if query not in word_to_id:
        print(f"{query} is not found")
        return
    print(f"[query] {query}")
    # 根据语料库将要查询的词汇转换成词汇ID和词汇向量
    query_id = word_to_id[query]
    query_vec = word_matrix[query_id]

    # 获取当前词汇表中词汇量总数，便于接下来遍历
    vocab_size = len(id_to_word)
    # 根据词汇总量初始化词汇相似度列表
    similarity = np.zeros(vocab_size)
    # 遍历语料库
    for i in range(vocab_size):
        # 计算每个语料与查询词汇之间的余弦相似度
        similarity[i] = cos_similarity(word_matrix[i], query_vec)

    count = 0
    # argsort 根据值从大到小排序返回排序之后的索引列表
    for i in (-1 * similarity).argsort():
        # 排除语料库中查询词对应语料的相似度值
        if id_to_word[i] == query:
            continue
        print(f"{id_to_word[i]}, {similarity[i]}")
        count += 1
        if count >= top:
            return


def ppmi(C, verbose=False, eps=1e-8):
    """
    将共现矩阵转换为 PPMI矩阵
    """
    # 初始化 PPMI矩阵
    M = np.zeros_like(C, dtype=np.float32)
    # 计算所有单词的总数
    N = np.sum(C)
    # 计算每个单词出现的次数
    S = np.sum(C, axis=0)
    total = C.shape[0] * C.shape[1]
    cnt = 0

    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
            pmi = np.log((M[i, j] * N) / (S[i] * S[j]) + eps)
            M[i, j] = max(0, pmi)

            if verbose:
                cnt += 1
                if cnt % (total // 100 + 1) == 0:
                    print("%.1f%% done" % (100 * cnt / total))

    return M


def create_contexts_target(corpus, vocab_size, window_size=1):
    """
    根据语料ID列表、词汇量和窗口大小生成每个预料词汇对应的上下文词汇列表和目标词汇
    """
    target = corpus[window_size:-window_size]
    contexts = []

    for idx in range(window_size, len(corpus) - window_size):
        cs = []
        for t in range(-window_size, window_size + 1):
            if t == 0:
                continue
            cs.append(corpus[idx + t])
        contexts.append(cs)

    return np.array(contexts), np.array(target)


def convert_one_hot(corpus, vocab_size):
    """
    one-hoe转换，需要考虑二维场景
    : param corpus:
    : param vocab_size:
    : return: ont-hot 表示
    """
    N = corpus.shape[0]

    if corpus.ndim == 1:
        one_hot = np.zeros((N, vocab_size), dtype=np.int32)
        # 遍历语料中的每个词汇，根据词汇ID更新one
        for idx, word_id in enumerate(corpus):
            one_hot[idx, word_id] = 1

    elif corpus.ndim == 2:
        C = corpus.shape[1]
        one_hot = np.zeros((N, C, vocab_size), dtype=np.int32)
        for idx_0, word_ids in enumerate(corpus):
            for idx_1, word_id in enumerate(word_ids):
                one_hot[idx_0, idx_1, word_id] = 1

    return one_hot
