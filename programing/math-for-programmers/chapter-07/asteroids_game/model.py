from random import randint, uniform
from math import pi, sqrt, cos, sin
from vector import to_cartesian, rotate2d, add

# 代表小行星或宇宙飞船的基础模型
class PolygonModel():
    
    def __init__(self, points):
        # 表示形状的向量
        self.points = points
        # 当前旋转角度
        self.rotation_angle = 0
        # 当前中心点的x坐标和y坐标
        self.x = 0
        self.y = 0
        # x和y方向的移动速度
        self.vx = 0
        self.vy = 0
        
    def transformed(self):
        """
        旋转：一定要先应用旋转，否则，平移向量也会被旋转一个角度。
        """
        rotated = [rotate2d(self.rotation_angle, p) for p in self.points]
        return [add((self.x, self.y), v) for v in rotated]
    
    def move(self, milliseconds):
        """
        基于时钟间隔，结合x和y轴方向的速度，计算多边形的移动
        """
        dx, dy = self.vx * milliseconds / 1000.0, self.vy * milliseconds / 1000.0
        self.x, self.y = add((self.x, self.y), (dx, dy))
        self.rotation_angle += self.rotation_angle * milliseconds / 1000.0
    
    # def does_intersect(self):
        

class Ship(PolygonModel):
    """
    表示飞船的数据结构
    """
    
    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])
        
    def laser_segment(self):
        """
        计算激光的起始和终止坐标
        """
        
        # 因为我们的坐标系是-10到10，所以此处的激光最大长度是(-10, -10)到(10, 10)之间的距离
        dist = 20 * sqrt(2)
        x, y = self.transformed()[0]
        return (x, y), (x + dist * cos(self.rotation_angle), y + dist * sin(self.rotation_angle))
        
        
class Asteroid(PolygonModel):
    """
    表示小行星的数据结构
    """
    
    def __init__(self):
        # 随机生成5到9之间的一个随机整数
        sides = randint(5, 9)
        # 根据边的数量，几次计算每个向量的坐标，随机生成长度在0.5到1.0之间逆时针增加角度的极坐标，再将其转换成直角坐标
        vs = [to_cartesian(uniform(0.5, 1.0), 2*pi*i/sides) for i in range(0, sides)]
        super().__init__(vs)
        