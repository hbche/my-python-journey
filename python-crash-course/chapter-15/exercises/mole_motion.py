# 练习15.3：分子运动　修改rw_visual.py，将其中的ax.scatter()替换为ax.plot()。
# 为了模拟花粉在水滴表面的运动路径，向plt.plot()传递rw.x_values和rw.y_values，并指定实参linewidth。
# 请使用5000个点而不是50 000个点，以免绘图中的点过于密集。
from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """模拟随机游走"""
    
    def __init__(self, number_points=5000):
        self.x_values = [0]
        self.y_values = [0]
        self.number_points = number_points
        
    def fill_walk(self):
        while len(self.x_values) < self.number_points:
            # 随机生成游走的方向
            direction = choice([(1, 1), (1, -1), (-1, -1), (-1, 1)])
            # 随机生成游走的步长
            step = choice(list(range(1, 7)))
            # 生成下一个坐标
            x = self.x_values[-1] + step * direction[0]
            self.x_values.append(x)
            y = self.y_values[-1] + step * direction[1]
            self.y_values.append(y)
            
random_walk = RandomWalk()
random_walk.fill_walk()

fig, ax = plt.subplots()
ax.plot(random_walk.x_values, random_walk.y_values, linewidth=1)
ax.set_title("Melo Motion Plot", fontsize=24)
ax.set_aspect('equal')

plt.show()