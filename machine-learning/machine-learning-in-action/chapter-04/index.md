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

另一种有效计算条件概率的方法称为贝叶斯准则。贝叶斯准则告诉我们如何交换条件概率中的条件和结果，即如果已知 $P(x|c)$，要求$P(c|x)$，那么可以使用下面的计算方法：

$$
p(c|x)=\frac{p(x|c)p(c)}{p(x)}
$$

## 4.3 使用条件概率来分类

贝叶斯决策理论要求计算两个概率 $p1(x,y)$和$p2(x,y)$:

- 如果 $p1(x,y)>p2(x,y)$，那么属于类别1
- 如果 $p2(x,y)>p1(x,y)$，那么属于类别2

我们真正需要计算和比较的是$p(c_1|x,y)$和$p(c_2|x,y)$。这些符号所代表的具体意义是：给定某个由x、y表示的数据点，那么该数据点来自类别$c_1$的概率是多少？数据点来自类别$c_2$的概率又是多少？注意这些概率与概率 $p(x, y|c_1)$ 表示的并不一样，不过可以通过使用贝叶斯准则来交换概率中条件与结果。具体地，应用贝叶斯准测得到：

$$
p(x_i|x,y) = \frac{p(x,y|x_i)p(x_i)}{p(x,y)}
$$

使用这些定义，可以定义贝叶斯分类准则为：

- 如果 $p(c_1|x,y)$ > $p(c_2|x,y)$，那么属于类别$c_1$；
- 如果 $p(c_1|x,y)$ < $p(c_2|x,y)$，那么属于类别$c_2$；

使用贝叶斯准则，可以通过已知的三个概率值来计算未知的概率值。

## 4.4 使用朴素贝叶斯进行文档分类

机器学习的一个重要应用是文档的自动分类。在文档分类中，我们可以观察文档中的词，并把每个词的出现或不出现作为一个特征，这样得到的特征数目就会跟词汇表的词目一样多。

朴素贝叶斯的一般过程：

1. 收集数据：可以使用任何方法。本章使用RSS源。
2. 准备数据：需要数值型或者布尔型数据。
3. 分析数据：又大量特征时，绘制特征作用不大，此时使用直方图效果会更好。
4. 训练算法：计算不同的独立特征的条件概率。
5. 预测算法：计算错误率。
6. 使用算法：一个常见的朴素贝叶斯应用是文档分类。可以在任意的分类场景中使用朴素贝叶斯分类器，不一定非要是文本。

假设词汇表中有1000个单词。要得到好的概率分布，就需要足够的数据样本，假定样本数为N。由统计学知，如果每个特征需要N个样本，那么对于10个特征将需要$N^10$个样本，对于包含1000个特征的词汇表将需要$N^1000$个样本。可以看出，所需的样本数会随着特征数据增大而迅速增长。

如果特征之间相互独立，那么样本数就可以从 $N^1000$ 减少到 $1000xN$。所谓独立指的是统计意义上的独立，即一个特征或者单词出现的可能性与它和其他单词相邻没有关系。举个例子，假设单词 bacon 出现在 unhealthy 后面与出现在 delicious 后面的概率相同。当然，我们知道这种假设不正确，bacon 常常出现在 delicious 后面，而很少出现在 unhealthy 附近，这个假设正是朴素贝叶斯分类器中朴素一次的含义。朴素贝叶斯分类器中的另一个假设是，每个特征同等重要。其实这个假设也有问题。 如果要判断留言板的留言是否得当，那么可能不需要看完所有的1000个单词，而只需要看10～20个特征就足以做出判断了。尽管上述假设存在一些小的瑕疵，但朴素贝叶斯的实际效果却很好。

## 4.5 使用 Python 进行文本分类

要从文本中获取特征，需要先拆分文本。这里的特征是来自文本的词条（token）​，一个词条是字符的任意组合。可以把词条想象为单词，也可以使用非单词词条，如URL、IP地址或者任意其他字符串。然后将每一个文本片段表示为一个词条向量，其中值为1表示词条出现在文档中，0表示词条未出现。

以在线社区的留言板为例。为了不影响社区的发展，我们要屏蔽侮辱性的言论，所以要构建一个快速过滤器，如果某条留言使用了负面或者侮辱性的语言，那么就将该留言标识为内容不当。过滤这类内容是一个很常见的需求。对此问题建立两个类别：侮辱类和非侮辱类，使用1和0分别表示。

接下来首先给出将文本转换为数字向量的过程，然后介绍如何基于这些向量来计算条件概率，并在此基础上构建分类器，最后还要介绍一些利用Python实现朴素贝叶斯过程中需要考虑的问题。

### 4.5.1 准备数据：从文本中构建词向量

我们将把文本看成单词向量或者词条向量，也就是说将句子转换为向量。考虑出现在所有文档中的所有单词，再决定将哪些词纳入词汇表或者说所要的词汇集合，然后必须要将每一篇文档转换为词汇表上的向量。

