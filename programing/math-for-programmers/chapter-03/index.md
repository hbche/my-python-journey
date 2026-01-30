# 第 3 章 上升到三维世界

目标：

- 建立三维向量的心智模型
- 进行三维向量运算
- 使用点集和向量集测量长度和方向
- 在二维平面上渲染三维对象

## 3.1 在三维空间中绘制向量

绘制三维坐标系：

```py
from colors import *
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

## https://stackoverflow.com/a/22867877/1704140
class FancyArrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d

        # 🔥 关键：从 Axes 获取投影矩阵
        xs, ys, zs = proj3d.proj_transform(
            xs3d, ys3d, zs3d, self.axes.get_proj()
        )

        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        # 返回深度值，用于 z-order 排序
        return np.min(zs)

class Polygon3D():

    def __init__(self, *verties, color=blue):
        self.verties = verties
        self.color = color

class Points3D():

    def __init__(self, *vectors, color=black):
        self.vectors = vectors
        self.color = color

class Arrow3D():

    def __init__(self, tip, tail=(0, 0, 0), color=red):
        self.tip = tip
        self.tail = tail
        self.color = color

class Segment3D():

    def __init__(self, start_point, end_point, color=blue, linestyle='solid'):
        self.start_point = start_point
        self.end_point = end_point
        self.color = color
        self.linestyle = linestyle

class Box3D():

    def __init__(self, *vector):
        self.vector = vector

# 工具方法，从对象列表中获取所有向量
def extract_vectors_3D(objects):
    for object in objects:
        if type(object) == Polygon3D:
            for v in object.verties:
                yield v
        elif type(object) == Points3D:
            for v in object.vectors:
                yield v
        elif type(object) == Arrow3D:
            yield object.tip
            yield object.tail
        elif type(object) == Segment3D:
            yield object.start_point
            yield object.end_point
        elif type(object) == Box3D:
            yield object.vector
        else:
            raise TypeError(f'Unrecognized object: {object}')



def draw3d(*objects, origin=True, axes=True, width=6, save_as=None, azim=None, elev=None, xlim=None, ylim=None, zlim=None, xticks=None, yticks=None, zticks=None, depthshade=False):

    # 获取当前 figure
    fig = plt.gcf()
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=elev, azim=azim)

    all_vectors = list(extract_vectors_3D(objects))

    if origin:
        all_vectors.append((0, 0, 0))
    xs, ys, zs = zip(*all_vectors)

    max_x, min_x = max(0, *xs), min(0, *xs)
    max_y, min_y = max(0, *ys), min(0, *ys)
    max_z, min_z = max(0, *zs), min(0, *zs)

    x_size = max_x - min_x
    y_size = max_y - min_y
    z_size = max_z - min_z

    padding_x = 0.05 * x_size if x_size else 1
    padding_y = 0.05 * y_size if y_size else 1
    padding_z = 0.05 * z_size if z_size else 1

    plot_x_range = (min(min_x - padding_x, -2), max(max_x + padding_x, 2))
    plot_y_range = (min(min_y - padding_y, -2), max(max_y + padding_y, 2))
    plot_z_range = (min(min_z - padding_z, -2), max(max_z + padding_z, 2))

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # 绘制线段工具函数
    def draw_segment(start, end, color=black, linestyle='solid'):
        xs, ys, zs = [[start[i], end[i]] for i in range(0, 3)]
        ax.plot(xs, ys, zs, color=color, linestyle=linestyle)

    if axes:
        # 绘制坐标轴
        draw_segment((plot_x_range[0], 0, 0), (plot_x_range[1], 0, 0))
        draw_segment((0, plot_y_range[0], 0),  (0, plot_x_range[1], 0))
        draw_segment((0, 0, plot_z_range[0]), (0, 0, plot_z_range[1]))

    if origin:
        # 绘制坐标原点
        ax.scatter([0], [0], [0], color='k', marker='x')


    for object in objects:
        if type(object) == Points3D:
            # 绘制 点
            xs, ys, zs = zip(*object.vectors)
            ax.scatter(xs, ys, zs, color=object.color, depthshade=depthshade)

        elif type(object) == Polygon3D:
            # 绘制多边形
            for i in range(0, len(object.verties)):
                # 为了避免最后一个线段的结尾节点索引溢出，且最后一个线段的结尾节点设置为线段的第一个节点的起点
                draw_segment(object.verties[i], object.verties[i+1] % len(object.verties), color=object.color)

        elif type(object) == Arrow3D:
            xs, ys, zs = zip(object.tail, object.tip)
            a = FancyArrow3D(xs, ys, zs, mutation_scale=20, arrowstyle='-|>', color=object.color)

            ax.add_artist(a)

        elif type(object) == Segment3D:
            # 绘制线段
            draw_segment(object.start_point, object.end_point, color=object.color, linestyle=object.linestyle)

        elif type(object) == Box3D:
            x, y, z = object.vector
            kwargs = {'color': 'gray', 'linestyle': 'dashed'}
            draw_segment((0,y,0),(x,y,0),**kwargs)
            draw_segment((0,0,z),(0,y,z),**kwargs)
            draw_segment((0,0,z),(x,0,z),**kwargs)
            draw_segment((0,y,0),(0,y,z),**kwargs)
            draw_segment((x,0,0),(x,y,0),**kwargs)
            draw_segment((x,0,0),(x,0,z),**kwargs)
            draw_segment((0,y,z),(x,y,z),**kwargs)
            draw_segment((x,0,z),(x,y,z),**kwargs)
            draw_segment((x,y,0),(x,y,z),**kwargs)
        else:
            raise TypeError("Unrecognized object: {}".format(object))

    if xlim and ylim and zlim:
        plt.xlim(*xlim)
        plt.ylim(*ylim)
        plt.zlim(*zlim)

    if xticks and yticks and zticks:
        plt.xticks(xticks)
        plt.yticks(yticks)
        ax.set_zticks(zticks)

    if save_as:
        plt.savefig(save_as)

    plt.show()
```

