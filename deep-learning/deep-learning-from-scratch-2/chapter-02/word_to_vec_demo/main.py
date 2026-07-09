import sys

sys.path.append("../../")
from common.util import create_co_matrix, most_similarity, preprocess

message = "You say goodbye and i say hello."
corpus, word_to_id, id_to_word = preprocess(message)
co_matrix = create_co_matrix(corpus, vocab_size=len(word_to_id))
most_similarity("you", word_to_id, id_to_word, co_matrix, top=5)
# [query] you
# goodbye, 0.7071067758832467
# hello, 0.7071067758832467
# i, 0.7071067758832467
# and, 0.0
# say, 0.0