```py
def load_data_set():
    # 评论列表
    post_list = [
        ["my", "dog", "has", "flea", "problems", "help", "please"],
        ["maybe", "not", "take", "him", "to", "dog", "park", "stupid"],
        ["my", "dalmation", "is", "so", "cute", "I", "love", "him"],
        ["stop", "posting", "stupid", "worthless", "garbage"],
        ["mr", "licks", "ate", "my", "steak", "how", "to", "stop", "him"],
        ["quit", "buying", "worthless", "dog", "food", "stupid"],
    ]
    # 表示每个评论是否出现过侮辱性词汇
    class_vec = [0, 1, 0, 1, 0, 1]  # 1 代表侮辱性文字，0 代表正常言论
    return post_list, class_vec


def create_vocab_list(data_set):
    """
    计算词汇表
    """
    vocab_set = set([])
    # 遍历每个评论，对评论中的每个词进行处理，最终得到一个不重复的词汇表
    for document in data_set:
        # 在数学符号表示上，按位或操作与集合求并操作使用相同记号。
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

前面介绍了如何将一组单词转换为一组数字，接下来看看如何使用这些数字计算概率。现在已经知道一个词是否出现在一篇文档中，也知道该文档所属的类别。还记得4.2节提到的贝叶斯准则？我们重写贝叶斯准则，将之前的x、y替换为w。粗体w表示这是一个向量，即它由多个数值组成。在这个例子中，数值个数与词汇表中的词个数相同。

$$
p(c_i|w)=\frac{p(w|c_i)p(c_i)}{p(w)}
$$

我们将使用上述公式，对每个类计算该值，然后比较这两个概率值的大小。如何计算呢？首先可以通过类别i（侮辱性留言或非侮辱性留言）中文档数除以总的文档数来计算概率p(ci)。接下来计算p(w|ci)，这里就要用到朴素贝叶斯假设。如果将w展开为一个个独立特征，那么就可以将上述概率写作p(w0, w1, w2..wN|ci)。这里假设所有词都互相独立，该假设也称作条件独立性假设，它意味着可以使用 **p(w0|ci)p(w1|ci)p(w2|ci)...p(wN|ci)** 来计算上述概率，这就极大地简化了计算的过程。

该函数的伪代码如下：

```
计算每个类别中文档数目
对每篇训练文档：
    对每个类别：
        如果词条出现在文档中 -> 增加该词条的计数值
        增加所有词条的计数值
对每个类别：
    对每个词条：
        将该词条的数目除以总词条数目得到条件概率
返回每个类别的条件概率
```

我们利用下面的代码来实现上述伪码。打开文本编辑器，将这些代码添加到bayes.py文件中。该函数使用了NumPy的一些函数，故应确保将`from numpy import *`语句添加到bayes.py文件的最前面。

程序清单 4-2 朴素贝叶斯分类器训练函数

```py
def trainNB0(train_matrix, train_category):
    """
    train_matrix: 用于训练的文档对应的词向量矩阵：每一行代表一个文档对应的词向量
    train_category: 训练文档对应的分类列表
    """
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    # 计算含有侮辱性词语的文档对应的概率，即P(c_i)
    p_abusive = np.sum(train_category) / float(num_train_docs)
    # 计算不含侮辱性词语的文档中，对应词向量中每个词汇的总数
    p0_num = np.zeros(num_words)
    # 计算含侮辱性词语的文档中，对应词向量中每个词汇的总数
    p1_num = np.zeros(num_words)
    # 计算不含侮辱性词语文档对应的单词总数
    p0_denom = 0.0
    # 计算含侮辱性词语文档对应的单词总数
    p1_denom = 0.0
    # 遍历每个文档
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += np.sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += np.sum(train_matrix[i])

    # 计算 p(w|c_i)
    p1_vec = p1_num / p1_denom
    p0_vec = p0_num / p0_denom

    return p0_vec, p1_vec, p_abusive
```

### 4.5.3 测试算法：根据显示情况修改分类器

利用贝叶斯分类器对文档进行分类时，要计算多个概率的乘积以获得文档属于哪个类别的概率，即计算 $p(w_0|1)p(w_1|1)p(w_2|1)...p(w_n|1)$。如果其中任意一个概率值为0，那么最后的乘积也为0。为降低这种影响，可以将所有词的出现次数初始化为1，并将分母初始化为2。

优化 trainNB0() :

```py
def trainNB0(train_matrix, train_category):
    """
    train_matrix: 用于训练的文档对应的词向量矩阵：每一行代表一个文档对应的词向量
    train_category: 训练文档对应的分类列表
    """
    num_train_docs = len(train_matrix)
    num_words = len(train_matrix[0])
    # 计算含有侮辱性词语的文档对应的概率，即P(c_i)
    p_abusive = np.sum(train_category) / float(num_train_docs)
    # 计算不含侮辱性词语的文档中，对应词向量中每个词汇的总数，为了避免 p(w_i|c)的概率为零，需要将默认单词个数统计为1
    p0_num = np.ones(num_words)
    # 计算含侮辱性词语的文档中，对应词向量中每个词汇的总数
    p1_num = np.ones(num_words)
    # 计算不含侮辱性词语文档对应的单词总数
    p0_denom = 2.0
    # 计算含侮辱性词语文档对应的单词总数
    p1_denom = 2.0
    # 遍历每个文档
    for i in range(num_train_docs):
        if train_category[i] == 1:
            p1_num += train_matrix[i]
            p1_denom += np.sum(train_matrix[i])
        else:
            p0_num += train_matrix[i]
            p0_denom += np.sum(train_matrix[i])

    # 计算 p(w|c_i)
    p1_vec = p1_num / p1_denom
    p0_vec = p0_num / p0_denom

    return p0_vec, p1_vec, p_abusive
