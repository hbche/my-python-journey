import matplotlib.pyplot as plt
import numpy as np
from util.create_co_matrix import create_co_matrix
from util.ppmi import ppmi
from util.preprocess import preprocess

if __name__ == "__main__":
    message = "You say goodbye and i say hello."
    corpus, word_to_id, id_to_word = preprocess(message)
    C = create_co_matrix(corpus, len(word_to_id))
    W = ppmi(C)
    U, S, V = np.linalg.svd(W)

    np.set_printoptions(precision=3)  # 有效位数为3位
    print("covariance matrix")
    print(C)
    print("-" * 50)
    print("PPMI")
    print(W)
    print("-" * 50)
    print("SVD")
    print(U)

    print(C[0])
    print(W[0])
    print(U[0])

    print(U[0, :2])

    for word, word_id in word_to_id.items():
        plt.annotate(word, (U[word_id, 0], U[word_id, 1]))

    plt.scatter(U[:, 0], U[:, 1], alpha=0.5)
    plt.show()
