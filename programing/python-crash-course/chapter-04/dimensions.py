# # 定义元组
# dimensions = (200, 50)
# print(dimensions[0])        # 200
# print(dimensions[1])        # 50

# # 修改元组中的元素
# dimensions = (200, 50)
# dimensions[0] = 100

# # Traceback (most recent call last):
# #   File "my-python-journey\python-crash-course\chapter-04\dimensions.py", line 8, in <module>
# #     dimensions[0] = 100
# #     ~~~~~~~~~~^^^
# # TypeError: 'tuple' object does not support item assignment

# # 使用 for 循环遍历元组
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# 给元组变量赋值
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)        # 200 50

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)        # 400 100