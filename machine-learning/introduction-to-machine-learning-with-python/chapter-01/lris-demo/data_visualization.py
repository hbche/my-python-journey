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