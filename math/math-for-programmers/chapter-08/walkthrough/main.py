import matplotlib.pyplot as plt
from tools import plot_volume, plot_secant, plot_interval_flow_rates, plot_function, get_flow_rate_function

def volume(t):
    """
    volume：石油体积关于时间的变化函数
    
    :param t: 时间参数
    """
    return (t-4)**3 / 64 + 3.3

def flow_rate(t):
    """
    flow_rate：石油流速关于时间的变化函数
    
    :param t: 时间参数
    """
    return 3*(t-4)**2 / 64

# 根据流体体积随时间变化的函数，绘制0~10单位时间内，流体体积变化曲线图
# plot_volume(volume, 0, 10)
# plot_secant(volume,1,4)
# plot_secant(volume,6,8)

# # 测试按照1小时进行计算平均速率与实际速率函数的偏差
# plot_volume(flow_rate, 0, 10)
# plot_interval_flow_rates(volume, 0, 10, 0.5)

# plot_function(flow_rate, 0, 10)
plot_function(get_flow_rate_function(volume), 0, 10)


plt.show()