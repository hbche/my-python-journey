from bayes import create_vocab_list, load_data_set

if __name__ == "__main__":
    data_set, class_vec = load_data_set()
    vocab_list = create_vocab_list(data_set)
    print(vocab_list)
    # result = set_of_words_to_vec(vocab_list, data_set[3])
    # print(result)
