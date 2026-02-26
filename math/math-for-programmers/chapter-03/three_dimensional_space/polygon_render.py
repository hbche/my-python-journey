# 将3D推向渲染在2D平面上的渲染函数

import matplotlib
from vector_tools import unit, normal, dot, face_to_2d
from draw2d import Polygon2D, draw2d

blues = matplotlib.colormaps['Blues']

def render(faces, light=(1, 2, 3), color_map=blues, lines=None):
    # 储存转换之后的多边形
    polygons = []

    for face in faces:
        # 获取每个面的法线向量
        unit_normal = unit(normal(face))

        # 由于假设视角是在Z轴正半轴处，所有面的朝向如果偏向Z轴负半轴，那么将不可见
        if unit_normal[2] > 0:
            # 法线与光源的点积越大，阴影越小
            c = color_map(1 - dot(unit_normal, unit(light)))
            # 为每一个三角形的边指定一个可选的lines参数，显示正在绘制的形状骨架
            p = Polygon2D(*face_to_2d(face), fill=c, color=lines)
            polygons.append(p)

    
    draw2d(*polygons, axes=False, origin=False, grid=None)