### 3.1.1 用坐标表示三维向量

使用 `(x, y, z)` 表示三维向量

### 3.1.1 用 Python 进行三维向量绘制

```py
from draw3d import *

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

# 绘制带箭头的向量，并展示向量的box立方体
draw3d(
    Points3D((2,2,2),(1,-2,-2)),
    Arrow3D((2, 2, 2)),
    Arrow3D((1, -2, -2)),
    Segment3D((2, 2, 2), (1, -2, -2)),
    Box3D(2, 2, 2),
    Box3D(1, -2, -2)
)
```

## 3.2 三维空间中的向量运算

### 3.2.1 添加三维向量

在三维空间中，向量加法仍然是按照各向量对应坐标相加进行计算。

使用 Python 绘制向量 (2, 1, 1)和(1, 2, 2)相加：

```py
def add(*vectors):
    by_coordinate = zip(*vectors)
    coordinate_sums = [sum(coords) for coords in by_coordinate]
    return tuple(coordinate_sums)

v1 = (2, 1, 1)
v2 = (1, 2, 2)
sum_result = add(v1, v2)

draw3d(
    Arrow3D(v1),
    Arrow3D(v2),
    Arrow3D(sum_result),
    Box3D(*v1),
    Box3D(*v2),
    Box3D(*sum_result)
)
```

### 3.2.2 三维空间中的标量乘法

将三维向量乘以标量，就是将其所有分量乘以标量系数。

用 Python 绘制 `(1, 2, 3) * 2` 的结果：

```py
def scale(scale, vector):
    return tuple(scale * v for v in vector)

v = (1, 2, 3)
scale_2_v = scale(2, v)

draw3d(
    Arrow3D(v),
    Box3D(*v),
    Arrow3D(scale_2_v),
    Box3D(*scale_2_v)
)
```

### 3.2.3 三维向量减法

