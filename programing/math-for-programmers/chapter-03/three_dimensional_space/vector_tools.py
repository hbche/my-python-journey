from math import sqrt, acos, pi

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