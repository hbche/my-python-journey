from create_set import shuffle_and_split_data
from load_data import load_housing_data

housing = load_housing_data()
# 添加一个索引列
housing_with_id = housing.reset_index()
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
train_set, test_set = shuffle_and_split_data(housing_with_id, 0.2)
# train_set, test_set = shuffle_and_split_data(housing, 0.2)
print(test_set)


# # 通过 describe() 方法获取数字特征的描述信息
# print(housing.describe())

# # 通过 value_counts()获取某个属性不重复的值的总数，即类别总数
# print(housing["ocean_proximity"].value_counts())

# ocean_proximity
# <1H OCEAN     9136
# INLAND        6551
# NEAR OCEAN    2658
# NEAR BAY      2290
# ISLAND           5
# Name: count, dtype: int64

# # 获取数据的描述信息
# print(housing.info())
# # 使用head方法查看前5行数据
# print(housing.head())
