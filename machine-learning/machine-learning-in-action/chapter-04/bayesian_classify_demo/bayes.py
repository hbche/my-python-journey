def load_data_set():
    post_list = [
        ["my", "dog", "has", "flea", "problems", "help", "please"],
        ["maybe", "not", "take", "him", "to", "dog", "park", "stupid"],
        ["my", "dalmation", "is", "so", "cute", "I", "love", "him"],
        ["stop", "posting", "stupid", "worthless", "garbage"],
        ["mr", "licks", "ate", "my", "steak", "how", "to", "stop", "him"],
        ["quit", "buying", "worthless", "dog", "food", "stupid"],
    ]
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 代表侮辱性文字，0 代表正常言论
    return post_list, class_vec


def create_vocab_list(data_set):
    """
    计算词汇表
    """
    vocab_set = set([])
    # 遍历每个评论，对评论中的每个词进行处理，最终得到一个不重复的词汇表
    for document in data_set:
        vocab_set = vocab_set | set(document)  # 求并集
    return list(vocab_set)
    
    
def set_of_words_to_vec(vocab_list, input_set):
    """
    词集模型
    """
    # 根据词汇表初始化每个词汇的向量值为0，1表示出现过，0表示没出现过
    return_vec = [0] * len(vocab_list)
    for word in input_set:
        if word in vocab_list:
            return_vec[vocab_list.index(word)] = 1
        else:
            print(f"the word: {word} is not in my Vocabulary!")
    return return_vec
    