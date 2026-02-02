# 第 7 章 求解线性方程组

目标：

- 检测二维视频游戏中对象的碰撞
- 用方程来表示直线并找出直线在平面上的交点
- 绘制和求解三维或更高维度的线性方程组
- 将向量重写为其他向量的线性组合

本章将通过设计实现景点街机游戏 Asteroids，对上述目标进行讲解。

## 7.0 前置知识

本章将基于 Python 游戏库 pygame 进行开发，我们需要掌握 pygame 的基本使用。

## 7.1 设计一款街机游戏

本章将讲解一款简化版的小行星将以多边形的形式呈现。我们继续使用向量建模。使用多边
形表示小行星。例如使用 8 个向量表示一颗八边形的小行星，将它们连接起来绘制轮廓。

### 7.1.1 游戏建模

小行星或宇宙飞船在太空中旅行时会发生平移或旋转，但形状保持不变。因此，我们将代表
这个形状的向量与其中心点的 x 坐标和 y 坐标分开存储。因为 x 和 y 坐标会随时间变化
。再存储一个角度，表示物体在当前时刻的旋转。PolygonModel 类代表一个可以平移或旋
转并保持形状不变的游戏实体（飞船或小行星）。默认情况下，其中心点 x 坐标和 y 坐标
机器旋转角度设置为 0。

以下是对应数据模型的代码：

```py
from random import randint, uniform, pi
from vector import to_cartesian

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


class Ship(PolygonModel):
    """
    表示飞船的数据结构
    """

    def __init__(self):
        super().__init__([(0.5, 0), (-0.25, 0.25), (-0.25, -0.25)])


class Asteroid(PolygonModel):
    """
    表示小行星的数据结构
    """

    def __init__(self):
        # 随机生成5到9之间的一个随机整数
        sides = randint(5, 9)
        # 长度是0.5到1.0之间的随机数，角度是2π/n的倍数，其中n是边数
        vs = [to_cartesian(uniform(0.5, 1.0), 2*pi*i/sides) for i in range(0, sides)]
        super().__init__(vs)

```

### 7.1.2 渲染游戏

游戏的初始状态需要一搜飞船和几颗小行星。开始时飞船在屏幕中心，小行星则随机分布在
屏幕上。可以显示一个在 x 方向和 y 方向上分别为-10 到 10 的平面区域，如下所示：

```py
ship = Ship()

asteroid_count = 10
asteroids = [Asteroid() for _ in range(0, asteroid_count)]

for ast in asteroids:
    ast.x = randint(-9, 9)
    ast.y = randint(-9, 9)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

width, height = (400, 400)

def to_pixels(x, y):
    """
    将多边形的坐标转换成像素坐标，因为多边形的坐标原点在屏幕中心，且分成了-10到10这20个单元格，屏幕坐标系的原点在左上角，且长宽为400像素
    """
    return (width/2 + width*x/20, height/2 - height*y/20)

def draw_poly(screen, polygon_model: PolygonModel, color=GREEN):
    """
    在pygame的屏幕上绘制多边形
    """
    # 获取每个多边形对象的端点坐标
    pixel_points = [to_pixels(x, y) for x, y in polygon_model.transformed()]
    # 以闭合回路在screen上以指定颜色绘制多边形
    pygame.draw.aalines(screen, color, True, pixel_points, 10)

screenshot_mode = False

def main():
    """
    定义主程序
    """

    # 初始化 pygame
    pygame.init()

    # 获取pygame的screen
    screen = pygame.display.set_mode([width, height])

    pygame.display.set_caption('Asteroids!')

    done = False
    clock = pygame.time.Clock()

    while not done:

        clock.tick()

        for event in pygame.event.get():
            # 监听退出程序事件
            if event.type == pygame.QUIT:
                done = True


        milliseconds = clock.get_time()

        for ast in asteroids:
            ast.move(milliseconds)

        screen.fill(WHITE)

        draw_poly(screen, ship)

        for asteroid in asteroids:
                draw_poly(screen, asteroid, color=GREEN)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    if '--screenshot' in sys.argv:
        screenshot_mode = True

    main()
```

### 7.1.3 发射激光

我们接下来为飞船实现一种自我防御的方法！玩家能够使用左右箭头键让飞机瞄准，然后按
下空格键来发射激光。激光束应从飞船的顶端射出，并延伸到屏幕的边缘。

我们给飞船扩展激光函数：

```py
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
```

接下来我们为游戏添加按键监听，实现激光发射！

