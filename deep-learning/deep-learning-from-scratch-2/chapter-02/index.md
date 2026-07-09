# 第 2 章 自然语言处理和单词的分布式表示

## 2.1 什么是自然语言处理

简单地说，自然语言处理是一种能够让计算机理解人类语言的技术。换言之，自然语言处理的目标就是让计算机理解人说的话，进而完成对我们有帮助的事情。

首要目标是让计算机理解单词的含义。目前主要有三种方法：

- 基于同义词词典的方法
- 基于计数的方法
- 基于推理的方法

## 2.2 同义词词典

目前被广泛使用的同义词词典，不是像《新华字典》那样解释说明一个词的含义，而是将具有相同含义或含义类似的词归为一组。

另外，在自然语言处理中用到的同义词词典有时会定义单词之间的粒度更细的关系，比如“上位-下位”关系、​“整体-部分”关系。

通过对所有单词创建近义词集合，并用图表示各个单词的关系，可以定义单词之间的联系。利用这个“单词网络”​，可以教会计算机单词之间的相关性。

### 2.2.1 WordNet

在自然语言处理领域，最出名的同义词词典是 WordNet。

### 2.2.2 同义词词典的问题

- 难以顺应时代的变化
- 人力成本高
- 无法表示单词的微妙差异

## 2.3 基于计数的方法

### 2.3.1 基于Python的语料库的预处理

首先我们建立单词与id的关联列表

```py
import re

message = "You say goodbye and i say hello."
words = re.split("\W ?", message.lower())
print(words)
# ['You', 'say', 'goodbye', 'and', 'i', 'say', 'hello', '']
word_to_id = {}
id_to_word = {}

for word in words:
    if word not in word_to_id:
        new_id = len(word_to_id)
        word_to_id[word] = new_id
        id_to_word[new_id] = word

print(word_to_id)
print(id_to_word)
```

接下来，我们生成id列表：

```py
id_list = [word_to_id[word] for word in words]
id_list = np.array(id_list)
```

上述都是预料处理逻辑，我们现在将其封装成函数：

```py
import re

import numpy as np


def preprocess(message):
    """
    将 message 语句转换成语料库
    """

    words = re.split("\\W+", message.lower())
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
```

至此，语料库的预处理就完成了。接下来就是利用语料库提取单词含义。

### 2.3.2 单词的分布式表示

类比RGB格式的颜色，我们将单词转换成向量。将单词领域构建紧凑合理的向量表示，这在自然语言处理领域称为“分布式表示”。

单词的分布式表示将单词表示为固定长度的向量。这种向量的特征在于它是用密集向量表示的。密集向量的意思是，向量的各个元素（大多数）是由非0实数表示的。例如，三维分布式表示是[0.21,-0.45,0.83]​。

### 2.3.3 分布式假设

许多研究表明“某个单词的含义由它周围的单词形成”​，这称为分布式假设（distributional hypothesis）​。

分布式假设所表达的理念非常简单。单词本身没有含义，单词含义由它所在的上下文（语境）形成。的确，含义相同的单词经常出现在相同的语境中。比如“I drink beer.”​“We drink wine.”,drink的附近常有饮料出现。

从现在开始，我们会经常使用“上下文”一词。本章说的上下文是指某个单词（关注词）周围的单词。这里，我们将上下文的大小（即周围的单词有多少个）称为窗口大小（window size）​。窗口大小为1，上下文包含左右各1个单词；窗口大小为2，上下文包含左右各2个单词，以此类推。

这里，我们将左右两边相同数量的单词作为上下文。但是，根据具体情况，也可以仅将左边的单词或者右边的单词作为上下文。此外，也可以使用考虑了句子分隔符的上下文。

### 2.3.4 共现矩阵

下面，我们来考虑如何基于分布式假设使用向量表示单词，最直截了当的实现方法是对周围单词的数量进行计数。具体来说，在关注某个单词的情况下，对它的周围出现了多少次什么单词进行计数，然后再汇总。这里，我们将这种做法称为“基于计数的方法”​，在有的文献中也称为“基于统计的方法”​。

我们还是以 "You say goodbye and i say hello." 为例，基于统计的方法计算每个单词其周围单词出现的次数作为其向量表示。

```py
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
```

无论语料库多大，都可以自动生成共现矩阵。

### 2.3.5 向量间的相似度

前面我们根据共现矩阵将词汇转换成向量。下面我们来看一下如何测量向量间的相似度。

测量向量间的相似度有很多种方法，其中最具代表性的方法有向量内积或欧式距离等。还存在其他很多种方法，但是余弦相似度是很常用的。余弦相似度计算公式如下：

$$
similarity(x, y)=\frac{x \cdot y}{||x||\cdot||y||}=\frac{x_1y_1+...+x_ny_n}{\sqrt{x_1^2+...x_n^2}\sqrt{y_1^2+...y_n^2}}
$$

代码实现：

```py
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
```

我们尝试计算 "i" 和 "you" 这两个单词对应向量的余弦相似度：

```py
import sys

sys.path.append("../../")
from common.util import cos_similarity, create_co_matrix, preprocess

message = "You say goodbye and i say hello."
corpus, word_to_id, id_to_word = preprocess(message)

print(corpus)
print(word_to_id)
print(id_to_word)

co_matrix = create_co_matrix(corpus, vocab_size=len(word_to_id))
print(co_matrix)

word_1 = "i"
word_2 = "you"
x = co_matrix[word_to_id[word_1]]
y = co_matrix[word_to_id[word_2]]
similarity = cos_similarity(x, y)
print(f'The word "{word_1}" and "{word_2}"\'s similarity is {similarity}')
# The word "i" and "you"'s similarity is 0.7071067758832467
```

余弦相似度的值域在 $[-1, 1]$。越趋向于1，向量就越相似。

### 2.3.6 相似单词的排序

接下来我们将计算与给定单词相似度最高的几个单词。

```py
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
    # argsort 根据值从小到大排序返回排序之后的索引列表，此处乘以-1，就转换成了从大到小排序
    for i in (-1 * similarity).argsort():
        # 排除语料库中查询词对应语料的相似度值
        if id_to_word[i] == query:
            continue
        print(f"{id_to_word[i]}, {similarity[i]}")
        count += 1
        if count >= top:
            return
```

下面我们来测试上面的方法：

```py
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
```

## 2.4 基于计数的方法的改进

### 2.4.1 点互信息

上一节的共现矩阵的元素表示两个单词同时出现的次数。但是，这种“原始”的次数并不具备好的性质。如果我们看一下高频词汇（出现次数很多的单词）​，就能明白其原因了。比如，我们来考虑某个语料库中the和car共现的情况。在这种情况下，我们会看到很多“...the car...”这样的短语。因此，它们的共现次数将会很大。另外，car和drive也明显有很强的相关性。但是，如果只看单词的出现次数，那么与drive相比，the和car的相关性更强。这意味着，仅仅因为the是个常用词，它就被认为与car有很强的相关性。

为了解决这一问题，可以使用点互信息（Pointwise Mutual Information, PMI）这一指标。对于随机变量x和y，它们的PMI定义如下：

$$
PMI(x, y)=\log_{2}\frac{P(x, y)}{P(x)P(y)}
$$
