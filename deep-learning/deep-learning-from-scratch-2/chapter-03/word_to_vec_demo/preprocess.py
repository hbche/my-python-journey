import sys

sys.path.append("../..")
from common.util import convert_one_hot, create_contexts_target, preprocess

message = "You say goodbye and i say hello."
corpus, word_to_id, id_to_word = preprocess(message)
contexts, target = create_contexts_target(corpus, len(word_to_id))
vocab_size = len(word_to_id)

contexts = convert_one_hot(contexts, vocab_size)
target = convert_one_hot(target, vocab_size)
