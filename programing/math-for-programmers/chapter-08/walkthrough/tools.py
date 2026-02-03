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
    plt.show()
        

def plot_volume(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="volume (bbl)", axes=axes, **kwargs)
    
def plot_flow_rate(f, tmin, tmax, axes=False, **kwargs):
    plot_function(f, tmin, tmax, tlabel="time (hr)", xlabel="flow rate (bbl/hr)", axes=axes, **kwargs)
    

        