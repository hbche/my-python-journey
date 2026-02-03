from abc import ABCMeta, abstractmethod

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