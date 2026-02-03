# 绘图工具
import matplotlib.pyplot as plt
import numpy as np

def plot_function(f, tmin, tmax, tlabel=None,xlabel=None, axes=False, **kwargs):
    # 将时间间隔平均等分成1000分的区间
    ts = np.linspace(tmin, tmax, 1000)
    if tlabel:
        plt.xlabel(tlabel, fontsize=18)
    if xlabel:
        plt.ylabel(xlabel, fontsize=18)
    # 绘制函数关于时间变化的折线
    plt.plot(ts, [f(t) for t in ts], **kwargs)
    if axes:
        total_t = tmax-tmin
        plt.plot([tmin-total_t/10, tmax+total_t/10], [0, 0], c='k', linewidth=1)
        plt.xlim(tmin-total_t/10, tmax+total_t/10)
        xmin, xmax = plt.ylim()
        plt.plot([0, 0], [xmin, xmax], c='k', linewidth=1)
        plt.ylim(xmin, xmax)

def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)
    
def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)
    

def secant_line(f, x1, x2):
    """
    secant_line: 计算两点之间的割线方程
    
    :param f: 指定函数
    :param x1: 割线的第一个点的x坐标
    :param x2: 割线的第二个点的x坐标
    """
    def line(x):
        return (f(x2)-f(x1))/(x2-x1)*(x-x1)+f(x1)
    return line

def average_flow_rate(f, x1, x2):
    """
    average_flow_rate: 平均流速
    
    :param f: 说明
    :param x1: 说明
    :param x2: 说明
    """
    return (f(x1) - f(x2))/(x1-x2)

def plot_secant(f, x1, x2, color='k'):
    """
    plot_secant 的 Docstring
    
    :param f: 说明
    :param x1: 说明
    :param x2: 说明
    :param color: 说明
    """
    line = secant_line(f, x1, x2)
    plot_function(line, x1, x2, c=color)
    plt.scatter([x1, x2], [f(x1), f(x2)], c=color)


def interval_flow_rates(f, t1, t2, dt):
    """
    interval_flow_rates: 计算给定时间段内指定时间间隔的每一段平均速率
    
    :param f: 说明
    :param t1: 说明
    :param t2: 说明
    :param dt: 说明
    """
    return [
        (t, average_flow_rate(f, t, t+dt))
        for t in np.arange(t1, t2, dt)
    ]

def plot_interval_flow_rates(f, t1, t2, dt):
    """
    plot_interval_flow_rates: 以散点展示间隔平均流速图
    
    :param f: 说明
    :param t1: 说明
    :param t2: 说明
    :param dt: 说明
    """
    series = interval_flow_rates(f, t1, t2, dt)
    times, rates = [], []
    for time, rate in series:
        times.append(time)
        rates.append(rate)
    plt.scatter(times, rates)

def instantaneous_flow_rate(v, t, digits=6):
    """
    instantaneous_flow_rate: 以指定精度计算某个时刻的瞬时速率
    
    :param v: 说明
    :param t: 说明
    :param digits: 说明
    """
    tolerance = 10 ** (-digits)
    h=1
    approx = average_flow_rate(v, t-h, t+h)
    for _ in range(0, 2 * digits):
        h = h/10
        next_approx =average_flow_rate(v, t-h, t+h)
        if abs(next_approx - approx) < tolerance:
            return round(next_approx, digits)
        else:
            approx = next_approx

    raise Exception('Derivative did not converge')  # 如果超过了最大的迭代次数，就表示程序没有收敛到一个结果


def get_flow_rate_function(v):
    """
    get_flow_rate_function: 基于流体体积变化，计算某个时刻的瞬时速率
    
    :param v: 说明
    """
    def flow_rate_function(t):
        return instantaneous_flow_rate(v, t)
    return flow_rate_function

def small_volume_change(q, t, dt):
    """
    small_volume_change: 计算瞬时体积变化
    
    :param q: 瞬时流速函数
    :param t: 时刻，用于计算瞬时速率
    :param dt: 经过的时间
    """
    return q(t) * dt