```py
def draw_segment(screen, v1, v2, color=RED):
    """
    在屏幕上绘制线段
    """
    pygame.draw.aalines(screen, color, False, [to_pixels(*v1), to_pixels(*v2)], 10)

def main():

    pygame.init()

    screen = pygame.display.set_mode([width, height])

    pygame.display.set_caption('Asteroids!')

    done = False
    clock = pygame.time.Clock()

    while not done:

        clock.tick()

        for event in pygame.event.get():
            # 监听退出程序事件
            if event.type == pygame.QUIT:
                done = True


        milliseconds = clock.get_time()
        keys = pygame.key.get_pressed()

        for ast in asteroids:
            ast.move(milliseconds)

        # 获取飞船的激光坐标
        laser = ship.laser_segment()

        screen.fill(WHITE)

        if keys[pygame.K_SPACE]:
            draw_segment(screen, *laser)

        draw_poly(screen, ship)

        for asteroid in asteroids:
            draw_poly(screen, asteroid, color=GREEN)

        pygame.display.flip()

    pygame.quit()
```

### 7.1.4 练习

7.1：在 PolyonModel 模型上实现 transformed()方法。该方法返回由对象的 x 属性和 y
属性转换并由 rotation_angle 属性旋转的模型的点。

```py
class PolygonModel():
    ...

    def transformed(self):
        """
        旋转：一定要先应用旋转，否则，平移向量也会被旋转一个角度。
        """
        rotated = [rotate2d(self.rotation_angle, p) for p in self.points]
        return [add((self.x, self.y), v) for v in rotated]
```

7.2：实现一个 to_pixels(x, y)函数。该函数取一对笛卡尔坐标系中的坐标，将其转换为
pygame 坐标系中的坐标。

```py
def to_pixels(x, y):
    """
    由于笛卡尔坐标系是以屏幕中心为原点，向右和向上分别为x轴正坐标和y轴正坐标
    pygame坐标系，以屏幕左上角为坐标原点，向右和向下才是x轴正坐标和y轴正坐标
    我们现在需要实现将笛卡尔坐标转换为pygame坐标：
    因为多边形的坐标原点在屏幕中心，且分成了-10到10这20个单元格，所以笛卡尔坐标每一个单位长度对应屏幕的400/20像素
    """
    return (width/2 + width*x/20, height/2 - height*y/20)
```

## 7.2 找到直线的交点

接下来的重点是我们需要判断激光是否击中小行星。抽象成数学建模，就是激光是否和多边
形中的某一条边存在交点。

### 7.2.1 为直线选择正确的

### 7.2.2 直线的标准形式方程

`x + 2y = 8`就是一种标准的方程。

### 7.2.3 线性方程组的矩阵形式

例如，现在有一个小行星的一条边对应的方程为 `x + 2y = 8`，其与激光对应的方程
`x - y = 0` 相交。我们可以将其转换成矩阵形式进行表示：

$$
x \cdot
\begin{pmatrix}
  1 \\
  1 \\
\end{pmatrix}
+ y \cdot

\begin{pmatrix}
  -1 \\
  2 \\
\end{pmatrix}
=

\begin{pmatrix}
  8 \\
  0 \\
\end{pmatrix}
$$

另一种方法是进一步合并，并将其写成矩阵乘法。系数为 x 和 y 的(-1, 1)和(-1, -2)的
线性组合与矩阵乘积相同。

$$
\begin{pmatrix}
    1 & -1 \\
    1 & 2 \\
\end{pmatrix}

\cdot

\begin{pmatrix}
    x \\
    y \\
\end{pmatrix}

=

\begin{pmatrix}
    0 \\
    8 \\
\end{pmatrix}
$$

### 7.2.4 使用 NumPy 求解线性方程组

虽然只是表示方法存在差异，但是以矩阵形式对问题进行框架化处理使我们可以使用预先构
建的工具来解决该问题。具体来说，Python 的 NumPy 库有一个线性代数模块和一个用于解
决这类方程的函数。这里有一个例子。

```py
# 利用 NumPy 求解线性方程组
import numpy as np

# 将矩阵打包为NumPy数组对象
matrix = np.array(((1, -1), (1, 2)))
# 将输出对象打包成NumPy数组
out = np.array((0, 8))

# numpy.linalg.solve函数接收一个矩阵和一个输出矩阵，并产生该输出向量的输入向量
result = np.linalg.solve(matrix, out)

print(result)   # 输出结果为 [2.66666667 2.66666667]
```

通过 NumPy 可以算出交点的 x 坐标和 y 坐标分别约为 8/3，从几何上看起来是正确的。

### 7.2.5 确定激光是否击中小行星

现在我们来为 PolygonModel 实现碰撞检测的函数。对于这个类的任何实例，如果输入线段
与多边形的任何线段相交，则此方法返回 True。

为此，我们需要实现一个辅助函数。首先，需要将给定的线段从端点向量对转换为标准的线
性方程。

接下来，给定两条线段，每条线段都由它的一对端点向量表示，我们要找出它们的交点。如
果 u1 和 u2 是第一条线段的端点，v1 和 v2 是第二条线段的端点，我们首先找到标准方
程，然后将它们传递给 NumPy 来求解。例如：

