import numpy as np
import pandas as pd
from zlib import crc32

def is_id_in_set(identifier, ratio):
    return crc32(identifier) <= crc32(ratio * 2 * 32)

# 学习使用numpy.random.permutation、pandas.DataFrame.iloc和对数据进行随机分组
data = [
    [1, "Alice", 25],
    [2, "Bob", 30],
    [3, "Charlie", 35],
    [4, "Sam", 30],
    [5, "Green", 27],
    [6, "Lucy", 24],
    [7, "Lili", 18],
    [8, "Jerry", 32],
    [9, "Tom", 35],
    [10, "Liming", 32],
]
df = pd.DataFrame(data, columns=["ID", "Name", "Age"])
print(type(df))

shuffle_indecies = np.random.permutation(10)
test_indecies = shuffle_indecies[:3]
train_indecies = shuffle_indecies[3:]
print(f"test_indecies: {test_indecies}")
print(f"train_indecies: {train_indecies}")

print(f"df: {df}")
test_datasets = df.iloc[test_indecies]
print(f"test_datasets: {test_datasets}")

# 为了保证每次随机生成的测试集不变，我们需要给每个数据增加一个唯一标识符，再基于该唯一标识符进行随机分组
# 增加 index 列
df_with_id = df.reset_index()
df_with_id['id'] = df_with_id['Name']