```

另一个遇到的问题是下溢出，这是由于太多很小的数相乘造成的。当计算乘积 $p(w_0|c_i)p(w_1|c_i)...p(w_n|ci)$时，由于大部分因子都非常小，所以程序会下溢出或者得到不正确的答案。一种解决办法是对乘积取自然对数。在代数中有 $ln(a*b)=ln(a)+ln(b)$，于是通过求对数可以避免下溢出或者浮点数舍入导致的错误。同时，采用自然对数进行处理不会有任何损失。下图是函数 f(x) 和 ln(f(x)) 的曲线。检查者两条曲线，就会发现他们在相同作用域内同时增长或减少，并且在相同点上取到极值。他们的取值虽然不同，但不影响最终结果。所以我们将概率计算做如下改动：

```py
# 计算 p(w|c_i)
p1_vec = np.log(p1_num / p1_denom)
p0_vec = np.log(p0_num / p0_denom)
```

上述两个问题解决了，现在已经准备好构建完整的分类器了。

```py
def classifyNB(vec_classify, p0_vec, p1_vec, p_class1):
    # 有对数乘法计算规则，ln(a*b) = ln(a) + ln(b) 得到 p(W|c_i)p(c_i) = ln(p(W|c_i)p(c_i)) = ln(p(W|c_i)) + ln(p(c_i))
    p1 = np.sum(vec_classify * p1_vec) + np.log(p_class1)
    p0 = np.sum(vec_classify * p0_vec) + np.log(p_class1)
    if p1 > p0:
        return 1
    else:
        return 0
```

上述代码完成了最终的分类逻辑，写下来我们来写一个测试：

```py
def testing_nb():
    doc_list, label_list = load_data_set()
    vocab_list = create_vocab_list(doc_list)
    # 将训练文档转换为 词汇表矩阵
    doc_matrix = []
    for doc in doc_list:
        doc_matrix.append(set_of_words_to_vec(doc, vocab_list))
    # 根据文档矩阵和分类标签列表计算 在对应分类条件下所有单词的概率以及各个分类的概率
    p0, p1, p_class1 = trainNB0(doc_matrix, label_list)
    test_doc_0 = ["love", "my", "dalmation"]
    # 计算当前文档的分类
    doc_0_class = classifyNB(
        set_of_words_to_vec(test_doc_0, vocab_list), p0, p1, p_class1
    )
    print(f"{test_doc_0} classified as: {doc_0_class}")
    # ['love', 'my', 'dalmation'] classified as: 0

    test_doc_1 = ["stupid", "garbage"]
    doc_1_class = classifyNB(
        set_of_words_to_vec(test_doc_1, vocab_list), p0, p1, p_class1
    )
    print(f"{test_doc_1} classified as: {doc_1_class}")
    # ['stupid', 'garbage'] classified as: 1
```

接下来，我们会对代码做些修改，是分类器工作得更好。

### 4.5.4 准备数据：文档词袋模型

目前为止，我们将每个词的出现与否作为一个特征，这可以被描述为词集模型（set-of-words model）​。如果一个词在文档中出现不止一次，这可能意味着包含该词是否出现在文档中所不能表达的某种信息，这种方法被称为词袋模型（bag-of-words model）​。在词袋中，每个单词可以出现多次，而在词集中，每个词只能出现一次。为适应词袋模型，需要对函数setOfWords2Vec()稍加修改，修改后的函数称为bagOfWords2Vec()。

下面的程序清单给出了基于词袋模型的朴素贝叶斯代码。它与函数setOfWords2Vec()几乎完全相同，唯一不同的是每当遇到一个单词时，它会增加词向量中的对应值，而不只是将对应的数值设为1。

```py
def bag_of_words_to_vec(doc, vocab_list):
    """
    使用词袋模型，将文档转换为向量
    """
    bag_vec = [0] * len(vocab_list)
    for vocab in vocab_list:
        if vocab in doc:
            bag_vec[vocab_list.index(vocab)] += 1
        else:
            print(f"the word: {vocab} is not in my Vocabulary!")
    return bag_vec
```

现在分类器已经构建好了，下面我们将利用该分类器来过滤垃圾邮件。

### 4.5.5 对文本进行多分类

前面讲述的是基于文档是否含有侮辱性词语这种二分类问题进行解决的，接下来，我们假设文档分类存在多个分类，我们将编写代码实现多分类的场景：

``` py

```

## 4.6 示例：使用朴素贝叶斯过滤垃圾邮件