```py
def standard_form(p1, p2):
    """
    根据线段端点，输出直线的标准方程
    """

    # 计算斜率
    slope = (p2[1] - p1[1])/(p2[0]-p1[0])
    # 计算截距
    # x等于0处的点对应的y坐标即为截距
    # p1[1]-y = slope * p1[0]
    intercept = p2[1] - slope * p2[0]
    # slope * x + intercept = y
    # x + (1/slope)*intercept = (1/slope)*y
    # (1/slope)*y - x = (1/slope)*intercept
    # -(1/slope)*y + x = -(1/slope)*intercept

    return (1, -(1/slope), -(1/slope)*intercept)

def intersection(u1, u2, v1, v2):
    """
    计算两个线段的交点坐标：
    u1和u2是第一个线段的两个坐标
    v1和v2是第二个线段的两个坐标
    """

    a1, b1, c1 = standard_form(u1, u2)
    print(a1, b1, c1)
    a2, b2, c2 = standard_form(v1, v2)
    print(a2, b2, c2)
    matrix = np.array(((a1, b1), (a2, b2)))
    out = np.array((c1, c2))
    return np.linalg.solve(matrix, out)
```

输出的是两条线段所在直线的交点。但是，这一点可能不在任何一条线段上。

为了检测两条线段是否相交，需要检测它们所在直线的交点是否位于两对端点之间。我们可
以用距离来校验。

分别将直线交点与线段中的两个交点进行距离比较，如果与其中任意一个端点的距离小于线
段的长度，表明交点位于线段上。

```py
def do_segments_intersect(s1, s2):
    """
    判断两条线段s1和s2的交点是否在线段上
    """
    distance1 = distance(*s1)
    distance2 = distance(*s2)

    # 计算
    intersection_point = intersection(*s1, *s2)
    print(f"intersection point is {intersection_point}")

    u1, u2 = s1
    v1, v2 = s2

    return distance(intersection_point, u1) <= distance1 \
        and distance(intersection_point, u2) <= distance1 \
            and distance(intersection_point, v1) <= distance2 \
                and distance(intersection_point, v2) <= distance2
```

### 7.2.6 识别不可解方程组

并非每一个二维线性方程组都可以求解！如果我们把一个没有解的线性方程组传给 NumPy，
就会得到一个异常，所以需要处理这种情况。

当二维中的一对直线不平行时，它们会在某处相交。如果两条直线平行，那么它们将永远不
相交。

但是平行又分两种场景，一种是没有交点，另一种是有无限多个交点（两条直线重叠）。

我们可以传入两个平行的线性方程，测试下 NumPy 的 solve 方法：

```py
# 4x+2y=8
# 2x + y = 6
matrix = np.array(((2, 1), (4, 2)))
output = np.array((8, 6))
np.linalg.solve(matrix, output)
```

会输出以下错误：

```bash
Traceback (most recent call last):
  File "\asteroids_game\tools.py", line 62, in <module>
    np.linalg.solve(matrix, output)
    ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "\asteroids_game\.venv\Lib\site-packages\numpy\linalg\_linalg.py", line 452, in solve
    r = gufunc(a, b, signature=signature)
  File "\asteroids_game\.venv\Lib\site-packages\numpy\linalg\_linalg.py", line 145, in _raise_linalgerror_singular
    raise LinAlgError("Singular matrix")
numpy.linalg.LinAlgError: Singular matrix
```

NumPy 指出矩阵是错误的来源。矩阵

$
\begin{pmatrix}
    4 && 2\\
    2 && 1\\
\end{pmatrix}
$

称为**奇异矩阵**，这意味着线性方程组没有唯一的解。

由于我们的小行星游戏中坐标都是随机生成的，所以与激光平行的概率很低，暂时不考虑修
复平行场景，只是增加错误捕获处理。

```py
def do_segments_intersect(s1, s2):
    """
    判断两条线段s1和s2的交点是否在线段上
    """
    distance1 = distance(*s1)
    distance2 = distance(*s2)

    try:
        # 计算交点坐标
        intersection_point = intersection(*s1, *s2)
        print(f"intersection point is {intersection_point}")

        u1, u2 = s1
        v1, v2 = s2

        return distance(intersection_point, u1) <= distance1 \
            and distance(intersection_point, u2) <= distance1 \
                and distance(intersection_point, v1) <= distance2 \
                    and distance(intersection_point, v2) <= distance2

    except np.linalg.linalg.LinAlgError:
        # 如果发生异常，就表示平行了，返回false
        return False
```

### 7.2.7 练习

练习 7.11：编写一个 Python 函数 standard_form，该函数接收两个向量$v_1$和$v_2$并
找到通过这两个向量的直线：$ax+by=c$

```py
def standard_form(p1, p2):
    # ax + by = c
    # ax1 + by1 = c
    # ax2 + by2 = c
    # a(x1 -x2) = b(y2 - y1)
    # a/b = (y2-y2)/(x1-x2) => a=y2-y1, b=x1-x2
    # c = (y2-y1)x1 + (x1-x2)y1 = x1y2-x1y1 + x1y1-x2y1=x1y2-x2y1
    x1, y1 = p1
    x2, y2 = p2
    a = y2 - y1
    b = x1 - x2
    c = x1 * y2 - y1 * x2
    return (a, b, c)
```
