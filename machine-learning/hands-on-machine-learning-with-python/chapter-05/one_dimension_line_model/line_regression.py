import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def mse(X, Y, W):
    """
    mse: 均方误差
    """
    f = W[0] * X + W[1]
    return np.mean((f - Y)**2)

def plot_mse(X, T):
    xn = 100
    w0_range = [-25, 25]
    w1_range = [120, 170]
    w0 = np.linspace(w0_range[0], w0_range[1], xn)
    w1 = np.linspace(w1_range[0], w1_range[1], xn)
    ww0, ww1 = np.meshgrid(w0, w1)
    # 初始化w0、w1对应的均方误差列表
    J = np.zeros((xn, xn))

    for i in range(xn):
        for j in range(xn):
            J[i, j] = mse(X, T, (w0[i], w1[j]))

    fig = plt.figure(figsize=(9.5, 4))
    plt.subplots_adjust(wspace=0.5)

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.plot_surface(ww0, ww1, J, rstride=10, cstride=10, alpha=0.3, color='blue', edgecolor='black')
    ax.set_xticks([-20, 0, 20])
    ax.set_xlabel('w0')
    ax.set_ylabel('w1')
    ax.set_yticks([120, 140, 160])
    ax.view_init(20, -60)

    fig.add_subplot(1, 2, 2)
    cont = plt.contour(ww0, ww1, J, 30, colors='black', levels=[100, 1000, 10000, 100000])
    cbar = plt.colorbar(cont, format='%d')
    cbar.ax.tick_params(labelsize=8)
    cbar.formatter
    plt.grid(True)

    plt.show()


