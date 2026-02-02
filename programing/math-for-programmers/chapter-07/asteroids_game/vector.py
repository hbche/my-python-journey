from math import sin, cos, sqrt, atan

def to_cartesian(length, angle):
    """
    将极坐标转换为笛卡尔坐标
    """
    return (length*cos(angle), length*sin(angle))

def length(v):
    """
    计算笛卡尔坐标的长度
    """
    return sqrt(sum(coordinate ** 2 for coordinate in v))

def to_polar(v):
    """
    将笛卡尔坐标转换为集坐标
    """
    return (length(v), atan(v[1]/v[0]))

def rotate2d(rotate_angle, v):
    """
    旋转坐标
    """
    length, angle = to_polar(v)
    return to_cartesian(length, angle + rotate_angle)

def add(v1, v2):
    """
    计算坐标相加
    """
    return (sum(coordinates) for coordinates in zip(v1, v2))

def distance(p1, p2):
    """
    计算两点之间的距离
    """
    x1, y1 = p1
    x2, y2 = p2
    
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)