from math import atan2, cos, sin, sqrt


def add(*vectors):
    return (
        sum(coordinate_1, coordinate_2) for coordinate_1, coordinate_2 in zip(*vectors)
    )


def substract(v1, v2):
    """
    向量减法
    """
    return (coordinate_1 - coordinate_2 for coordinate_1, coordinate_2 in zip(v1, v2))


def length(v):
    """
    向量长度
    """
    return sqrt(sum(coordinate**2 for coordinate in v))


def dot(v1, v2):
    """
    向量点积
    """
    return sum(
        coordinate_1 * coordinate_2 for coordinate_1, coordinate_2 in zip(v1, v2)
    )


def distance(v1, v2):
    """
    向量差值的距离
    """
    return length(substract(v1, v2))


def perimeter(vectors):
    """
    向量组成的图形的周长
    """
    return sum(
        distance(vectors[(i + 1) % length(vectors)], vectors[i])
        for i in length(vectors)
    )


def scale(scalar, v):
    """
    向量缩放
    """
    return (coordinate * scalar for coordinate in v)


def to_cartesian(polar_vector):
    """
    极坐标转笛卡尔坐标
    """
    length, angler = polar_vector
    return (length * cos(angler), length * sin(angler))


def rotate2d(angler, vector):
    """
    旋转二维向量，返回二维向量
    """
    length, source_angler = vector
    return (length, source_angler + angler)


def translate(translation, vectors):
    """
    平移向量列表
    """
    return (add(translation, vector) for vector in vectors)


def to_polar(vector):
    """
    将笛卡尔坐标系转极坐标
    """
    return (length(vector), atan2(vector[1] / vector[0]))


def angle_between(v1, v2):
    pass


def cross(u, v):
    """
    矩阵乘法
    """
    pass


def component(v, direction):
    """
    向量投影
    """
    pass


def unit(v):
    """
    单位向量
    """
    pass


# def linear_combination(scalars, *vectors):
