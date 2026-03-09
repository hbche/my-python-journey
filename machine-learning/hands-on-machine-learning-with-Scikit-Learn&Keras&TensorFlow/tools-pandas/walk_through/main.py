import pandas as pd

# series_data = pd.Series([2, -1, 3, 5])
# print(series_data)
# # 0    2
# # 1   -1
# # 2    3
# # 3    5
# # dtype: int64

# print(np.exp(series_data))
# # 0      7.389056
# # 1      0.367879
# # 2     20.085537
# # 3    148.413159
# # dtype: float64

# print(series_data + [1000, 2000, 3000, 4000])
# # 0    1002
# # 1    1999
# # 2    3003
# # 3    4005
# # dtype: int64

# print(series_data + 1000)
# # 0    1002
# # 1     999
# # 2    1003
# # 3    1005
# # dtype: int64

# print(series_data < 0)
# # 0    False
# # 1     True
# # 2    False
# # 3    False
# # dtype: bool

# s2 = pd.Series([68, 83, 112, 68], index=["alice", "bob", "charles", "darwin"])
# print(s2)
# alice       68
# bob         83
# charles    112
# darwin      68
# dtype: int64

# # 通过索引访问数据
# print(s2["bob"])    # 83
# print(s2.loc["bob"])    # 使用标签索引
# print(s2.iloc[1])       # 使用整数索引

# # 切片操作
# print(s2.iloc[1:3])
# # bob         83
# # charles    112
# # dtype: int64

surprise = pd.Series([1000, 1001, 1002, 1003])
print(surprise)
# 0    1000
# 1    1001
# 2    1002
# 3    1003
# dtype: int64
surprise_slice = surprise[2:]
print(surprise_slice)
# 2    1002
# 3    1003
# dtype: int64
try:
    surprise_slice[0]
except KeyError as e:
    print("Key error: ", e)
# Key error:  0
print(surprise_slice.iloc[0])   # 1002
