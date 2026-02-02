import numpy as np
from vector import distance

# def standard_form(p1, p2):
#     """
#     根据线段端点，输出直线的标准方程
#     """
    
#     # 计算斜率
#     slope = (p2[1] - p1[1])/(p2[0]-p1[0])
#     # 计算截距
#     # x等于0处的点对应的y坐标即为截距
#     # p1[1]-y = slope * p1[0]
#     intercept = p2[1] - slope * p2[0]
#     # slope * x + intercept = y
#     # x + (1/slope)*intercept = (1/slope)*y
#     # (1/slope)*y - x = (1/slope)*intercept
#     # -(1/slope)*y + x = -(1/slope)*intercept
    
#     return (1, -(1/slope), -(1/slope)*intercept)

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


def intersection(u1, u2, v1, v2):
    """
    计算两个线段对应直线的交点坐标：
    u1和u2是第一个线段的两个坐标
    v1和v2是第二个线段的两个坐标
    """
    
    a1, b1, c1 = standard_form(u1, u2)
    print(f"{a1}x + {b1}y = {c1}")
    a2, b2, c2 = standard_form(v1, v2)
    print(f"{a2}x + {b2}y = {c2}")
    matrix = np.array(((a1, b1), (a2, b2)))
    out = np.array((c1, c2))
    return np.linalg.solve(matrix, out)


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
    
# 4x+2y=8
# 2x + y = 6
matrix = np.array(((2, 1), (4, 2)))
output = np.array((8, 6))
np.linalg.solve(matrix, output)