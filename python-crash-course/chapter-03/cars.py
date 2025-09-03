# # 使用 sort() 方法对列表永久排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)         # 打印排序之后的列表 ['audi', 'bmw', 'subaru', 'toyota']

# # 使用与字母顺序相反的顺序排列列表
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort(reverse=True)
# print(cars)             # 打印按照字母顺序相反的顺序排列的列表 ['toyota', 'subaru', 'bmw', 'audi']

# # 要保留原始列表，返回排序之后的列表，需要使用 sorted() 函数
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# sorted_cars = sorted(cars)
# print(cars)             # 打印原始列表      ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted_cars)      # 打印排序之后的列表 ['bmw', 'audi', 'toyota', 'subaru']

# # 使用 sorted 函数倒序排列列表
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# sorted_cars = sorted(cars, reverse=True)
# print(cars)             # 打印原始列表          ['bmw', 'audi', 'toyota', 'subaru']
# print(sorted_cars)      # 打印排序之后的列表    ['toyota', 'subaru', 'bmw', 'audi']

# # 使用 reverse() 方法反转列表
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)             # 打印原始列表 ['bmw', 'audi', 'toyota', 'subaru']
# cars.reverse()          # 反转列表
# print(cars)             # 打印反转之后的列表 ['subaru', 'toyota', 'audi', 'bmw']

# # 使用 len 函数获取列表长度
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(len(cars))        # 打印原始列表长度 4
# del cars[-1]            # 删除最后一个元素
# print(len(cars))        # 打印列表长度 3
# cars.pop(-2)            # 删除倒数第二个元素
# print(len(cars))        # 打印列表长度 2
# cars.insert(1, 'subaru')# 在索引为1的位置插入一个元素
# print(len(cars))        # 打印列表长度 3

# 使用列表是避免索引出错
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars[4])
# Traceback (most recent call last):
#   File "\my-python-journey\python-crash-course\chapter-03\cars.py", line 41, in <module>
#     print(cars[4])
#           ~~~~^^^
# IndexError: list index out of range
