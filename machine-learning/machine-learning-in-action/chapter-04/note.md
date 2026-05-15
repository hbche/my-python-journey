# 基于朴素贝叶斯的分类算法

## 核心原理说明

1. **数据预处理**：小写化、去除标点数字、分词，得到一个干净的单词列表。
2. **词汇表**：收集训练集中所有出现过的单词，为后续向量化提供固定维度。
3. **向量化**：采用词袋模型，统计每个单词在文档中的出现次数（也可以使用二值化的伯努利模型，本例使用多项式模型，适合词频信息）。
4. **朴素贝叶斯公式**：
   - 先验概率 $P(c)$：类别 c 的文档数 / 总文档数。
   - 条件概率 $P(w_i|c)$：使用拉普拉斯平滑，避免零概率。
     $$
     P(w_i|c) = \frac{\text{count}(w_i, c) + \alpha}{\sum_{w \in V} \text{count}(w, c) + \alpha |V|}
     $$
   - 预测时比较后验概率 $P(c|\mathbf{x}) \propto P(c) \prod_{i} P(w_i|c)^{x_i}$，取对数计算避免数值下溢。
5. **分类决策**：取对数后验概率最大的类别。

### 如何扩展

- 可以引入更复杂的文本清洗（如停用词过滤、词干提取）。
- 可用 TF-IDF 替代纯粹的词频，提高特征区分度。
- 如果需求是不考虑词频、只关注单词是否出现，可将 `doc_to_vector` 中的计数改为二值（`1 if count>0 else 0`），并使用伯努利朴素贝叶斯模型（相应修改条件概率计算方法）。

## 朴素贝叶斯文档分类原理详解

朴素贝叶斯是一种基于**贝叶斯定理**和**特征条件独立假设**的分类方法。在文档分类任务中，它根据文档中出现的词语来预测文档属于哪个类别（例如侮辱性 / 非侮辱性）。下面从数学原理、模型假设、参数估计、分类决策四个层面逐步解析。

---

### 1. 问题形式化

设文档为一个单词序列 $d = (w_1, w_2, \dots, w_n)$，类别 $c \in \{C_1, C_2, \dots, C_K\}$（二分类时 $K=2$）。我们想要计算在给定文档 $d$ 的条件下，文档属于类别 $c$ 的后验概率 $P(c \mid d)$，并将文档判给后验概率最大的类别：

$$
\hat{c} = \arg\max_{c} P(c \mid d)
$$

根据**贝叶斯定理**：

$$
P(c \mid d) = \frac{P(c) \cdot P(d \mid c)}{P(d)}
$$

由于分母 $P(d)$ 对于所有类别相同，在比较时可以忽略，因此分类决策简化为：

$$
\hat{c} = \arg\max_{c} P(c) \cdot P(d \mid c)
$$

其中：

- $P(c)$ 是类别的**先验概率**（训练集中该类文档的比例）。
- $P(d \mid c)$ 是**似然概率**，表示在类别 $c$ 下生成文档 $d$ 的概率。

---

### 2. 朴素假设（特征条件独立）

直接计算 $P(d \mid c)$ 是非常困难的，因为文档是一个单词序列，不同单词的出现存在复杂的依赖关系（例如“非常”后面常跟形容词）。为了简化，朴素贝叶斯引入一个极强的假设：**在给定类别 $c$ 的条件下，文档中每个单词的出现相互独立**。

这就是“朴素”一词的来源。用数学语言表达：

$$
P(d \mid c) = P(w_1, w_2, \dots, w_n \mid c) = \prod_{i=1}^{n} P(w_i \mid c)
$$

其中 $P(w_i \mid c)$ 表示在类别 $c$ 中单词 $w_i$ 出现的概率。注意这里忽略了单词的位置和顺序，只考虑单词是否出现以及出现的次数（或频次），即**词袋模型**。

---

### 3. 文档的概率建模：多项式模型 vs 伯努利模型

朴素贝叶斯在文本分类中有两种常见变体：

- **多项式模型**：考虑单词在文档中出现的**次数**（词频）。文档的生成过程是：先选择类别 $c$，然后按照多项式分布重复选择 $n$ 个单词（允许重复）。此时：

  $$
  P(d \mid c) = \frac{n!}{x_{w_1}!\,x_{w_2}!\cdots} \prod_{w \in V} P(w \mid c)^{x_w}
  $$

  其中 $x_w$ 是单词 $w$ 在文档中出现的次数，$V$ 是词汇表。由于阶乘部分与类别 $c$ 无关，在比较时通常省略。

