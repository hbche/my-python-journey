# # 根据索引访问元素
# motorcycles = ["honda", 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# # 在列表结尾处插入新元素
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles)              # ['honda', 'yamaha', 'suzuki']

# # 在指定位置插入元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.insert(0, 'ducati')
# print(motorcycles)                # ['ducati', 'honda', 'yamaha', 'suzuki']

# # 使用 del 语句删除元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)      # 打印删除前的列表
# del motorcycles[0]      # 删除 honda
# print(motorcycles)      # 打印删除第一个元素后的列表

# # 使用pop删除结尾的元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)                      # 打印原始列表 ['honda', 'yamaha', 'suzuki']
# poped_motorcycle = motorcycles.pop()    # 调用pop删除结尾元素，并保存在 poped_motorcycle 变量中
# print(motorcycles)                      # 打印删除后的列表 ['honda', 'yamaha']
# print(poped_motorcycle)                 # 打印被删除的元素

# # 使用pop方法删除指定位置的元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# poped_motorcycle = motorcycles.pop(1)       # 删除第二个元素，并将值保存在 poped_motorcycle
# print(motorcycles)                          # 打印删除后的列表
# print(poped_motorcycle)                     # 打印被删除的元素

# 使用remove方法根据元素值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                      # 打印全部列表              ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'                # 定义最贵的摩托车
motorcycles.remove(too_expensive)       # 从列表中删除最贵的摩托车
print(motorcycles)                      # 打印删除之后的元素列表     ['honda', 'yamaha', 'suzuki']