# 第 3 章 决策树

一句话理解：我们每天都在用决策树

早上起床，我们决定穿什么衣服：

```
外面下雨吗？
  ├── 是 → 温度低于 15°C 吗？
  │        ├── 是 → 穿厚外套
  │        └── 否 → 穿薄外套 + 带伞
  └── 否 → 温度高于 25°C 吗？
           ├── 是 → 穿短袖
           └── 否 → 穿长袖
```

这就是一棵决策树。每次选择一个问题（特征）来问，根据答案走向不同分支，最终做出决定（类别）。 机器学习中的决策树，核心问题就是：机器如何自动学会"该先问哪个问题"？

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

每次我们划分数据集时只选择一个特征属性，如果训练集中存在 20 个特征，第一次我们选择哪个特征值作为划分的参考属性呢？在回答这个问题之前，我们必须采用量化的方法判断如何划分数据。

### 3.1.1 信息增熵

假设我们的数据如下：

| 不露出水面能生存 | 有脚蹼    | 是鱼吗 |
| ---------------- | --------- | ------ |
| 1（是）          | 1（有）   | yes    |
| 1（是）          | 1（有）   | yes    |
| 1（是）          | 0（没有） | no     |
| 0（不能）        | 1（有）   | no     |
| 0（不能）        | 1（有）   | no     |

问题是：先按"不露出水面能否生存"划分，还是先按"有脚蹼"划分？ 哪种顺序能让决策树更短、更准？

**直觉**：一堆样本混在一起分不清，叫"混乱"；如果能清晰地分开，叫"纯净"。

- 5 条数据全是 "yes" → 完全不混乱，熵 = 0
- 3 条 yes + 2 条 no → 有一点混乱
- 各一半 → 最混乱，熵最大

我们把“混乱程度”变成了一个数字，这个数字就是“熵”。

划分数据集的大原则是：将无序数据变得更加有序。组织杂乱无章数据的一种方法就是使用信息论度量信息，信息论是量化处理信息的分支科学。

在划分数据集之前和之后信息发生的变化称为**信息增益**，知道如何计算信息增益，我们就可以计算每个特征值划分数据集获得的信息增益，获得信息增益最高的特征就是最好的选择。

集合信息的度量方式称为香浓熵或者简称为熵。

熵定义为信息的期望值，在明晰这个概念之前，我们必须知道信息的定义。如果待分类的事务可能划分在多个分类之中，则符号$x_i$的信息定义为：

$$
I(x_i)=-\log_{2}{p(x_i)}
$$

其中 $p(x_i)$是选择该分类的概率。

为了计算熵，我们需要计算所有类别所有可能值包含的信息期望值，通过下面公式得到，其中 n 为分类的数目：

$$
H=\sum_{i=1}^{n}p(x_i)I(x_i) = \sum_{i=1}^{n}p(x_i)(-\log_{2}{p(x_i)})=-\sum_{i=1}^{n}p(x_i)\log_{2}p(x_i)
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

熵越高，则混合的数据也越多，也就越混乱，不利于分类，我们可以在数据集中添加更多的分类，观察熵是如何变化的。我们增加第三个名为 "maybe" 的分类，测试熵的变化：

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

**直觉**：每个特征，我们都希望它能最大限度地减少混乱。

- 划分前的熵：当前数据有多混乱
- 划分后的熵：根据指定特征分类之后，每个分支平均有多乱
- 信息增益 = 划分前 - 划分后

增益越大，说明这个特征越有“分辨力”，越应该优先问。

以我们的数据为例：

- 按"不露出水面能否生存"划分：第 1、2、3 条 → 一边（2 yes 1 no），第 4、5 条 → 另一边（全是 no）。混乱明显减少，增益大。
- 按"有脚蹼"划分：4 条去一边（2 yes 2 no），1 条去另一边。几乎还是一半一半，增益小。

我们将对每个特征划分数据集的结果计算一次信息熵，然后判断按照哪个特征划分数据集时最好的划分方式。

