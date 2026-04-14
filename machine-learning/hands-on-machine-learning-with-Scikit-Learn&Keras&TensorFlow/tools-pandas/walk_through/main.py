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

# surprise = pd.Series([1000, 1001, 1002, 1003])
# print(surprise)
# # 0    1000
# # 1    1001
# # 2    1002
# # 3    1003
# # dtype: int64
# surprise_slice = surprise[2:]
# print(surprise_slice)
# # 2    1002
# # 3    1003
# # dtype: int64
# try:
#     surprise_slice[0]
# except KeyError as e:
#     print("Key error: ", e)
# # Key error:  0
# print(surprise_slice.iloc[0])   # 1002

### # 自动对齐
# weight = {"alice": 68, "bob": 83, "colin": 86, "darwin": 68}
# s3 = pd.Series(weight)
# print(s3)
# # alice     68
# # bob       83
# # colin     86
# # darwin    68
# # dtype: int64

# s2 = pd.Series([68, 83, 11, 68], index=['alice', 'bob', 'charles', 'darwin'])
# print(s2)
# # alice      68
# # bob        83
# # charles    11
# # darwin     68
# # dtype: int64

# print(s3.keys())
# # Index(['alice', 'bob', 'colin', 'darwin'], dtype='str')
# print(s2.keys())
# # Index(['alice', 'bob', 'charles', 'darwin'], dtype='str')

# print(s2 + s3)
# # alice      136.0
# # bob        166.0
# # charles      NaN
# # colin        NaN
# # darwin     136.0
# # dtype: float64

# s2 = pd.Series([68, 83, 11, 68], index=['alice', 'bob', 'charles', 'darwin'])
# s5 = pd.Series([1000, 1000, 1000, 1000])
# print("s2=", s2.values)
# # s2= [ 68  83 112  68]
# print("s5=", s5.values)
# # s5= [1000 1000 1000 1000]

# print(s2 + s5)
# # alice     NaN
# # bob       NaN
# # charles   NaN
# # darwin    NaN
# # 0         NaN
# # 1         NaN
# # 2         NaN
# # 3         NaN
# # dtype: float64


# ### # 使用标量初始化
# meaning = pd.Series(42, ['life', 'unverse', 'everything'])
# print(meaning)

# # life          42
# # unverse       42
# # everything    42
# # dtype: int64

# ### # Series name
# s6 = pd.Series([83, 68], index=['bob', 'alice'], name="weights")
# print(s6)

# # bob      83
# # alice    68
# # Name: weights, dtype: int64

### # plot series 对象
# import matplotlib.pyplot as plt
# temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9, 3.5]
# s7 = pd.Series(temperatures, name="Temperature")
# s7.plot()
# plt.show()

## 时间处理

### 时间范围
import matplotlib.pyplot as plt

dates = pd.date_range('2016/10/29 5:30pm', periods=12, freq='h')
temperatures = [4.4, 5.1, 6.1, 6.2, 6.1, 6.1, 5.7, 5.2, 4.7, 4.1, 3.9, 3.5]
temp_series = pd.Series(temperatures, index=dates)
temp_series.plot(kind='bar')

plt.title("Temperature Change Over Time")
plt.xlabel("Date Time")
plt.xticks(rotation=45, ha='right')  # x轴标签倾斜45度，ha='right' 使标签右对齐避免重叠
plt.tight_layout()  # 自动调整子图参数，防止标签被窗口边缘截断
plt.grid(True)
plt.show()