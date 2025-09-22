# 第 3 章 列表简介

## 3.1 列表是什么

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)     # ['trek', 'cannondale', 'redline', 'specialized']
```

### 3.1.1 访问列表元素

列表是有序集合。

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])      # 访问第一款自行车
```

### 3.1.2 索引从 0 而不是 1 开始

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])      # cannondale
print(bicycles[3])      # specialized
print(bicycles[-1])     # specialized 负数索引表示从列表结尾往前计算，-1表示最有一个元素
```

### 3.1.3 使用列表中的各个值

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
```

## 3.2 修改、添加和删除元素

### 3.2.1 修改列表元素

```python
motorcycles = ["honda", 'yamaha', 'suzuki']
print(motorcycles)          # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'
print(motorcycles)          # ['ducati', 'yamaha', 'suzuki']
```

### 3.2.2 在列表中添加元素

1. 在列表末尾添加元素

```python

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)          # ['honda', 'yamaha', 'suzuki']
```

2. 在列表中插入元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)                # ['ducati', 'honda', 'yamaha', 'suzuki']
```

### 3.2.3 从列表中删除元素

1. 使用 del 语句删除元素

```python
# 使用 del 语句删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)      # 打印删除前的列表
del motorcycles[0]      # 删除 honda
print(motorcycles)      # 打印删除第一个元素后的列表
```

2. 使用 pop() 方法删除元素，同时获取被删除的元素

```python
# 使用pop删除结尾的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)                      # 打印原始列表 ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()    # 调用pop删除结尾元素，并保存在 poped_motorcycle 变量中
print(motorcycles)                      # 打印删除后的列表 ['honda', 'yamaha']
print(poped_motorcycle)                 # 打印被删除的元素
```

3. 使用 pop(index) 方法删除列表中任意位置的元素，同时获取被删除的元素

```python
# 使用pop方法删除指定位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop(1)       # 删除第二个元素，并将值保存在 poped_motorcycle，索引必须小于列表最大索引，可以为负数索引
print(motorcycles)                          # 打印删除后的列表
print(poped_motorcycle)                     # 打印被删除的元素
```

4. 根据元素值删除元素

```python
# 使用remove方法根据元素值删除元素
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)                      # 打印全部列表              ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'                # 定义最贵的摩托车
motorcycles.remove(too_expensive)       # 从列表中删除最贵的摩托车
print(motorcycles)                      # 打印删除之后的元素列表     ['honda', 'yamaha', 'suzuki']
```

> 注意：remove()方法值删除第一个指定的值。如果要删除的值可能在列表中出现多次，就
> 需要使用循环，确保每个值都删除。

## 3.3 管理列表

### 3.3.1 使用 sort()方法对列表进行永久排序

```python
# 使用 sort() 方法对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)         # 打印排序之后的列表 ['audi', 'bmw', 'subaru', 'toyota']
```

还可以按与字母列表相反的顺序排列列表

```python
# 使用与字母顺序相反的顺序排列列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)             # 打印按照字母顺序相反的顺序排列的列表 ['toyota', 'subaru', 'bmw', 'audi']
```

### 3.3.2 使用 sorted() 函数对列表进行临时排序

要保留原始列表，返回排序之后的列表，需要使用 sorted() 函数

```python
# 要保留原始列表，返回排序之后的列表，需要使用 sorted() 函数
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars)
print(cars)             # 打印原始列表      ['bmw', 'audi', 'toyota', 'subaru']
print(sorted_cars)      # 打印排序之后的列表 ['bmw', 'audi', 'toyota', 'subaru']
```

> 注意：`sorted()` 是函数，不是方法，所以不能写成 `list.sorted()`，必须是
> `sorted(list)`

同理，如果需要让 sorted 函数倒序排列列表，需要传入 `reverse=True` 参数

```python
# 使用 sorted 函数倒序排列列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars = sorted(cars, reverse=True)
print(cars)             # 打印原始列表          ['bmw', 'audi', 'toyota', 'subaru']
print(sorted_cars)      # 打印排序之后的列表    ['toyota', 'subaru', 'bmw', 'audi']
```

### 3.3.3 反转列表

要反转列表的排列顺序，可以使用 reverse 方法

```python
# 使用 reverse() 方法反转列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)             # 打印原始列表 ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()          # 反转列表
print(cars)             # 打印反转之后的列表 ['subaru', 'toyota', 'audi', 'bmw']
```

### 3.3.4 获取列表长度

可以使用 len 函数获取列表长度。

```python
# 使用 len 函数获取列表长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))        # 打印原始列表长度 4
del cars[-1]            # 删除最后一个元素
print(len(cars))        # 打印列表长度 3
cars.pop(-2)            # 删除倒数第二个元素
print(len(cars))        # 打印列表长度 2
cars.insert(1, 'subaru')# 在索引为1的位置插入一个元素
print(len(cars))        # 打印列表长度 3
```

## 3.4 使用列表时避免索引错误

使用索引访问列表元素时，如果索引超过列表 长度 - 1 ，就会存在溢出情况。

```python
# 使用列表是避免索引出错
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars[4])
# Traceback (most recent call last):
#   File "\my-python-journey\python-crash-course\chapter-03\cars.py", line 41, in <module>
#     print(cars[4])
#           ~~~~^^^
# IndexError: list index out of range
```

## 3.5 小结

1. 列表是什么、如何访问列表元素
2. 操作列表：增删改、永久排序、临时排序、反转列表、获取列表长度
3. 避免索引错误