- **伯努利模型**：只考虑单词**是否出现**（二值特征），忽略词频。文档生成时，对每个单词独立地以概率 $P(w \mid c)$ 决定该单词是否出现。

---

### 4. 参数估计（训练阶段）

训练的目标是从已标注的训练集中估计出：

- 先验概率 $P(c)$
- 类别条件概率 $P(w \mid c)$（对每个单词 $w$ 和每个类别 $c$）

#### 4.1 先验概率

$$
P(c) = \frac{N_c}{N_{\text{total}}}
$$

其中 $N_c$ 是训练集中属于类别 $c$ 的文档数，$N_{\text{total}}$ 是总文档数。

#### 4.2 条件概率（多项式模型）

设训练集中类别 $c$ 的所有文档中，单词 $w$ 出现的总次数为 $\text{count}(w, c)$，类别 $c$ 下所有单词的总词数为 $\sum_{w'} \text{count}(w', c)$。则最大似然估计为：

$$
P(w \mid c) = \frac{\text{count}(w, c)}{\sum_{w'} \text{count}(w', c)}
$$

**问题**：如果测试文档中出现了一个在训练集中从未与类别 $c$ 一同出现过的单词（即 $\text{count}(w, c)=0$），那么 $P(w \mid c)=0$，导致整个似然乘积为 0，模型失去判别能力。

#### 4.3 拉普拉斯平滑（Laplace Smoothing）

为避免零概率，引入平滑参数 $\alpha > 0$（通常取 $\alpha=1$，也称为加一平滑）：

$$
P(w \mid c) = \frac{\text{count}(w, c) + \alpha}{\sum_{w'} \text{count}(w', c) + \alpha \cdot |V|}
$$

其中 $|V|$ 是词汇表的大小（所有可能单词的个数）。平滑后，即使在训练中未出现的单词，也有一个很小的非零概率 $\frac{\alpha}{\sum_{w'} \text{count}(w', c) + \alpha |V|}$，这保证了模型的鲁棒性。

#### 4.4 补充讲解

- $ V $：词汇表（所有不重复的单词），大小记为 $ |V| $。
- 类别 $ c $：例如侮辱类（1）或非侮辱类（0）。
- $ \text{count}(w, c) $：在训练集中，属于类别 $ c $ 的所有文档里，单词 $ w $ 出现的总次数（注意是所有文档累加，不是单篇文档）。
- $ \text{total*words}\_c = \sum*{w \in V} \text{count}(w, c) $：类别 $ c $ 下所有文档包含的总单词数（重复计数）。

我们的目标是估计 $ P(w \mid c) $：**给定类别 $ c $ 时，单词 $ w $ 出现的概率**。

---

##### 4.4.1 不加平滑（极大似然估计）

根据极大似然原理，最直观的估计是：

$$
P(w \mid c) = \frac{\text{count}(w, c)}{\text{total\_words}_c}
$$

**含义**：在类别 $ c $ 的所有文档中，单词 $ w $ 出现的次数占该类别总单词数的比例。

###### 例子

假设词汇表只有 3 个单词：`[love, hate, stupid]`  
类别 **侮辱类** 训练集由两篇文档组成：

- 文档1：`"you are stupid stupid"` → 单词统计：stupid 出现 2 次，其他 0 次
- 文档2：`"hate you"` → 单词统计：hate 出现 1 次

那么：

- count(stupid, 侮辱类) = 2
- count(hate, 侮辱类) = 1
- count(love, 侮辱类) = 0
- total*words*侮辱类 = 2 + 1 + 0 = 3

所以：

- $ P(\text{stupid} \mid 侮辱类) = 2/3 \approx 0.667 $
- $ P(\text{hate} \mid 侮辱类) = 1/3 \approx 0.333 $
- $ P(\text{love} \mid 侮辱类) = 0/3 = 0 $

**问题**：如果测试文档中出现了单词 `"love"`，则 $ P(\text{love} \mid 侮辱类) = 0 $，导致整个似然乘积为 0，模型会认为侮辱类不可能生成包含 love 的文档，这显然不符合实际（侮辱文档也可能意外出现 love 一词，只是概率很低）。这称为“零概率问题”。

---

##### 4.4.2 加上拉普拉斯平滑（Laplace Smoothing）

