# 第 3 章 决策树

## 3.1 决策树的构造

优点：计算复杂度不高，输出结果易于理解，对中间值的缺失不敏感，可以处理不相关特征数据。

缺点：可能会产生过度匹配问题。

使用数据类型：数值型和标称型。

在构造决策树时，首先需要解决的问题是，当前数据集上哪个特征在划分数据分类时起决定性作用。为了找到决定性特征，划分最好的结果，我们必须评估每个特征。

决策树的一般流程：

1. 收集数据
2. 准备数据：树构造算法只适用于标称型数据，因此数值型数据必须离散化。
3. 分析数据：可以使用任何方法，构造树完成之后，我们应该检查图形是否符合预期。
4. 训练算法：构造树的数据结构
5. 测试算法：使用经验树测算错误率
6. 使用算法：此步骤适用于任何监督学习算法，而使用决策树可以更好地理解数据的内在含义。

每次我们划分数据集时只选择一个特征属性，如果训练集中存在20个特征，第一次我们选择哪个特征值作为划分的参考属性呢？在回答这个问题这个问题之前，我们必须采用量化的方法判断如何划分数据。

### 3.1.1 信息增熵

划分数据集的大原则是：将无序数据变得更加有序。组织杂乱无章数据的一种方法就是使用信息论度量信息，信息论是量化处理信息的分支科学。

在划分数据集之前和之后信息发生的变化称为信息增益，知道如何计算信息增益，我们就可以计算每个特征值划分数据集获得的信息增益，获得信息增益最高的特征就是最好的选择。

集合信息的度量方式称为香浓熵或者简称为熵。

熵定义为信息的期望值，在明晰这个概念之前，我们必须知道信息的定义。如果待分类的事务可能划分在多个分类之中，则符号$x_i$的信息定义为：

$$
I(x_i)=-\log_{2}{p(x_i)}
$$

其中 $p(x_i)$是选择该分类的概率。

为了计算熵，我们需要计算所有类别所有可能值包含的信息期望值，通过下面公式得到，其中n为分类的数目：

$$
H=\sum_{i=1}^{n}p(x_i)(-\log_{2}{p(x_i)})
$$

下面我们使用 Python 计算信息熵：

```py
def information_entropy(data_set):
    """
    计算数据集的信息熵：H=\sum_{i=1}^{n}p(x_i)(-\log_{2}{p(x_i)})
    """
    # 数据集总数
    data_size = len(data_set)
    # 各个标签对应的数目
    label_count_map = {}
    for item in data_set:
        current_label = item[-1]
        if current_label not in label_count_map:
            label_count_map[current_label] = 1
        else:
            label_count_map[current_label] += 1
    entropy = 0.0
    for label, count in label_count_map.items():
        # 计算每个 特征 的概率
        label_probability = float(count / data_size)
        entropy += -(label_probability * math.log2(label_probability))
    return entropy
```

下面我们来创建一组数据集来测试上面的熵计算：

```py
from information_entropy import information_entropy

def create_data_set():
    data_set = [
        [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"],
    ]
    labels = ["no surfacing", "flippers"]
    return data_set, labels


if __name__ == "__main__":
    data_set, label_set = create_data_set()
    print(data_set)
    result = information_entropy(data_set)
    print(result)   # 0.9709505944546686
```

熵越高，则混合的数据也越多，我们可以在数据集中添加更多的分类，观察熵是如何变化的。我们增加第三个名为 "maybe" 的分类，测试熵的变化：

```py
from information_entropy import information_entropy

def create_data_set():
    data_set = [
        [1, 1, "maybe"],  # [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"],
    ]
    labels = ["no surfacing", "flippers"]
    return data_set, labels


if __name__ == "__main__":
    data_set, label_set = create_data_set()
    print(data_set)
    result = information_entropy(data_set)
    print(result)   #1.3709505944546687
```

得到熵之后，我们可以按照获得最大信息增益的方法划分数据集了。

另一种度量集合无序程度的方法是基尼不纯度，简单来说就是从一个数据集中随机选取子项，度量其被错误分类到其他分组里的概率。

### 3.1.2 划分数据集

我们将对每个特征划分数据集的结果计算一次信息熵，然后判断按照哪个特征划分数据集时最好的划分方式。

```py
def split_data_set(data_set, axis, value):
    """
    根据给定的数据集、分类特征及特征值来划分数据
    """
    # 由于 list 类型是引用传递，所以需要重新生成列表，不可对原始 data_set 进行修改，否则会影响原始数据集
    rest_data_set = []
    for item in data_set:
        if item[axis] == value:
            rest_item = item[:axis] + item[axis + 1 :]
            rest_data_set.append(rest_item)
    return rest_data_set
```

测试：

```py
from split_data_set import split_data_set

def create_data_set():
    data_set = [
        [1, 1, "yes"],
        [1, 1, "yes"],
        [1, 0, "no"],
        [0, 1, "no"],
        [0, 1, "no"],
    ]
    labels = ["no surfacing", "flippers"]
    return data_set, labels


if __name__ == "__main__":
    data_set, label_set = create_data_set()
    result = split_data_set(data_set, 0, 1)
    print(result)
    result = split_data_set(data_set, 0, 0)
    print(result)
```

接下来我们将遍历整个数据集，循环计算数据熵和 `split_data_set()`，找到最好的特征划分方式。熵计算将告诉我们如何划分数据集是最好的数据组织方式。