`v - w` 就是从 w 到 v 的位移，把这个向量与 w 相加即可得到 v。

```py
def substract(v1, v2):
    return tuple(coordinate[0] - coordinate[1] for coordinate in zip(v1, v2))

v1 = (-1, -3, 3)
v2 = (3, 2, 4)

# draw3d(
#     Arrow3D(v1),
#     Box3D(*v1),
#     Arrow3D(v2),
#     Box3D(*v2)
# )

substract_result = substract(v1, v2)

draw3d(
    Arrow3D(substract_result),
    Box3D(*substract_result)
)
```

### 3.2.4 计算长度和距离

三维向量 `(x, y, z)` 的长度为 $\sqrt{x^2 + y^2 + z^2 }$。

使用 Python 绘制向量 `(4, 3, 12)` 的长度计算：

```py
def add(*vectors):
    return tuple(sum(coordinate) for coordinate in zip(*vectors))

v = (4, 3, 12)

vx = (4, 0, 0)
vy = (0, 3, 0)
vz = (0, 0, 12)

draw3d(
    Arrow3D(vx),
    Arrow3D(vy),
    Arrow3D(add(vx, vy)),
    Arrow3D(v, add(vx, vy)),
    Arrow3D(v),
    Box3D(*v)
)
```

使用 Python 计算向量长度：

```py
def length(vector):
    return math.sqrt(sum(coordinate ** 2 for coordinate in vector))
```

### 3.2.5 计算角度和方向

类似二维向量的极坐标，三维向量需要使用一个长度和两个角度表示，其中一个角度表示相
对 x 轴逆时针方向的角度，第二个角度表示相对 y 轴逆时针方向的角度。这种坐标称为球
坐标。

### 3.2.6 练习

## 3.3 点积：测量向量对齐

点积取两个向量并返回一个标量（数），而向量集取两个向量并返回另一个向量。然而，使
用这两种运算都可以推断出三维空间中向量的长度和方向。

### 3.3.1 绘制点积

点击（也叫内积）是对两个向量的运算，返回一个标量。

指向相似方向的两个向量的点积为正，并且向量越大，点积越大。相反，如果两个向量指向
相反的方向，则其点积为负。向量越长，点积越小。如果两个向量的方向完全垂直，那么无
论他们的长度如何，点积都是零。

### 3.3.2 计算点积

给定两个向量的坐标，有一个计算点积的简单工时：将相应的坐标相乘，然后将乘积相加。

假设现在给定两个向量 $v = (x_v, y_v, z_v)$ 和 $w = (x_w, y_w, z_w)$，则他们的点
积计算公式如下：

$$
v\cdot{w} = x_v \times{x_w} + y_v\times{y_w} + z_v\times{z_w}
$$

Python 实现如下：

```py
def dot(v1, v2):

    return sum((coordiante1 * coordinate2 for coordiante1, coordinate2 in zip(v1, v2)))
```

### 3.3.3 点积的示例

### 3.3.4 用点积测量角度

我们已经知道，点击是根据两个向量的夹角而变化的。其实点积还有另一个公式。

$$
v\cdot{w} = |v|\times{|w|}\times{cos(θ)}
$$

因此我们可以依据点积的两种计算公式计算两个向量的夹角：

$$
cos(θ) = \frac{v\cdot{w}} {|v|\times{|w|}}
$$

利用反三角函数推理出 θ 的值：

$$
θ = arccos(\frac{v\cdot{w}} {|v|\times{|w|}})
$$

计算两个向量间夹角的 Python 实现如下：

```py
def between_angle(v1, v2):
    return acos(dot(v1, v2) / (length(v1) * length(v2)))
```

### 3.3.5 练习

## 3.4 向量积：测量定向区域

### 3.4.1 在三维空间中确定自己的朝向

### 3.4.2 找到向量积的方向

向量积遵循右手规则。向量积 $u \times{v}$ 向量的方向：右手食指指向 u 的方向，将三
指弯向 v 的方向，拇指指向的就是 $u \times{v}$ 的方向。

