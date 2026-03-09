# 第 2 章 端到端机器学习项目

本章要完成的主要步骤：
1. 放眼大局
2. 获取数据
3. 探索和可视化数据以获得见解
4. 为机器学习算法准备数据
5. 选择一个模型并训练它
6. 微调模型
7. 展示解决方案
8. 发布、监控和维护

## 2.1 使用真实数据

流行的开放数据存储库：
- [OpenML.org](https://www.openml.org/)
- Kaggle.com
- PapersWithCode.com
- Uc Irvine Machine Learning

## 2.2 放眼大局

## 2.3 获取数据

### 2.3.5 下载数据

编写程序获取房屋真实数据：

``` py
import tarfile
import urllib.request
from pathlib import Path
import pandas as pd


def load_housing_data():
    """
    获取房屋数据集
    """
    tarball_path = Path("datasets/housing.tgz")
    # 如果本地datasets文件夹下没有没有housing.tgz压缩包，则会从github请求
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        # urlretrieve是urllib模块的一个核心函数，专门用于从指定的URL地址下载文件并直接保存到本地文件系统。
        urllib.request.urlretrieve(url, tarball_path)
    with tarfile.open(tarball_path) as housing_tarball:
        # extractall方法新增了一个filter参数，用于指定提取策略
        # data 过滤器会忽略许多UNIX文件系统/归档格式的专有特性，适合纯粹的数据提取场景
        # tar 过滤器模拟GUN tar 行为，保留更多类UNIX的我呢间系统特性
        # full_trusted过滤器是完全信任归档文件
        # 我们此处只为提取数据，所以只需要使用 data 过滤器即可
        housing_tarball.extractall(path="datasets", filter="data")
        # 使用pandas读取csv文件，返回DataFrame结构
    return pd.read_csv(Path("datasets/housing/housing.csv"))
```

### 2.3.6 快速浏览数据结构

DataFrame的head()方法可以查看前5行数据：

``` py
housing = load_housing_data()
# 使用head方法查看前5行数据
print(housing.head())
```

info() 方法对于获取数据的快速描述很有用，特别是总行数、每个属性的类型和非空值的数量：

``` py
housing = load_housing_data()
# 获取数据的描述信息
print(housing.info())
```

获取某个特征的类别：

``` py
housing = load_housing_data()
# 通过 value_counts()获取某个特征不重复的值的总数，即类别总数
print(housing["ocean_proximity"].value_counts())
```
输出结果如下：

``` shell
ocean_proximity
<1H OCEAN     9136
INLAND        6551
NEAR OCEAN    2658
NEAR BAY      2290
ISLAND           5
Name: count, dtype: int64
```

可以使用describe()方法显示数字特征的摘要：

``` py
housing = load_housing_data()
# 通过 describe() 方法获取数字特征的描述信息
print(housing.describe())
```

另一种快速了解我们正在处理数据类型的方法是针对每个特征绘制直方图：

``` py
from pathlib import Path

import matplotlib.pyplot as plt
from load_data import load_housing_data

IMAGES_PATH = Path() / "images" / "end_to_end_project"
IMAGES_PATH.mkdir(parents=True, exist_ok=True)


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    """
    保存可视化结果
    """
    path = IMAGES_PATH / f"{fig_id}.{fig_extension}"
    if tight_layout:
        # 如果紧凑布局的话，需要调用plt调整其布局为紧凑布局
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)


# 可视化数据集

plt.rc("font", size=14)
plt.rc("axes", labelsize=14, titlesize=14)
plt.rc("legend", fontsize=14)
plt.rc("xtick", labelsize=10)
plt.rc("ytick", labelsize=10)

housing = load_housing_data()
# 绘制每个特征值的直方图
# bins 用户控制直方图中每组，如果该参数为整数，表示将最大值到最小值这个范围均分成多少个区间；也可以设置为列表或数组，表示非均分区间；还可以设置为字符串，用于指定内置的分区策略。此处50，表示均分区间为50等份
# figsize 指定每个图形的宽高，为坐标轴、标签、图例等所有图形元素提供布局空间，本例中创建宽度为12英尺，高度为8英尺的图形画布。实际屏幕上展示的图形尺寸还需要结合DPI进行计算，即实际渲染的宽高为figsize * DPI
housing.hist(bins=50, figsize=(12, 8))
save_fig("attributes_histogram_plots")
plt.show()
```

### 2.3.7 创建测试集

创建测试集在理论上很简单，随机选择一个实例，通常是数据集的20%，然后将它们放在一边：

``` py
import numpy as np
import pandas as pd


def shuffle_and_split_data(data: pd.DataFrame, test_ratio: float):
    """
    清洗数据并分出训练集和测试集
    """
    # 根据data生成与其索引对应的随机索引列表
    shuffle_indices = np.random.permutation(len(data))
    # 计算测试集的大小
    test_set_size = int(len(data) * test_ratio)
    # 计算测试集对应的索引列表
    test_indices = shuffle_indices[:test_set_size]
    # 计算训练集对应的索引列表
    train_indices = shuffle_indices[test_set_size:]
    # 获取训练集数据和测试集数据
    # 切记：DataFrame.iloc不是方法
    return data.iloc[train_indices], data.iloc[test_indices]
```

| 函数                       | 描述                                                                                                                                                                                     | 示例                                                                                                        |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| numpy.random.permutation() | 接收一个整数，生成一个 np.range(n) 的随机列表<br/>接收一个列表或元组时，返回一个元素顺序被随机打乱后的新列表或元组，原始数据保持不变<br/>针对多为列表，permutation仅打乱第一个维度的数据 | permutation(5)会返回一个类似 [2, 0, 3, 1, 4] 的数组<br/>permutation([1, 2, 3])会返回一个类似[2, 1, 3]的列表 |
| numpy.random.shuffle()     | 与permutation类似，但是shuffle会修改原始列表                                                                                                                                             | xxx                                                                                                         |

> 注意：pandas.DataFrame.iloc不是方法

我们发现，上述随机分组函数存在一个问题，每次调用时，都会重新分组。我们有两种解决办法，一种是将随机分组数据保存，后续加载本地数据；另一种是在随机分组前，指定随机种子，确保每次随机结果都是一样的。

但是这两种方案都无法避免后续新增数据集时，获取更新的数据集还保持一致。一个常见的解决方案是依赖每个实例的唯一标识符来决定它是否应该进入测试集。例如，我们可以计算每个实例标识符的哈希值，当该哈希值低于或等于最大实例标识符哈希值的20%时，将其纳入测试集中，可确保测试集在多次运行随机分组之后仍能保持一致，且在新增实例数据的时候也不影响先前的随机分组。

``` py
def is_id_in_test_set(identifier, test_ratio):
    return crc32(np.int64(identifier) < test_ratio * 2 ** 32)


def split_data_with_id_hash(data, test_ratio, id_column):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: is_id_in_test_set(id_, test_ratio))
    return data.loc[-in_test_set], data.loc[in_test_set]
```

| 函数名     | 描述                                                                                                                   | 示例                    |
| ---------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| zlib.crc32 | CRC 循环冗余校验。接收一个字节数据，生成一个32位的无符号整数作为校验和。主要用作数据完整性验证、压缩文件校验、网络协议 | crc32(b"Hello, World~") |

我们的房屋数据没有唯一标识，我们也不能将实例的索引作为唯一标识符，因为如果中间删除了实例或者新增了实例，都会影响索引，我们需要确保唯一标识永远不改变。基于实例的特征，我们可以结合房屋的经纬度生成唯一标识：

``` py

```