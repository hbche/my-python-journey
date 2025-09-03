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
print(bicycles[-1])     # specialized
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

```

2. 使用 pop() 方法删除元素

3. 使用 pop(index) 方法删除列表中任意位置的元素
