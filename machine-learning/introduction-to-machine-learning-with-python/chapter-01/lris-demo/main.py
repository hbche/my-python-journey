from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

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

print(f"First five rows of data:\n{iris_dataset['data'][:5]}")
# First five rows of data:
# [[5.1 3.5 1.4 0.2]
#  [4.9 3.  1.4 0.2]
#  [4.7 3.2 1.3 0.2]
#  [4.6 3.1 1.5 0.2]
#  [5.  3.6 1.4 0.2]]

print(f"Type of target: {type(iris_dataset['target'])}")
# Type of target: <class 'numpy.ndarray'>

print(f"Shape of target: {iris_dataset['target'].shape}")
# Shape of target: (150,)

print(f"Target: \n{iris_dataset['target']}")
# Target:
# [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
#  0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
#  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
#  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
#  2 2]

X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
print(f"X_train shape: {X_train.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_test shape: {y_test.shape}")