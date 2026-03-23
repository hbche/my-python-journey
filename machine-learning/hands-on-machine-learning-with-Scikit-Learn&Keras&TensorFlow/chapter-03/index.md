# 第 3 章 分类

## 3.1 MNIST

```py
import os
import pickle

import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# sklearn 中存在三类函数：
# fetch_*** 用于获取现实生活中的数据集
# load_*** 用于加载与 scikit-learn 库捆绑的"小玩具"数据集
# make_*** 用于生成假数据集，对于测试很有用


def load_mnist_local(cache_dir="./.mnist_cache", force_download=False):
    """
    加载 MNIST 数据集，支持本地缓存以避免重复下载

    参数:
        cache_dir: 缓存目录路径，默认为当前目录下的.mnist_cache 文件夹
        force_download: 是否强制重新下载，默认 False

    返回:
        包含 data, target, DESCR 属性的对象
    """
    # 创建缓存目录
    os.makedirs(cache_dir, exist_ok=True)
    cache_file = os.path.join(cache_dir, "mnist_784.pkl")

    # 检查缓存是否存在且不需要强制下载
    if os.path.exists(cache_file) and not force_download:
        print(f"从本地缓存加载 MNIST 数据集：{cache_file}")
        with open(cache_file, "rb") as f:
            mnist = pickle.load(f)
    else:
        # 从网络下载
        print("正在从 OpenML 下载 MNIST 数据集...")
        mnist = fetch_openml("mnist_784", as_frame=False)
        # 保存到本地缓存
        with open(cache_file, "wb") as f:
            pickle.dump(mnist, f)
        print(f"数据已缓存到：{cache_file}")

    return mnist


# fetch_openml 默认是以 pandas 的 DataFrame 结构返回数据，针对图像数据不理想，所以我们通过设置 as_frame=False 来设置其返回 NumPy 格式的数据集
mnist = load_mnist_local()
# data: 输入数据
# target: 标签
# DESCR: 数据集的描述
X, Y, desc = mnist.data, mnist.target, mnist.DESCR
# print(X)
print(X.shape)
# (70000, 784) 表明 data 中含有 70000 张包含 784 个特征点的图像数据，784 是有 28 * 28 像素的图片，每个特征点代表 0（白色）~255（黑色）的颜色强度
# print(desc)


# 我们接下来使用 matplotlib 的 imshow 函数展示其中一个数据
def plot_digit(image_data):
    # 将一维 784 特征点的数据转换为 28*28 的矩阵
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    # 隐藏坐标轴
    plt.axis("off")


some_digit = X[0]
digit_label = Y[0]
plot_digit(some_digit)
plt.show()

# 输出：图像的列表标签，验证我们的判断是否正确
print(digit_label)
```


## 3.2 训练二元分类器

我们先从简单分类出发：判断当前图片是否是 "5"。

1. 计算训练数据集和测试数据集
2. 通过随机梯度下降算法计算模型参数值
3. 通过测试集计算模型性能

``` py

```