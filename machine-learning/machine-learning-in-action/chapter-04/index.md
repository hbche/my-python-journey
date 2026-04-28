# 第 4 章 基于概率论的方法：朴素贝叶斯

学习目标：

1. 使用概率分布进行分类
2. 学习朴素贝叶斯分类器
3. 解析 RSS 源数据
4. 使用朴素贝叶斯来分析不同地区的态度

## 4.1 基于贝叶斯决策理论的分类方法

朴素贝叶斯

- 优点：在数据较少的情况下仍能有效，可以处理多类别问题
- 缺点：对于输入数据的准备方式较为敏感。
- 使用数据类型：标称型数据

我们需要了解贝叶斯决策理论，因为其是朴素贝叶斯决策理论的一部分。

选择具有最高概率的决策，这个是贝叶斯决策理论的核心思想。

## 4.2 条件概率

假设有一个箱子，里面装有 7 个球，其中有 3 个灰色的球和 4 个黑色的球，那么抓取灰色球的概率为 $\frac{3}{7}$，抓取黑色球的概率为 $\frac{4}{7}$。

现在我们修改策略，将 7 个球用 A 和 B 两个箱子分装。此时，已知 A 箱子中球的分装情况为 “2 黑 2 灰”，B 箱子中秋的分装情况为 “2 黑 1 灰”。

此时，从 B 箱中抓取灰色球的概率为：$\frac{1}{3}$。这只是直觉上理解来的，具体的计算公式如下：

$$
P(抓取灰色球|在B箱中抓取) = \frac{P(在B箱中抓取灰色球的概率)}{P(在B箱中抓取)}=\frac{\frac{1}{7}}{\frac{3}{7}}=\frac{1}{3}
$$

另一种有效计算条件概率的方法称为贝叶斯准则。贝叶斯准测告诉我们如何交换条件概率中的条件和结果，即如果已知 $P(x|c)$，要求$P(c|x)$，那么可以使用下面的计算方法：

$$
p(c|x)=\frac{p(x|c)p(c)}{p(x)}
$$

## 4.3 使用条件概率来分类

贝叶斯决策理论要求计算两个概率 $p1(x,y)$和$p2(x,y)$:

- 如果 $p1(x,y)>p2(x,y)$，那么属于类别1
- 如果 $p2(x,y)>p1(x,y)$，那么属于类别2

我们真正需要计算和比较的是$p(c_1|x,y)$和$p(c_2|x,y)$。这些符号所代表的具体意义是：给定某个由x、y表示的数据点，那么该数据点来自类别$c_1$的概率是多少？数据点来自雷彪$c_2$的概率又是多少？

## 4.5 使用 Python 进行文本分类

### 4.5.1 准备数据：从文本中构建词向量

```py
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
```

### 4.5.2 训练算法：从词向量计算概率