# 第 6 章 字典

在 Python 中，字典是一种用来存储键值对的数据结构。

## 6.1 一个简单的字典

```python
# 存储特定外星人信息的字典
alien_0 = {
    "color": "green",
    "points": 5
}

print(alien_0["color"])     # 访问字典的 color 键对应的值
print(alien_0["points"])    # 访问字段的 points 键对应的值
```

## 6.2 使用字典

在 Python 中，字典(dictionary)是一系列键值对。每个键都与一个值关联，可以使用键来
访问与之关联的值。与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任意
Python 对象用作字典中的值。

### 6.2.1 访问字典中的值

要获取与键关联的值，可指定字典名并把键放在后面的方括号内

```python
# 存储特定外星人信息的字典
alien_0 = {"color": "green"}
print(alien_0["color"])     # 访问字典的 color 键对应的值
```

### 6.2.2 添加键值对

字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方
括号括起来的键和与该键关联的值。

```python
# 给字典添加键值对
alien_0 = { "color": "green", "points": 5 }
print(alien_0)              # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)              # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
```

### 6.2.3 从创建一个空字典开始

可先使用一对空花括号定义一个空字典，再分行添加各个键值对。

```python
# 从创建一个空字典开始
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)      # {'color': 'green', 'points': 5}
```

### 6.2.4 修改字典中的值

要修改字典中的值，可依次指定字典名、用方括号括起来的键和与该键关联的新值。

```python
# 修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")                  # The alien is green
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")                  # The alien is yellow
```

### 6.2.5 删除键值对

对于字典中不再需要的信息，可使用del语句将相应的键值对彻底删除。在使用del语句时，必须指定字典名和要删除的键。

``` python

```