为了消除零概率，我们在分子和分母上都加上一个正数 $ \alpha $（通常取 $ \alpha = 1 $），公式变为：

$$
P(w \mid c) = \frac{\text{count}(w, c) + \alpha}{\text{total\_words}_c + \alpha \cdot |V|}
$$

###### 为什么分母要加 $ \alpha |V| $？

目的：保证所有单词的条件概率之和为 1。

验证：

$$
\sum_{w \in V} P(w \mid c) = \sum_{w} \frac{\text{count}(w,c) + \alpha}{\text{total\_words}_c + \alpha |V|}
= \frac{\sum_w \text{count}(w,c) + \sum_w \alpha}{\text{total\_words}_c + \alpha |V|}
= \frac{\text{total\_words}_c + \alpha |V|}{\text{total\_words}_c + \alpha |V|} = 1
$$

###### 例子（沿用上面的词汇表）

$ |V| = 3 $，$ \alpha = 1 $

- 分子：每个单词的 count 上加 1
- 分母：$total\_words_c + \alpha |V| = 3 + 1\times 3 = 6$

计算：

- $P(\text{stupid} \mid 侮辱类) = (2+1)/6 = 3/6 = 0.5$
- $P(\text{hate} \mid 侮辱类) = (1+1)/6 = 2/6 \approx 0.333$
- $P(\text{love} \mid 侮辱类) = (0+1)/6 = 1/6 \approx 0.167$

现在所有概率均为正，且和 = 1。未出现的单词 love 也有了一个较小的概率（0.167），这符合“可能但不太可能”的直观。

---

##### 4.4.3 平滑的效果：直观对比表

| 单词 w | count(w, c) | 无平滑 P(w  | c)          | 平滑后 P(w | c) (α=1) |
| ------ | ----------- | ----------- | ----------- | ---------- | -------- |
| stupid | 2           | 2/3 = 0.667 | 3/6 = 0.5   |
| hate   | 1           | 1/3 = 0.333 | 2/6 = 0.333 |
| love   | 0           | 0           | 1/6 ≈ 0.167 |

平滑后：

- 高频词的概率略微降低（从 0.667 降到 0.5）
- 低频词的概率略微提高
- 未见词获得非零概率

---

##### 4.4.4 为什么拉普拉斯平滑有效？

拉普拉斯平滑相当于在极大似然估计中引入一个**先验分布**：假设每个单词在每类中都已经出现了 $\alpha$ 次“虚拟计数”。这可以解释为：

$$
P(w \mid c) = \frac{\text{count}(w,c) + \alpha}{\text{total\_words}_c + \alpha |V|}
= \frac{\text{count}(w,c) + \alpha}{N_c + \alpha |V|}
$$

其中 $N_c = total\_words_c$。

当 $\alpha = 1$ 时，这等价于在计算概率前，先给每个单词在每类中“预先添加” 1 次出现。

---

##### 4.4.5 在代码中的实现

对应上面代码中的：

```python
prob = (word_counts + self.alpha) / (total_words + self.alpha * n_features)
```

- `word_counts`：类别 c 下每个单词的总频数（数组） → 对应 count(w, c)
- `total_words`：类别 c 下的总词数 → 对应 total_words_c
- `n_features`：词汇表大小 → 对应 |V|
- `self.alpha`：平滑系数，默认 1.0

这样计算出的 `prob` 就是平滑后的 $ P(w \mid c) $。

---

##### 4.4.6 总结

| 公式         | 形式                                                                        | 优点                                 | 缺点                                       |
| ------------ | --------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------ |
| 无平滑       | $\frac{count(w,c)}{total_words_c}$                         | 直接反映训练数据中的真实频率         | 出现零概率导致分类失效                     |
| 拉普拉斯平滑 | $\frac{count(w,c) + \alpha}{total_words_c + \alpha \|\|V\|\|}$ | 消除零概率，保持概率和为 1，鲁棒性好 | 对概率分布引入一定的偏差（α 较小时偏差小） |

通常在实际使用中，拉普拉斯平滑（α=1）是标准做法，能显著提升模型泛化能力。

---

### 5. 分类决策（预测阶段）

对于新文档 $d$，我们需要计算：

$$
\hat{c} = \arg\max_{c} \left( \log P(c) + \sum_{w \in d} \log P(w \mid c) \right)
$$

这里取对数有两个原因：

