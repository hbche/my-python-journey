from math import sqrt, acos, pi,atan, sin, cos

def add(*vectors: tuple):
    """
    add: 计算向量加法
    
    :param vectors: 说明
    """
    
    return tuple(sum(coordinates) for coordinates in zip(*vectors))

def subtract(v1, v2):
    """
    subtract: 计算两个向量相减
    """
    return tuple([coordinate1 - coordinate2 for coordinate1, coordinate2 in zip(v1, v2)])

def length(vector: tuple):
    """
    length: 计算向量长度
    
    :param vector: 说明
    """
    
    return sqrt(sum(coordinate ** 2 for coordinate in vector))


def dot(v1: tuple, v2: tuple) -> int:
    """
    dot: 计算两个向量的点积
    
    :param v1: 第一个向量
    :type v1: tuple
    :param v2: 第二个向量
    :type v2: tuple
    """
    
    return sum((coordiante1 * coordinate2 for coordiante1, coordinate2 in zip(v1, v2)))


def between_angle(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))

def radian_to_angle(radian):
    """
    radian_to_angle：将弧度转换成角度
    
    :param radian: 说明
    """
    return 360 / (2*pi) * radian


def cross(u, v):
    """
    cross：计算两个三维向量的向量积
    """
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)


def component(v, direction):
    """
    component: 将给定三维向量 v 按照给定方向分解成二维向量
    
    :param v: 三维向量
    :param direction: 视图向量
    """

    return dot(v, direction) / length(direction)


def vector_to_2d(v):
    """
    vector_to_2d：定义三维向量在 (1, 0, 0)和 (0, 1, 0)两个方向上的分量，从而将三维向量转换成二维向量（投影）
    
    :param v: 说明
    """
    return (component(v, (1, 0, 0)), component(v, (0, 1, 0)))


def face_to_2d(face):
    """
    face_to_2d: 将表示三角形的所有定点转换成二维向量
    
    :param face: 说明
    """
    return [vector_to_2d(vector) for vector in face]

def scale(s: int, v: tuple):
    """
    scale: 将向量 v 缩放 s 倍
    """
    return tuple(coordinate * s for coordinate in v)

def unit(v):
    """
    unit: 将向量 v 转换成长度为 1 的单位向量，方向保持不变
    """
    return scale(1/length(v), v)


def normal(face):
    """
    normal: 获取面的法线
    """
    return cross(subtract(face[1], face[0]), subtract(face[2], face[0]))

def to_polar(v):
    """
    将二维笛卡尔坐标转换成极坐标
    """
    return (length(v), atan(v[1] / v[0]))

def to_orthogonal(v):
    """
    将极坐标转换为二维笛卡尔坐标
    """
    l, angle = v
    return (round(l * cos(angle)), round(l * sin(angle)))

def rotate(v, rotate_angle):
    """
    将二维向量旋转指定弧度
    """
    l, angle = to_polar(v)
    return to_orthogonal((l, angle + rotate_angle))

def rotate_x_by(angle):
    """
    将三维向量围绕 X 轴逆时针旋转指定弧度
    """
    def new_function(v):
        vx, vy, vz = v
        return (vx, *rotate((vy, vz), angle))
    
    return new_function

def rotate_y_by(angle):
    """
    将三维向量围绕 Y 轴逆时针旋转指定弧度
    """
    def new_function(v):
        vx, vy, vz = v
        rotate_x, rotate_z = rotate((vx, vz), angle)
        return (rotate_x, vy, rotate_z)
    
    return new_function


def rotate_z_by(angle):
    """
    将三维坐标围绕 Z 轴逆时针旋转指定弧度
    """
    def new_function(v):
        vx, vy, vz = v
        return (*rotate((vx, vy), angle), vz)
    
    return new_function


def compose(*args):
    """
    函数组合
    """
    def new_function(input):
        state = input
        for f in reversed(args):
            state = f(state)
        return state
    return new_function

v = (1, 2, 3)
transform_1 = compose(rotate_z_by(pi/2), rotate_x_by(pi/2))
transform_2 = compose(rotate_x_by(pi/2), rotate_z_by(pi/2))
print(transform_1(v))   # (3, 1, 2)
print(f"Original vector: {v}")
# 绕Y轴顺时针旋转pi/2
print(compose(rotate_y_by(-pi/2))(v))   # (3, 2, -1)
print(transform_2(v))   # (-2, -3, 1)
print(f"Original vector: {v}")
# 绕Y轴逆时针旋转pi/2
print(compose(rotate_y_by(pi/2))(v))    # (-3, 2, 1)
