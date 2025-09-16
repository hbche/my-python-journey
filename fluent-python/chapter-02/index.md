# 第 2 章 序列构成的数组

## 2.1 内置序列类型概览

容器序列：list、tuple 和 collections.deque 这些序列能存放不同类型的数据。

扁平序列：str、bytes、bytearray、memoryview 和 array.array，这类序列只能容纳一种类型。

容器序列存放的是它们所包含的任意类型的对象的引用，而扁平序列里存放的是值而不是引用。

可变序列：list、bytearray、array.array、collections.deque 和 memoryview。

不可变序列：tuple、str 和 bytes

## 2.2 列表推导和生成器表达式

### 2.2.1 列表推导式和可读性

把一个字符串变成 Unicode 码位的列表

```python
# 讲一个字符串转换成Unicode码位的列表
symbols = "$¢£¥€¤"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))

print(codes)            # [36, 162, 163, 165, 8364, 164]
```

使用列表推导式

```python
# 讲一个字符串转换成Unicode码位的列表
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
```

### 2.2.2 列表推导同 filter 和 map 的比较

```python
# 使用列表推导和map/filter组合来创建同样的表单
symbols = '$¢£¥€¤'
beyond = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(beyond)           # [162, 163, 165, 8364, 164]
```

使用 filter 和 map：

```python
# 使用filter和map组合来创建列表
symbols = '$¢£¥€¤'
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(codes)              # [162, 163, 165, 8364, 164]
```

### 2.2.3 笛卡尔积

使用列表推导生成笛卡尔积

```python
# 使用列表推导生成笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# # 先以颜色排序，再以尺寸排序
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
# 先以尺寸排序，再以颜色排序
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)  # [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]
```

### 2.2.4 生成器表达式

用生成器表达式初始化元组和列表

```python
# 使用生成器表达式计算笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ("%s %s" % (c, s) for c in colors for s in sizes):
    print(tshirt)

# black S
# black M
# black L
# white S
# white M
# white L
```

## 2.3 元组不仅仅是不可变的列表
