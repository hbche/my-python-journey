import numpy as np
import re

# ------------------------------
# 1. 示例数据集（文档与标签）
# ------------------------------
# 标签：1 表示侮辱性文档，0 表示非侮辱性文档
documents = [
    "You are a fool and stupid.",
    "I love this movie, it's great.",
    "Shut up! You idiot.",
    "This is a wonderful day.",
    "You are so dumb and ugly.",
    "I really enjoy the beautiful sunshine."
]
labels = [1, 0, 1, 0, 1, 0]  # 1: insulting, 0: non-insulting

# ------------------------------
# 2. 文本预处理函数
# ------------------------------
def clean_text(text):
    """
    将文本转为小写，只保留字母和空格（去掉标点符号和数字）
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)   # 去除非字母字符
    text = re.sub(r'\s+', ' ', text).strip() # 合并空白
    return text

def tokenize(text):
    """
    将清理后的文本拆分为单词列表
    """
    return text.split()

# ------------------------------
# 3. 构建词汇表（将所有训练文档中出现的单词收集起来）
# ------------------------------
def build_vocab(documents, labels):
    """
    输入：文档列表（原始字符串）和标签（用于训练，但构建词汇表时不需要标签）
    返回：词汇表（list of unique words）
    """
    vocab_set = set()
    for doc in documents:
        cleaned = clean_text(doc)
        words = tokenize(cleaned)
        vocab_set.update(words)
    return list(vocab_set)

# ------------------------------
# 4. 将文档转换为词频向量（基于词汇表）
# ------------------------------
def doc_to_vector(doc, vocab):
    """
    输入：单个文档（原始字符串）和词汇表（list）
    返回：一维数组，长度=len(vocab)，每个位置是该单词在文档中出现的次数
    """
    vector = np.zeros(len(vocab))
    cleaned = clean_text(doc)
    words = tokenize(cleaned)
    word_to_idx = {word: idx for idx, word in enumerate(vocab)}
    for w in words:
        if w in word_to_idx:
            vector[word_to_idx[w]] += 1
    return vector

# ------------------------------
# 5. 朴素贝叶斯分类器（多项式模型）
# ------------------------------
class NaiveBayesClassifier:
    def __init__(self, alpha=1.0):
        """
        alpha: 拉普拉斯平滑系数，避免概率为零
        """
        self.alpha = alpha
        self.class_prior = {}      # P(c)
        self.cond_prob = {}        # P(word_i | c)
        self.vocab = None
        self.classes = None

    def fit(self, X, y, vocab):
        """
        X: 文档向量矩阵 (n_samples, n_features)
        y: 标签数组 (n_samples,)
        vocab: 词汇表，用于存储特征名称
        """
        self.vocab = vocab
        self.classes = np.unique(y)
        n_samples, n_features = X.shape

        # 计算每个类别的先验概率 P(c)
        for c in self.classes:
            self.class_prior[c] = np.sum(y == c) / n_samples

        # 计算每个类别下每个单词的条件概率 P(word|class)
        # 使用拉普拉斯平滑: (count(word, class) + alpha) / (total_words_in_class + alpha * |V|)
        self.cond_prob = {}
        for c in self.classes:
            # 选出属于该类别的所有文档向量
            X_c = X[y == c]
            # 该类别的总词数（所有文档中词频之和）
            total_words = np.sum(X_c)
            # 统计每个单词在该类别中出现的总次数
            word_counts = np.sum(X_c, axis=0)
            # 计算条件概率（平滑）
            prob = (word_counts + self.alpha) / (total_words + self.alpha * n_features)
            self.cond_prob[c] = prob

    def predict(self, X):
        """
        预测多个文档的类别
        """
        preds = []
        for x in X:
            preds.append(self._predict_one(x))
        return np.array(preds)

    def _predict_one(self, x):
        """
        预测单个文档向量的类别
        使用对数概率以避免下溢
        """
        log_probs = {}
        for c in self.classes:
            # 对数先验
            log_prior = np.log(self.class_prior[c])
            # 对数似然：log(P(x|c)) = sum_i log(P(word_i|c) ** count_i) = sum_i count_i * log(P(word_i|c))
            # 注意：x 是词频向量，可能包含重复的单词（多次出现）
            log_likelihood = np.sum(x * np.log(self.cond_prob[c] + 1e-9))  # 加微小量避免log(0)
            log_probs[c] = log_prior + log_likelihood
        # 返回对数概率最大的类别
        return max(log_probs, key=log_probs.get)

# ------------------------------
# 6. 训练与评估
# ------------------------------
if __name__ == "__main__":
    # 构建词汇表
    vocab = build_vocab(documents, labels)
    print("词汇表大小:", len(vocab))
    print("词汇表示例:", vocab[:10])

    # 将所有文档转换为向量矩阵
    X = np.array([doc_to_vector(doc, vocab) for doc in documents])
    y = np.array(labels)

    # 划分训练集和测试集（简单起见直接用全部数据训练，然后测试）
    # 实际应用中应划分训练/测试集，这里为了演示，我们再做几个新文档预测
    classifier = NaiveBayesClassifier(alpha=1.0)
    classifier.fit(X, y, vocab)

    # 测试新文档
    new_docs = [
        "You are really stupid.",
        "I love you baby.",
        "Shut up and go away!",
        "What a beautiful sunny day."
    ]
    print("\n预测结果：")
    for doc in new_docs:
        vec = doc_to_vector(doc, vocab)
        pred = classifier.predict(np.array([vec]))[0]
        label_str = "侮辱性" if pred == 1 else "非侮辱性"
        print(f"文档: '{doc}' -> 预测类别: {label_str}")

    # 可选：用训练集本身评估准确率（仅演示）
    train_pred = classifier.predict(X)
    accuracy = np.mean(train_pred == y)
    print(f"\n训练集准确率: {accuracy:.2f}")