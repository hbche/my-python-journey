import numpy as np

def preprocess(message):
    """
    语料预处理
    """

    words = message.lower().replace('.', ' .').split(' ')
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    corpus = np.array([word_to_id[word] for word in words])

    return corpus, word_to_id, id_to_word
