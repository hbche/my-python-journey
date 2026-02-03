from tools import plot_volume

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
plot_volume(volume, 0, 10)