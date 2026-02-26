# 第 6 章 高维泛化

目标：

- 用 Python 实现对向量进行通用描述的抽象基类
- 定义向量空间，并且列出其有用的属性
- 将函数、矩阵、图像和声波描述为向量
- 探索向量空间的一些有趣的子空间

## 6.1 泛化向量的定义

### 6.1.1 为二维向量创建一个类

```py
class Vector2():
    """
    二维向量
    """

    def __init__(self, x, y):
        super()
        self.x = x
        self.y = y

    def add(self, other):
        """
        add: 向量加法
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def scale(self, scaler):
        """
        scale: 向量乘法
        """
        return Vector2(scaler * self.x, scaler * self.y)

    def __eq__(self, other):
        """
        __eq__: 向量相等性比较，运算符=重载
        """
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        """
        __repr__: 格式化输出重载
        """
        return f"Vector2({self.x}, {self.y})"
```

### 6.1.2 升级 Vector2

增加运算符重载

```py
class Vector2():
    """
    二维向量
    """

    def __init__(self, x, y):
        super()
        self.x = x
        self.y = y

    def add(self, other):
        """
        add: 向量加法
        """
        return Vector2(self.x + other.x, self.y + other.y)

    def scale(self, scaler):
        """
        scale: 向量乘法
        """
        return Vector2(scaler * self.x, scaler * self.y)

    def __eq__(self, other):
        """
        __eq__: 向量相等性比较，运算符=重载
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, v2):
        """
        运算符 + 重载
        """
        return self.add(v2)

    def __mul__(self, scalar):
        """
        __mul__: 重载乘法运算符
        """
        return self.scale(scalar)

    def __rmul__(self, scalar):
        """
        __rmul__: 重载标量在右侧的乘法运算符
        """
        return self.scale(scalar)

    def __neg__(self):
        """
        __neg__: 重载取反运算符
        """
        return self.scale(-1)

    def __repr__(self):
        """
        __repr__: 格式化输出重载
        """
        return f"Vector2({self.x}, {self.y})"
```

### 6.1.3 使用同样的方法定义三维向量

```py
class Vector3():
    """
    Vector3: 三维向量
    """

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
```

### 6.1.4 构建向量基类

将公共逻辑抽取到基类中:

```py
class Vector(metaclass=ABCMeta):

    @abstractmethod
    def add(self, other):
        pass

    @abstractmethod
    def scale(self, scalar):
        pass

    def subtract(self, other):
        """
        subtract: 实现向量减法
        """
        return self.add(-1 * other)

    def __sub__(self, other):
        """
        __sub__: 重载向量减法运算符
        """
        return self.subtract(other)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)
```

基于 Vector 基类实现二维向量类：

```py
class Vector2(Vector):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def scale(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"
```

### 6.1.5 定义向量空间

> 定义：向量是一个对象，具备一种与其他向量相加以及与标量相乘的合适方式。

以下是几条重要的规则：

1. 向量相加与顺序无关：$v + w = w + v$
2. 向量相加与如何分组无关：$u + (v + w) = (u + v) + w$
