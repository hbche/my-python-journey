import matplotlib.pyplot as plt
import numpy as np
from optimizer import RMSProp

# 使用等高线绘制函数 $f(x,y)=\frac{1}{20}x^2+y^2$的梯度


def f(x, y):
    return x**2 / 20.0 + y**2


def df(x, y):
    return x / 10.0, 2.0 * y


def move_points():
    init_pos = (-7.0, 2.0)
    params = {}
    params["x"], params["y"] = init_pos[0], init_pos[1]
    grads = {}
    grads["x"], grads["y"] = 0, 0

    x_history = []
    y_history = []
    optimizer = RMSProp(ratio=0.9, learning_rate=1.0)

    for i in range(20):
        x_history.append(params["x"])
        y_history.append(params["y"])

        grads["x"], grads["y"] = df(params["x"], params["y"])
        optimizer.update(params, grads)

    return x_history, y_history


# 绘制等高线
def plot_contour():
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    # for simple contour line
    mask = Z > 7
    Z[mask] = 0

    # plot
    # plt.subplot(2, 2, 1)
    plt.figure(figsize=(8, 6))
    x_history, y_history = move_points()
    plt.plot(x_history, y_history, "o-", color="red")
    plt.contour(X, Y, Z)
    plt.ylim(-10, 10)
    plt.xlim(-10, 10)
    plt.plot(0, 0, "+")
    # colorbar()
    # spring()
    plt.title("SGD")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.show()


if __name__ == "__main__":
    plot_contour()