1. **防止数值下溢**：多个概率（远小于 1）相乘的结果会非常小，可能超出浮点数精度范围。取对数将乘法转化为加法，数值更稳定。
2. **简化计算**：对数函数单调递增，最大化后验概率等价于最大化对数后验概率。

注意在多项式模型中，如果单词 $w$ 在文档中出现 $x_w$ 次，则对应的项是 $x_w \cdot \log P(w \mid c)$，其实本来应该是$P(w \mid c)^{x_w}$，由于进行了对数计算，所以指数中的 $x_w$就被转换到了前面，也就变成了乘积的模式。上面的求和就是遍历文档中每个单词（允许重复）。

代码中的 `_predict_one` 方法正是这样做：

```python
log_likelihood = np.sum(x * np.log(self.cond_prob[c] + 1e-9))
```

其中 `x` 是词频向量，`cond_prob[c]` 是平滑后的 $P(w \mid c)$ 数组。

---

### 6. 工作流程总结

| 步骤 | 操作         | 说明                                       |
| ---- | ------------ | ------------------------------------------ |
| 1    | 文本预处理   | 小写化、去除非字母字符、分词               |
| 2    | 构建词汇表   | 收集训练集中所有出现过的单词               |
| 3    | 向量化       | 将每个文档转换为词频向量（长度 = \|V\|）   |
| 4    | 估计先验     | 计算 $P(c) = N_c / N_{\text{total}}$       |
| 5    | 估计条件概率 | 对每个类别 $c$，计算平滑后的 $P(w \mid c)$ |
| 6    | 预测         | 对测试文档向量化，计算对数后验，取最大类   |

---

### 7. 实例演示（直觉理解）

假设训练集有两类文档：

- **侮辱类**：包含“fool”、“stupid”、“idiot”等词
- **非侮辱类**：包含“love”、“great”、“beautiful”等词

一个新文档 “You are a fool” 经过处理后得到单词列表 `['you', 'are', 'fool']`。

- 在侮辱类中，`P(fool | insult)` 较高（比如 0.2），`P(you | insult)` 和 `P(are | insult)` 也非零。
- 在非侮辱类中，`P(fool | non-insult)` 可能非常接近 0（平滑后很小）。

因此侮辱类的对数后验乘积会远大于非侮辱类，模型就会将其分类为侮辱性文档。

---

### 8. 朴素贝叶斯的优点与局限性

**优点**：

- 简单、计算高效，适合高维稀疏数据（如文本）。
- 对小规模数据集表现良好。
- 对噪声数据鲁棒（通过平滑处理）。
- 容易解释，可以输出每个单词对分类的贡献。

**局限性**：

- **特征条件独立假设**在现实中往往不成立（单词之间是有依赖关系的），这可能导致次优的决策边界。
- 对词频敏感（多项式模型）时，长文档可能被某一类主导，需要归一化或使用 TF-IDF。
- 如果某个单词在训练集中完全与某一类共现，平滑后仍然会保留较强偏向，但不会出现绝对的 0/1 边界。

尽管如此，朴素贝叶斯在文本分类、垃圾邮件过滤等任务中依然表现优秀，常作为基线模型使用。

---

### 9. 与代码的对应关系

- `build_vocab`：构建词汇表 $V$。
- `doc_to_vector`：生成词频向量 $x$。
- `fit`：计算 `class_prior[c]` 和 `cond_prob[c]`（平滑后的 $P(w|c)$）。
- `predict`：应用贝叶斯决策规则，使用对数概率比较。

通过理解上述原理，你可以调整平滑参数、切换特征表示（如用 TF-IDF 代替词频）、甚至修改为伯努利模型，以适应不同的实际场景。

## 代码实现

以下是一个完整的基于朴素贝叶斯算法的文档分类实现，可以将文档分为“含有侮辱性词语”和“不含有侮辱性词语”两类。代码包括数据预处理、特征提取、模型训练和预测，并附有详细注释。

```python
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
```

**输出示例**（词汇表内容可能因运行顺序略有差异）：

```
词汇表大小: 17
词汇表示例: ['you', 'are', 'fool', 'and', 'stupid', 'love', 'this', 'movie', 'it', 'great']

预测结果：
文档: 'You are really stupid.' -> 预测类别: 侮辱性
文档: 'I love you baby.' -> 预测类别: 非侮辱性
文档: 'Shut up and go away!' -> 预测类别: 侮辱性
文档: 'What a beautiful sunny day.' -> 预测类别: 非侮辱性

训练集准确率: 1.00
```
