# 第一章 引言

## 1.1 第一个应用：鸢尾花分类

### 1.1.1 初始数据

加载 scikit-learn 库的鸢尾花数据集。

``` py
from sklearn.datasets import load_iris

iris_dataset = load_iris()
print(f"Keys of iris_dataset:\n{iris_dataset.keys()}")  # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
```

| 字段名称      | 说明                                                                               | 值类型     |
| ------------- | ---------------------------------------------------------------------------------- | ---------- |
| DESCR         | 描述信息                                                                           | 字符串     |
| target_names  | 花的种类                                                                           | 字符串列表 |
| feature_names | 对每一个特征进行说明                                                               | 字符串列表 |
| target        | 数据集                                                                             |            |
| data          | 花萼长度、花萼宽度、花瓣长度、花瓣宽度的测量数据；每一行代表一朵花的四个维度的数据 | NumPy数组  |

``` py
from sklearn.datasets import load_iris

iris_dataset = load_iris()
print(f"Keys of iris_dataset:\n{iris_dataset.keys()}")  # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])

# 描述
print(iris_dataset['DESCR'][:193] + '\n...')

# 花的品种
print(f"Target names: {iris_dataset['target_names']}")  
# Target names: ['setosa' 'versicolor' 'virginica']

print(f"Feature names: \n{iris_dataset['feature_names']}")
# Feature names:
# ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

print(f"Type of data: {type(iris_dataset['data'])}")
# Type of data: <class 'numpy.ndarray'>

print(f"Shape of data: {iris_dataset['data'].shape}")
# Shape of data: (150, 4)
```

机器学习中的个体叫作样本(sample)，其属性叫作特征(feature)。data数组的形状(shape)是样本数乘以特征数。这是scikit-learn中的约定，你的数据形状应始终遵循这个约定。下面给出前5个样本的特征数值:

``` py
print(f"First five rows of data:\n{iris_dataset['data'][:5]}")
# First five rows of data:
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]]
```

target包含测量过的每朵花的品种，也是一个NumPy数组：

``` py
print(f"Type of target: {type(iris_dataset['target'])}")
# Type of target: <class 'numpy.ndarray'>

print(f"Shape of target: {iris_dataset['target'].shape}")
# Shape of target: (150,)
```

上述数字的代表含义由iris['target_names']数组给出：0代表setosa,1代表versicolor,2代表virginica。

### 1.1.2 衡量模型是否成功：训练数据和测试数据

我们不能将用于构建模型的数据用于评估模型。因为我们的模型会一直记住整个训练集，所以对于训练集中的任何数据点总会预测正确的标签。这种“记忆”无法告诉我们模型的泛化(generalize)能力如何（换句话说，在新数据上能否正确预测）​。

我们要用新数据来评估模型的性能。新数据是指模型之前没有见过的数据，而我们有这些新数据的标签。通常的做法是将收集好的带标签数据（此例中是150朵花的测量数据）分成两部分。一部分数据用于构建机器学习模型，叫作训练数据(training data)或训练集(training set)。其余的数据用来评估模型性能，叫作测试数据(test data)、测试集(test set)或留出集(hold-out set)。

scikit-learn中的train_test_split函数可以打乱数据集并进行拆分。这个函数将75%的行数据及对应标签作为训练集，剩下25%的数据及其标签作为测试集。训练集与测试集的分配比例可以是随意的，但使用25%的数据作为测试集是很好的经验法则。

对数据调用train_test_split，并对输出结果采用下面这种命名方法：

``` py
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")
# X_train shape: (112, 4)
# y_train shape: (112,)
# X_test shape: (38, 4)
# y_test shape: (38,)
```

### 1.1.3 要事第一：观察数据

使用散点矩阵图可视化数据特征：

``` py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import mglearn

iris_dataset = load_iris()

X_train,X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
# 利用 X_train 中的数据创建DataFrame
# 利用 iris_dataset.feature_names中的字符串对数据列进行标记
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# 利用 DataFrame 创建散点矩阵图
grr = pd.plotting.scatter_matrix(
    iris_dataframe, 
    c=y_train, 
    figsize=(15, 15), 
    marker='o', 
    hist_kwds={'bins': 20}, 
    s=60, 
    alpha=0.8, 
    cmap=mglearn.cm3
    )
plt.show()
```