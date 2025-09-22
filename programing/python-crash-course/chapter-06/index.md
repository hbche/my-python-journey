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

对于字典中不再需要的信息，可使用 del 语句将相应的键值对彻底删除。在使用 del 语句时，必须指定字典名和要删除的键。

```python
# 删除字典中的键值对
alien_0 = {"color": "green", "points": 5}
print(alien_0)          # {'color': 'green', 'points': 5}
del alien_0['color']
print(alien_0)          # {'points': 5}
```

### 6.2.6 由类似的对象组成的字典

```python
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
```

定义好字典后，在最后一个键值对的下一行添加一个右花括号，并且也缩进 4 个空格，使其与字典中的键对齐。一种不错的做法是，在最后一个键值对后面也加上逗号，为以后添加键值对做好准备。

### 6.2.7 使用 get() 来访问值

使用放在方括号内的键从字典中获取感兴趣的值，可能会引发问题：如果指定的键不存在，就将出错。

```python
# 使用中括号语法访问不存在的键值对
alien_no_points = {
    "color": 'green',
    'speed': 'slow'
    }
print(alien_no_points['points'])
```

这将导致 Python 显示 traceback，指出存在键值错误(KeyError)：

```bash
Traceback (most recent call last):
  File "my-python-journey\python-crash-course\chapter-06\alien_no_points.py", line 6, in <module>
    print(alien_no_points['points'])
          ~~~~~~~~~~~~~~~^^^^^^^^^^
KeyError: 'points'
```

就字典而言，为避免出现这样的错误，可使用 get()方法在指定的键不存在时返回一个默认值。get()方法的第一个参数用于指定键，是必不可少的；第二个参数为当指定的键不存在时要返回的值，是可选的：

```python
# 使用 get() 方法获取不存在的键，并指定默认值
alien_no_points = {
    'color': 'green',
    'speed': 'slow'
    }
print(alien_no_points.get('points', 'No point value assigned.'))        # No point value assigned.
```

如果指定的键有可能不存在，应考虑使用 get()方法，而不要使用方括号表示法。

## 6.3 遍历字典

### 6.3.1 遍历字典的键值对

```python
# 使用 items() 方法遍历字典的键值对
user_0 = {
    'username': 'Robin',
    'first': 'Robin',
    'last': 'Che'
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

### 6.3.2 遍历字典中的所有键

```python
# 遍历字典中所有的key
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
for name in favorite_languages.keys():
    print(name.title())
```

在遍历字典时，会默认遍历所有的键。

```python
for name in favorite_languages.keys():
```

替换为

```python
for name in favorite_languages:
```

如果显式地使用 keys()方法能让代码更容易理解。

```python
# 遍历字典中所有的key
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love {language}.")
```

keys()方法并非只能用于遍历：实际上，它会返回一个列表，其中包含字典中的所有键。

```python
# 遍历字典中所有的key
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")            # Erin, please take our poll!
```

### 6.3.3 按特定的顺序遍历字典中所有的键

遍历字典时将按插入元素的顺序返回其中的元素，但是在一些情况下，你可能要按与此不同的顺序遍历字典。要以特定的顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。

```python
# 按照指定的顺序遍历字典中所有的key
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, please take our poll!")
```

### 6.3.4 遍历字典中的所有值

可使用 values() 方法遍历字典的所有值。

```python
# 遍历字典中所有的值
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
```

可以使用集合进行去重。从已有列表创建集合使用 set() 函数：

```python
# 遍历字典中所有的值
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
```

可以使用一堆花括号直接创建集合：

```bash
>>> languages = {'python', 'c', 'rust', 'python'}
>>> languages
{'python', 'c', 'rust'}
```

集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的很可能是集合。不同于列表和字典，集合不会以特定的顺序存储元素。

## 6.4 嵌套

可以在列表中嵌套字典，在字典中嵌套列表，甚至在字典中嵌套字典。

### 6.4.1 字典列表

```python
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
```

### 6.4.2 在字典中存储列表

```python
# 顾客所点的披萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述顾客所点的披萨
print(f'You ordered a {pizza['crust']}-crust pizza with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')

# You ordered a thick-crust pizza with the following toppings:
#         mushrooms
#         extra cheese
```

### 6.4.3 在字典中存储字典

可以在字典中嵌套字典，但这样可能会让代码很快变得非常复杂。

```python
# 在字典中存储字典
many_users = {
    'robin': {
        'first': 'robin',
        'last': 'che',
        'location': 'Wuhan',
        },
    "sam": {
        'first': 'sam',
        'last': 'alter',
        'location': 'Guangzhou',
        }
    }
for user, info in many_users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['first']} {info['last']}"
    location = info['location']

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
```

## 6.5 小结

1. 如何定义字典
2. 访问和修改字典中的元素
3. 遍历字典
4. 字典中的嵌套
