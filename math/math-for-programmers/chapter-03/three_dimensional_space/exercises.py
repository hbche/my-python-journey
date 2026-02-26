from draw3d import *
from vector_tools import *

# # 3.1 绘制坐标点和三维箭头以及三维立体框
# draw3d(
#     Points3D((-1, -2, 2)),
#     Arrow3D((-1, -2, 2)),
#     Box3D(-1, -2, 2)
# )

# # 3.2 绘制立方体，(1, -1, 1)是其中一个点
# pm1 = [-1, 1]
# points = [
#     (x, y, z) for x in pm1 for y in pm1 for z in pm1
# ]
# edges = [
#     ((-1, y, z), (1, y, z)) for y in pm1 for z in pm1
# ] + [
#     ((x, -1, z), (x, 1, z)) for x in pm1 for z in pm1
# ] + [
#     ((x, y, -1), (x, y, 1)) for x in pm1 for y in pm1
# ]
# draw3d(
#     Points3D(*points),
#     *[Segment3D(*edge) for edge in edges]
# )

# 3.3 将(4, 0, 3)和(-1, 0, 1)绘制为Arrow3D对象，使它们在三维空间中以两种顺序首尾相接。它们的向量和是多少？

def add(*vectors):
    return tuple(sum(coordiantes) for coordiantes in zip(*vectors))

# v1 = (4, 0, 3)
# v2 = (-1, 0, 1)
# sum_v = add(v1, v2)

# draw3d(
#     Arrow3D(v1, color='gray'),
#     Arrow3D(sum_v, v1, color='gray'),
#     Arrow3D(v2, color='orange'),
#     Arrow3D(sum_v, v2, color='orange'),
#     Arrow3D(sum_v)
# )

# 3.4 假设设置vectors1=[(1,2,3,4,5),(6,7,8,9,10)]和vectors2=[(1,2),(3,4),(5,6)]。在不使用Python求值的情况下，zip(*vectors1)和zip(*vectors2)的长度分别是多少？

# 3.5 下面的代码创建了一个包含24个Python向量的列表。

# from math import sin, cos, pi
# vs = [(sin(pi*t/6), cos(pi*t/6), 1.0/3) for t in range(0, 24)]

# running_sum = (0, 0, 0)

# arrows = []

# for v in vs:
#     next_sum = add(running_sum, v)
#     arrows.append(Arrow3D(next_sum, running_sum))
#     running_sum = next_sum
    
# # 打印所有向量和的结果
# print(running_sum)

# draw3d(*arrows)

# 3.6：编写函数scale(scalar,vector)，返回输入标量乘以输入向量的结果。具体地说，这个函数要同时适用于二维和三维向量，以及有任意多坐标的向量。

# 3.18 (1, 1, 1)与(-1, -1, 1)之间的角是多少度

v1 = (1, 1, 1)
v2 = (-1, -1, 1)
print(between_angle(v1, v2))    # 1.911
print(radian_to_angle(between_angle(v1, v2)))   # 109.5°