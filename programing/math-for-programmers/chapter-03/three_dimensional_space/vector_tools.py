from math import sqrt, acos, pi

def add(*vectors: tuple):
    """
    add: 计算向量加法
    
    :param vectors: 说明
    """
    
    return tuple(sum(coordinates) for coordinates in zip(*vectors))


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