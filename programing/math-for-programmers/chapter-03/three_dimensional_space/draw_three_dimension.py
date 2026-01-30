from draw3d import *
import math
from vector_tools import add, length, dot, between_angle, cross, vector_to_2d

# draw3d()

# 绘制箭头
# draw3d(
#     Arrow3D((2, 2, 2)),
#     Arrow3D((1, -2, -2))
# )

# # 绘制带箭头的向量，以及两个向量之间的连线
# draw3d(
#     Points3D((2,2,2),(1,-2,-2)),
#     Arrow3D((2,2,2)),
#     Arrow3D((1,-2,-2)),
#     Segment3D((2,2,2), (1,-2,-2))
# )

# # 绘制带箭头的向量，并展示向量的box立方体
# draw3d(
#     Points3D((2,2,2),(1,-2,-2)),
#     Arrow3D((2, 2, 2)),
#     Arrow3D((1, -2, -2)),
#     Segment3D((2, 2, 2), (1, -2, -2)),
#     Box3D(2, 2, 2),
#     Box3D(1, -2, -2)
# )

# 3.2 向量运算
# 3.2.1 向量加法

# def add(*vectors):
#     by_coordinate = zip(*vectors)
#     coordinate_sums = [sum(coords) for coords in by_coordinate]
#     return tuple(coordinate_sums)

# v1 = (2, 1, 1)
# v2 = (1, 2, 2)
# sum_result = add(v1, v2)

# draw3d(
#     Arrow3D(v1),
#     Arrow3D(v2),
#     Arrow3D(sum_result),
#     Box3D(*v1),
#     Box3D(*v2),
#     Box3D(*sum_result)
# )

# 3.2.2 标量乘法

# def scale(scale, vector):
#     return tuple(scale * v for v in vector)

# v = (1, 2, 3)
# scale_2_v = scale(2, v)

# draw3d(
#     Arrow3D(v),
#     Box3D(*v),
#     Arrow3D(scale_2_v),
#     Box3D(*scale_2_v)
# )

# 3.2.3 向量减法

# def substract(v1, v2):
#     return tuple(coordinate[0] - coordinate[1] for coordinate in zip(v1, v2))

# v1 = (-1, -3, 3)
# v2 = (3, 2, 4)

# # draw3d(
# #     Arrow3D(v1),
# #     Box3D(*v1),
# #     Arrow3D(v2),
# #     Box3D(*v2)
# # )

# substract_result = substract(v1, v2)

# draw3d(
#     Arrow3D(substract_result),
#     Box3D(*substract_result)
# )

# 3.2.4 向量的长度和距离

# def add(*vectors):
#     return tuple(sum(coordinate) for coordinate in zip(*vectors))

# v = (4, 3, 12)

# vx = (4, 0, 0)
# vy = (0, 3, 0)
# vz = (0, 0, 12)

# draw3d(
#     # Arrow3D(vx),
#     # Arrow3D(vy),
#     Points3D(*[add(vx, vy), v]),
#     Arrow3D(add(vx, vy), color='gray'),
#     Arrow3D(v, add(vx, vy), color='gray'),
#     Arrow3D(v),
#     # Box3D(*v)
# )

# print(f"The length of {v} is: {length(v)}")

# # 3.3.2 点积计算

# v1 = (2,3, 0)
# v2 = (4, 5, 0)
# draw3d(
#     Arrow3D(v1),
#     Arrow3D(v2)
# )
# print(dot(v1, v2))

# # 3.3.4 计算向量的夹角
# v1 = (1, 1, 0)
# v2 = (1, -1, 0)
# print(between_angle(v1, v2))

# # 3.4.4 计算向量积
# v1 = (1, 0, 1)
# v2 = (-1, 0, 0)
# print(cross(v1, v2))

# # 3.5.1 绘制三维对象
# draw3d(
#     Segment3D((-1, 0, 0), (1, 0, 0)),
#     Segment3D((0, -1, 0), (0, 1, 0)),
#     Segment3D((0, 0, -1), (0, 0, 1)),
#     Points3D(*[
#         (1, 0, 0),
#         (-1, 0, 0),
#         (0, 1, 0),
#         (0, -1, 0),
#         (0, 0, 1),
#         (0, 0, -1)
#     ]),
#     Arrow3D((1, 0, 0), (0, 0, 1)),
#     Arrow3D((0, 1, 0), (0, 0, 1)),
#     Arrow3D((-1, 0, 0), (0, 0, 1)),
#     Arrow3D((0, -1, 0), (0, 0, 1)),
# )

# 正8面体的向量表示
octahedron = [
    [(1,0,0), (0,1,0), (0,0,1)],
    [(1,0,0), (0,0,-1), (0,1,0)],
    [(1,0,0), (0,0,1), (0,-1,0)],
    [(1,0,0), (0,-1,0), (0,0,-1)],
    [(-1,0,0), (0,0,1), (0,1,0)],
    [(-1,0,0), (0,1,0), (0,0,-1)],
    [(-1,0,0), (0,-1,0), (0,0,1)],
    [(-1,0,0), (0,0,-1), (0,-1,0)],
]

# 获取端点
def vertices(faces):
    return list(set([vertex for face in faces for vertex in face]))

print(vector_to_2d((1, 1, 1)))