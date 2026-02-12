import matplotlib.pyplot as plt
import numpy as np


def u(x, y):
    return 0.5 * (x**2 + y**2)


def scalar_field_contour(f, xmin, xmax, ymin, ymax, levels=None):

    fv = np.vectorize(f)

    X = np.arange(xmin, xmax, 0.1)
    Y = np.arange(ymin, ymax, 0.1)
    X, Y = np.meshgrid(X, Y)

    # https://stackoverflow.com/a/54088910/1704140
    Z = fv(X, Y)

    fig, ax = plt.subplots()
    CS = ax.contour(X, Y, Z, levels=levels)
    ax.clabel(CS, inline=1, fontsize=10, fmt="%1.1f")
    plt.xlabel("x")
    plt.ylabel("y")
    fig.set_size_inches(7, 7)
    plt.show()


scalar_field_contour(u, -10, 10, -10, 10, levels=[10, 20, 30, 40, 50, 60])
