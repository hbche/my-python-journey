from trajectory import trajectory
from measure_property import landing_position
import matplotlib.pyplot as plt

def plot_angles():
    # 每隔5°计算对应的射程：
    angles = range(0, 90, 5)
    plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
    plt.xlabel('θ')
    plt.ylabel('落地位置')
    plt.title('发射角度与最大落地距离之间的关系')
    plt.scatter(angles, [landing_position(trajectory(angle)) for angle in angles])
    plt.show()