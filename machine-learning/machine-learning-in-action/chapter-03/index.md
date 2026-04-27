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

在调用函数中调用参数需要满足一定的要求：第一个要求是，数据必须是一种由列表元素组成的列表，而且所有列表元素都要具有相同的数据长度；第二个要求是，数据的最后一列或者每个实例的最后一个元素是当前实例的类别标签。数据集一旦满足上述要求，我们就可以在函数的第一行判定当前数据集包含多少个特征属性。

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

def majority_count(class_list):
    """
    majority_count: 计算分类占比最高的分类

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

以下采用递归的思路实现完整的决策树算法。

```py
def create_decision_tree(data_set, labels):
    class_list = [item[-1] for item in data_set]
    # 如果当前数据的所有标签都是一样的，则不需要再进行分类了
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    # 如果当前只剩标签数据，则取标签占比最高的最为分类标签
    if len(data_set[0]) == 1:
        return majority_count(class_list)
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

上述构建树函数包含两个参数：数据集和标签列表。标签列表包含数据集中所有特征的标签，算法本身不需要这个变量，但是为了给出数据明确的含义，我们将它作为一个输入参数提供。此外，前面提到的对数据集的要求这里依然要满足。上述代码首先创建了名为 class_list 的列表变量，其中包含了数据集所有类标签。递归函数的第一个停止条件是所有的类标签完全相同，则直接返回该标签。递归的第二个终止条件是使用完了所有特征，仍然不能将数据集划分成仅包含唯一类别的分组。由于第二个条件无法简单地返回唯一的类标签，这里使用前面介绍的 majority_count 函数挑选出现次数最多的类别作为返回值。

下一步程序开始构建树，这里使用字典类型保存树的信息。字典变量 classify_tree 存储了树的所有信息，这对于其后绘制树形图非常重要。当前数据集选取的最好特征存储在变量 best_feature_index 中，得到列表包含的所有属性值。然后再根据当前数据源、最佳特征索引、特征值进行子数据集划分，再将子数据集进行树构建。

最后代码遍历当前选择特征包含的所有属性值，在每个数据集划分上递归调用函数 create_decision_tree ，得到的返回值将被插入到字典变量 classify_tree 中，因此函数终止执行时，字典中将会嵌套很多代表叶子节点信息的字典数据。

现在我们可以测试上面代码的实际输出结果：

```py
if __name__ == '__main__':
    data_set, labels = create_data_set()
    print(create_decision_tree(data_set, labels))   # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
```

如果值是类标签，则该子节点是叶子节点；如果值是另一个数据字典，则子节点是一个判断节点，这种结构不断重复就构成了整棵树。

## 3.2 使用 Matplotlib 绘制树形图

使用 Matplotlib 绘制树形图

### 3.2.1 Matplotlib 注释

Matplotlib 提供了一个非常有用的注释工具 annotations，它可以在数据图形上添加文本注释。注释通常用于解释数据的内容。由于数据上面直接存在文本描述会非常丑陋，因此工具内嵌支持带箭头的划线工具。

```py
import matplotlib.pyplot as plt

decision_node = dict(boxstyle='sawtooth', fc='0.8')
leaf_node = dict(boxstyle='round4', fc='0.8')
arrow_args = dict(arrowstyle='<-')

def create_plot():
    fig = plt.figure(1, facecolor='white')
    # 设置中文字体，防止中文乱码
    # Windows 系统使用 'SimHei'（黑体），macOS 使用 'Arial Unicode MS'
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 正常显示中文
    plt.rcParams['axes.unicode_minus'] = False   # 正常显示负号
    fig.clf()
    create_plot.ax1 = plt.subplot(111, frameon=False)
    plot_node('决策节点', (0.5, 0.1), (0.1, 0.5), decision_node)
    plot_node('叶节点', (0.8, 0.1), (0.3, 0.8), leaf_node)
    plt.show()

def plot_node(node_text, center_pt, parent_pt, node_type):
    create_plot.ax1.annotate(node_text, xy=parent_pt, xycoords='axes fraction',
                            xytext=center_pt, textcoords='axes fraction',
                            va='center', ha='center',
                            bbox=node_type, arrowprops=arrow_args)
```

TODO

## 3.3 测试和存储分类器

### 3.3.1 测试算法：使用决策树执行分类

```py
if __name__ == "__main__":
    data_set, label_set = create_data_set()
    decision_tree = create_decision_tree(data_set, label_set[:])
    print(decision_tree)
    # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    classify_result = classify(decision_tree, label_set[:], [1, 0])
    print(classify_result)  # no
    classify_result = classify(decision_tree, label_set[:], [1, 1])
    print(classify_result)  # yes
```

### 3.3.2 使用算法：决策树的存储

构造决策树是很耗时的任务，即使处理很小的数据集，我们可以将训练的决策树对象进行序列化转储，在使用的使用进行反序列化加载，这样就不用每次都计算决策树。

```py
import pickle

def store_decision_tree(decision_tree, filename):
    with open(filename, "wb") as fw:
        pickle.dump(decision_tree, fw)


def grab_decision_tree(filename):
    with open(filename, "rb") as fr:
        return pickle.load(fr)
```

测试：

```py
if __name__ == "__main__":
    data_set, label_set = create_data_set()
    if Path("decision_tree.pkl").exists():
        # 如果存在转储文件，直接解析
        decision_tree = grab_decision_tree("decision_tree.pkl")
    else:
        # 如果不存在则计算并转储，方便下次使用
        decision_tree = create_decision_tree(data_set, label_set[:])
        store_decision_tree(decision_tree, "decision_tree.pkl")
    print(decision_tree)
    # {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
    classify_result = classify(decision_tree, label_set[:], [1, 0])
    print(classify_result)  # no
    classify_result = classify(decision_tree, label_set[:], [1, 1])
    print(classify_result)  # yes
```

通过上述方法我们可以将分类器存储在硬盘上，而不用每次对数据分类时重新学习一遍，这也是决策树的优点之一。k-近邻算法就无法持久化分类器。

## 3.4 示例：使用决策树预测隐形眼镜的种类

步骤：

1. 收集数据
2. 准备数据
3. 分析数据
4. 训练算法
5. 测试算法
6. 使用算法

```py
def get_lenses_data_set():
    data_set = []
    labels = ["age", "prescript", "astigmatic", "tearRate"]
    with open("lenses.txt") as fr:
        for line in fr.readlines():
            line = line.strip().split("\t")
            data_set.append(line)
    return data_set, labels


if __name__ == "__main__":
    # 示例：预测隐形眼镜类型
    data_set, labels = get_lenses_data_set()
    print(data_set, labels)
    decision_tree = create_decision_tree(data_set, labels)
    print(decision_tree)
```

本章使用的是ID3算法实现的决策树，存在过度匹配的问题。后面为了减少过度匹配问题，我们采用剪裁决策树，去掉一些不必要的叶子节点。如果叶子节点只能增加少许信息，则可以删除该节点，将其并入到其他叶子节点中。

后面将学习 CART 算法构造决策树。ID3算法无法直接处理除执行数据，尽管我们可以将数值型数据转换为标称型数据，但是如果存在太多的特征划分，ID3算法仍然会面临其他问题。

## 3.5 本章小结

决策树分类器就像带有终止块的流程图，终止块表示分类结果。开始处理数据集时，我们首先需要测量集合中数据的不一致性（信息熵，越高越混乱），也就是熵，然后寻找最优方案划分数据集，直到数据集中的所有数据属于同一分类。ID3算法可以用于划分标称型数据。构建决策树时，我们通常采用递归方法将数据集转化为决策树。

还有其他的决策树构造算法，最流行的是C4.5和CART。
