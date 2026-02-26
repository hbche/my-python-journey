from math import cos, sin, pi
import matplotlib.pyplot as plt

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
