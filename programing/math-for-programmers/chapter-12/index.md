# 第 12 章 优化物理系统

目标

- 炮弹的模拟与可视化
- 利用导数求函数的最大值和最小值
- 模拟调试
- 可视化输入参数空间并进行模拟
- 实现梯度上升法，最大化多元函数

## 12.1 测试炮弹模拟器

用函数对导弹发射进行建模。研究导弹最远射程与发射角度的关系，以及求最远射程的导弹发射角度。

### 12.1.1 用欧拉方法建立模拟器

使用函数模拟导弹发射角度与射程、垂直高度和时间的关系

``` py
from math import cos, sin, pi

def trajectory(theta, speed=20, height=0, dt=0.01, g=-9.81):
    """
    trajectory: 模拟炮弹发射路径
    
    :param theta: 发射角度
    :param speed: 发射初始速度
    :param height: 初始发射高度
    :param dt: 时间变化单位
    :param g: 重力加速度
    """
    vx, vz = speed * cos(theta * pi / 180), speed * sin(theta * pi / 180)
    t, x, z = 0, 0, height
    ts, xs, zs = [t], [x], [z]

    while z >= 0:
        t += dt
        vz += g * dt
        ts.append(t)
        x += vx * dt
        z += vz *dt
        xs.append(x)
        zs.append(z)

    return ts, xs, zs
```

绘制函数：

``` py
import matplotlib.pyplot as plt
import numpy as np

def plot_function(f, xmin, xmax, **kwargs):
    ts = np.linspace(xmin, xmax, 1000)
    plt.plot(ts, [f(t) for t in ts], **kwargs)
```

绘制炮弹发射垂直高度和射程的可视化：

``` py
def plot_trajectories(*trajs, show_seconds=False):
    for traj in trajs:
        xs, zs = traj[1], traj[2]
        plt.plot(xs, zs)
        if show_seconds:
            second_indices = []
            second = 0
            for i, t in enumerate(traj[0]):
                if t >=second:
                    second_indices.append(i)
                    second += 1 
            plt.scatter([xs[i] for i in second_indices], [zs[i] for i in second_indices])

    xl = plt.xlim()
    plt.plot(plt.xlim(), [0, 0], c='k')
    plt.xlim(*xl)

    width = 7
    coords_height = (plt.ylim()[1] - plt.ylim()[0])
    coords_width = (plt.xlim()[1] - plt.xlim()[0])
    plt.gcf().set_size_inches(width, width * coords_height / coords_width)

    plt.show()
```

测试模拟炮弹发射射程和垂直距离的函数：

``` py
from trajectory import trajectory, plot_trajectories

plot_trajectories(trajectory(45), trajectory(60))
```

### 12.1.2 测量弹道的属性

``` py
def hang_time(traj):
    """
    landing_position: 导弹的滞空时间
    
    :param traj: 说明
    """
    return traj[0][-1]

def landing_position(traj):
    """
    hand_position: 导弹的最远射程
    
    :param traj: 说明
    """
    return traj[1][-1]

def max_height(traj):
    """
    max_height: 导弹的最高射程
    
    :param traj: 说明
    """
    return max(traj[2])
```

### 12.1.3 探索不同发射角度

可视化角度与射程的关系：

``` py
from trajectory import trajectory
from measure_property import hand_position
import matplotlib.pyplot as plt

def plot_angles():
    # 每隔5°计算对应的射程：
    angles = range(0, 90, 5)
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.xlabel('θ')
    plt.ylabel('落地位置')
    plt.title('发射角度与最大落地距离之间的关系')
    plt.scatter(angles, [hand_position(trajectory(angle)) for angle in angles])
    plt.show()
```

## 12.2 计算最佳射程


### 12.2.1 求炮弹射程与发射角度的函数

炮弹飞行的水平距离等于 $v_x * t$，关键取决于飞行时间 t。
t又取决于垂直飞行。

``` py
# 绘制垂直高度与时间之间的函数
trj = trajectory(45)
ts, zs = trj[0], trj[2]
plt.xlabel('t')
plt.ylabel('z')

plt.plot(ts, zs)
plt.show()
```

我们知道 $x''(t) = g$，我们知道z函数的二次求导是重力加速度。我们知道初始速度$v_z$，对z函数进行第一次积分就可以得到当前时刻的速度。

$$
z'(t) = z'(0) + \int_{0}^{t} gdt = |v| \cdot sin(θ) + g \cdot t
$$

第二次积分：

$$
z(t) = z(0) + \int_{0}^{t} z'(t) \cdot dt = \int_{0}^{t} |v| \cdot sin(θ) + g \cdot dt = |v| \cdot sin(θ) \cdot t + \frac{g\cdot t ^ 2}{2}
$$

因此，我们推理出来垂直距离与时间t的函数：

``` py
def z(t, speed=20, theta=45):
    """
    z: 滞空时间与垂直高度之间的函数
    
    :param t: 滞空时间
    :param speed: 初始速度
    :param theta: 初始角度
    """
    return speed * sin(theta * pi / 180) * t + ((-9.81) * t **2 )/2

plot_function(z, 0, 2.9)
```

我们的目标是找到 $z(t) = 0$时的t的值。即：$v\cdot sin(θ) \cdot t + \frac{g \cdot t ^ 2}{2}=0$。求得：t的值为 $t=-\frac{v\cdot sin(θ)}{g} \pm \frac{v\cdot sin(θ)}{g}$。因而 t 的最大值为 $-\frac{2\cdot v \cdot sin(θ)}{g}$。继而可以推出射程的函数为 $r(θ)=-\frac{2\cdot v^2 \cdot sin(θ) \cdot cos(θ)}{g}$。

我们绘制发射角度与射程之间的函数：

``` py
def r(theta, speed=20):
    """
    r: 射程与发射角度之间的函数
    
    :param speed: 发射速度
    :param theta: 发射角度
    """

    return (-2 * speed * speed / -9.81) * sin(theta * pi / 180) * cos(theta * pi / 180) 

plot_function(r, 0, 90)
```

### 12.2.2 求最大射程