### 3.4.3 求向量的长度

和点积一样，向量积的长度也是一个数，它提供了关于输入向量的相对位置的信息。

两个向量的向量积对应的向量的长度是两个向量构成的平行四边形的面积。

$
|u \times{v}| = |u| \times{|v|} \times{sin(θ)}
$

### 3.4.4 计算三维向量的向量积

u = $(u_x, u_y, u_z)$

v = $(v_x, v_y, v_z)$

向量积的公式如下：

$$
u \times{v} = (u_y \times{v_z}-u_z\times{v_y}, u_z\times{v_x} - u_x\times{v_z, u_x\times{v_y}}-u_y\times{v_x})
$$

使用 Python 代码实现如下：

```py
def cross(u, v):
    ux, uy, uz = u
    vx, vy, vz = v
    return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)
```

### 3.4.5 练习

## 3.5 在二维平面上渲染三维对象

### 3.5.1 使用向量定义三维对象

使用向量表示三维对象：

```py
# 正8面体的向量表示，每个二维数组代表一个面
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
```

### 3.5.2 二维投影

要把三维点变成二维点，必须选择我们的三维观察方向。一旦从我们的视角确定了定义“上”
和“右”的两个三维向量，就可以将任意三维向量投射到它们上面，得到两个分量，而不是三
个分量。以下函数利用点积提取三维向量在给定方向上的分量。

```py
def component(v, direction):
    return dot(v, direction) / length(direction)
```

通过对两个方向硬编码，我们可以建立一种从三个坐标向下投影到两个坐标的方法。这个函
数接收一个三维向量或三个数组组成的元组，并返回一个二维向量或两个数组组成的元组。

```py
def vector_to_2d(v):
    return (component(v, (1, 0, 0)), component(v, (0, 1, 0)))
```

例如三维向量 (1, 1, 1) 对应的二维投影为：

```py
vector_to_2d((1, 1, 1)) # (1.0, 1.0)
```

依次类推，我们可以将三角形从三维转换为二维，我们只需要将这个投影函数应用到表示三
角形面的所有定点向量上。

```py
def face_to_2d(face):
    return [vector_to_2d(vector) for vector in face]
```

### 3.5.3 确定面的朝向和阴影

为了给二维绘图着色，我们根据每个三角形面对给定光源的角度大小，为其选择一个固定的
颜色。假设光源在基于原点坐标(1, 2, 3)处，那么三角形面的亮度取决于它余光线的垂直
度。另一种测量方法是借助垂直于面的向量与光源的对齐程度。我们不必担心颜色的计算
，matplotlib 有一个内置的库来做这些工作。例如：

```py
blues = matplotlib.colormaps['Blues']
```

提供了一个叫 blues 函数，它将从 0 到 1 的数映射到由暗到亮的蓝色光谱上。我们的任
务是找出一个 0 到 1 之间的数，表示一个面的明亮程度。

给定一个垂直于每个面的向量（法线）和一个指向光源的向量，它们的点积就说明了其对齐
程度。此外，由于我们只考虑方向，可以选择长度为 1 的向量。那么，如果该面完全朝向
光源，点积介于 0 和 1 之间。如果它与光源的角度超过 90°，将完全不被照亮。这个辅助
函数接收一个向量，并返回另一个相同方向但长度为 1 的向量。

```py
def unit(v):
    return scale(1/length(v), v)
```

第二个辅助函数接收一个面，并返回一个垂直于它的向量。

```py
def normal(face):
    return cross(subtract(face[1], face[0], subtract(face[2], face[0])))
```

把他们结合起来，就得到了一个绘制三角形的函数。它调用 draw2d 函数来渲染三维模型。

```py
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
```

下面基于之前定义的 8 面体的数据和渲染函数对 8 面体进行渲染：

```py
render(octahedron, color_map=matplotlib.colormaps['Blues'], line=black)
```

### 3.5.4 联系

## 3.6 小结
