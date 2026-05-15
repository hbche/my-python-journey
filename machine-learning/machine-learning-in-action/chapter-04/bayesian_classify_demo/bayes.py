import numpy as np


def load_data_set():
    # 评论列表
    post_list = [
        ["my", "dog", "has", "flea", "problems", "help", "please"],
        ["maybe", "not", "take", "him", "to", "dog", "park", "stupid"],
        ["my", "dalmation", "is", "so", "cute", "I", "love", "him"],
        ["stop", "posting", "stupid", "worthless", "garbage"],
        ["mr", "licks", "ate", "my", "steak", "how", "to", "stop", "him"],
        ["quit", "buying", "worthless", "dog", "food", "stupid"],
    ]
    # 表示每个评论是否出现过侮辱性词汇
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 代表侮辱性文字，0 代表正常言论
    return post_list, class_vec


def create_vocab_list(data_list):
    """
    根据给定文档列表，生成词汇表
    """
    vocab_set = set([])
    for document in data_list:
        vocab_set.update(document)
    return list(vocab_set)


def set_of_words_to_vec(doc, vocab_list):
    """
    根据训练数据的词汇表，将输入文档转换为对应的词向量
    """
    # 根据词汇表初始化每个词汇的向量值为0，1表示出现过，0表示没出现过
    return_vec = [0] * len(vocab_list)
    for word in doc:
        if word in vocab_list:
            # 注意：此处是对应文章中当前单词在词汇表中的索引，而不是在文档中的索引
            return_vec[vocab_list.index(word)] = 1
        else:
            print(f"the word: {word} is not in my Vocabulary!")
    return return_vec


def bag_of_words_to_vec(doc, vocab_list):
    """
    使用词袋模型，将文档转换为向量
    """
    bag_vec = [0] * len(vocab_list)
    for vocab in vocab_list:
        if vocab in doc:
            bag_vec[vocab_list.index(vocab)] += 1
        else:
            print(f"the word: {vocab} is not in my Vocabulary!")
    return bag_vec


# p(c_i|w) = p(w|c_i)p(c_i)/p(w)，这里假设所有词都互相独立，该假设也称作条件独立性假设，它意味着可以使用 p(w|c_i)p(c_i) 计算


def trainNB0(train_matrix, train_category):
    """
    train_matrix: 用于训练的文档对应的词向量矩阵：每一行代表一个文档对应的词向量
    train_category: 训练文档对应的分类列表
    """
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    # 计算含有侮辱性词语的文档对应的概率，即P(c_i)
    p_abusive = np.sum(train_category) / float(num_train_docs)
    # 计算不含侮辱性词语的文档中，对应词向量中每个词汇的总数
    p0_num = np.ones(num_words)
    # 计算含侮辱性词语的文档中，对应词向量中每个词汇的总数
    p1_num = np.ones(num_words)
    # 计算不含侮辱性词语文档对应的单词总数
    p0_denom = 2.0
    # 计算含侮辱性词语文档对应的单词总数
    p1_denom = 2.0
    # 遍历每个文档
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += np.sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += np.sum(train_matrix[i])

    # 计算 p(w|c_i)
    p1_vec = np.log(p1_num / p1_denom)
    p0_vec = np.log(p0_num / p0_denom)

    return p0_vec, p1_vec, p_abusive


def classifyNB(vec_classify, p0_vec, p1_vec, p_class1):
    # 有对数乘法计算规则，ln(a*b) = ln(a) + ln(b) 得到 p(W|c_i)p(c_i) = ln(p(W|c_i)p(c_i)) = ln(p(W|c_i)) + ln(p(c_i))
    p1 = np.sum(vec_classify * p1_vec) + np.log(p_class1)
    p0 = np.sum(vec_classify * p0_vec) + np.log(p_class1)
    if p1 > p0:
        return 1
    else:
        return 0


def testing_nb():
    doc_list, label_list = load_data_set()
    vocab_list = create_vocab_list(doc_list)
    # 将训练文档转换为 词汇表矩阵
    doc_matrix = []
    for doc in doc_list:
        doc_matrix.append(set_of_words_to_vec(doc, vocab_list))
    # 根据文档矩阵和分类标签列表计算 在对应分类条件下所有单词的概率以及各个分类的概率
    p0, p1, p_class1 = trainNB0(doc_matrix, label_list)
    test_doc_0 = ["love", "my", "dalmation"]
    # 计算当前文档的分类
    doc_0_class = classifyNB(
        set_of_words_to_vec(test_doc_0, vocab_list), p0, p1, p_class1
    )
    print(f"{test_doc_0} classified as: {doc_0_class}")
    # ['love', 'my', 'dalmation'] classified as: 0

    test_doc_1 = ["stupid", "garbage"]
    doc_1_class = classifyNB(
        set_of_words_to_vec(test_doc_1, vocab_list), p0, p1, p_class1
    )
    print(f"{test_doc_1} classified as: {doc_1_class}")
    # ['stupid', 'garbage'] classified as: 1