首先我们实现数据集按照指定特征和特征值分组的实现：

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

接下来我们将遍历整个数据集，循环计算信息熵和 `split_data_set()`，找到最好的特征划分方式。熵计算将告诉我们如何划分数据集是最好的数据组织方式。

```py
from information_entropy import information_entropy
from split_data_set import split_data_set

def calculate_best_feature_split(data_set):
    # 特征总数
    feature_total = len(data_set[0]) - 1
    # 当前数据集的信息熵
    base_entropy = information_entropy(data_set)
    print(f"Base info entropy: {base_entropy}\n")
    # 最佳信息增益
    best_info_gain = 0.0
    # 最佳特征索引
    best_feature_index = -1
    # 分别计算每个特征划分的信息增益
    for feature_index in range(feature_total):
        # 获取当前特征对应的所有去重之后的值
        feature_values = set([item[feature_index] for item in data_set])
        # 计算当前特征不同值计算出来的熵
        current_entropy = 0.0
        # 遍历当前特征的所有值，根据每个值的占比以及该值分类的数据集的熵，计算当前特征的平均熵
        for feature_value in feature_values:
            # 计算每一个特征分类对应的信息熵
            sub_data_set = split_data_set(data_set, feature_index, feature_value)
            probability = len(sub_data_set) / len(data_set)
            # 子数据集的熵
            current_entropy += probability * information_entropy(sub_data_set)
        # 当前特征所有值产生的信息增益
        info_gain = base_entropy - current_entropy
        print(f"Current feature index is: {feature_index}, current info gain is : {info_gain}\n")
        # 比较当前特征所有值信息增益对信息熵产生的影响，取信息增益最大的特征作为最优分类
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = feature_index
    return best_feature_index
```

测试：

```py
from calculate_best_feature_split import calculate_best_feature_split

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
    best_feature_index = calculate_best_feature_split(data_set)
    print(best_feature_index)
```

### 3.1.3 递归构建决策树

如果划分到最后只剩下标签的时候，并且数据集的特征不止一个的话，我们需要取概率最高的标签作为最终结果。

```py
import operator

def major_count(class_list):
    """
    major_count: 计算分类占比最高的分类

    :param class_list: 分类列表
    """
    class_count_map = {}
    for item in class_list:
        if item not in class_count_map:
            class_count_map[item] = 0
        class_count_map[item] += 1
    sorted_class_count_map = sorted(class_count_map.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_count_map[0][0]
```

前面我们已经构建了“单层”最佳特征计算过程，对于当前最佳特征分类的子集如果还存在多个标签，说明子集也需要按照相同的思路进行特征最优分类计算。

以下采用递归的思路实现完整的策略树算法。

```py
def create_decision_tree(data_set, labels):
    class_list = [item[-1] for item in data_set]
    # 如果当前数据的所有标签都是一样的，则不需要再进行分类了
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 如果当前只剩标签数据，则取标签占比最高的最为分类标签
    if len(data_set[0]) == 1:
        return major_count(class_list)
    # 接下来以递归思想计算每个分支的分类，直到分类完为止
    best_feature_index = calculate_best_feature_to_split(data_set)
    feature_label = labels[best_feature_index]
    # 记录当前分类路径
    classify_tree = {feature_label: {}}
    # 删除当前分类
    del labels[best_feature_index]
    # 遍历当前最佳特征分类的标签，看是否还需要递归分类
    feature_value_set = set([item[-1] for item in data_set])
    for feature_value in feature_value_set:
        sub_labels = labels[:]
        classify_tree[feature_label][feature_value] = create_decision_tree(split_data_set(data_set, best_feature_index, feature_value), sub_labels)

    return classify_tree
```

测试上述测试集：

```py
if __name__ == '__main__':
    data_set, labels = create_data_set()
    print(create_decision_tree(data_set, labels))   # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
```

## 3.2 使用 Matplotlib 绘制树形图
