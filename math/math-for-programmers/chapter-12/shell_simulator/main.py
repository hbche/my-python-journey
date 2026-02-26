from trajectory import trajectory, plot_trajectories
import matplotlib.pyplot as plt
from plot_function import plot_function
from max_hang_time import z, r

# # 绘制45度和60度发射角中射程与发射高度的关系
# plot_trajectories(trajectory(45), trajectory(60))

# from explore_luncher_angle import plot_angles

# # 绘制发射角度与最大射程之间的关系
# plot_angles()


# # 绘制 20、45、60、80角度对应的最远射程和最大高度之间的关系
# thetas = [20, 45, 60, 80]
# plot_trajectories(*(trajectory(theta) for theta in thetas), show_seconds=True)

# 绘制0到180度之间，角度和发射时间的关系

# # 绘制垂直高度与时间之间的函数
# trj = trajectory(45)
# ts, zs = trj[0], trj[2]
# plt.xlabel('t')
# plt.ylabel('z')

# plt.plot(ts, zs)
# plt.show()

# plot_function(z, 0, 2.9)
plot_function(r, 0, 90)