# from generate_data import generate_data
# from line_regression import plot_mse
# from gradient_descent import calculate_gradient
import matplotlib.pyplot as plt
import numpy as np
from analytical_solution import analytical_solution
from gradient_descent import gradient_descent
from line_regression import mse

data = np.load("ch5_data.npz")
X = data["X"]
T = data["T"]
# # 计算 W 为[10, 165]对应的梯度
# dw = calculate_gradient(X, T, [10, 165])
# print(np.round(dw, 1))

w0, w1, *_ = gradient_descent(X, T)
print(f"Gradient W: [{w0}, {w1}]")
print(f"Gradient MSE: {mse(X, T, [w0, w1])}")

w_solution = analytical_solution(X, T)
print(f"Analytical Solution W=[{w_solution[0]}, {w_solution[1]}]")
print(f"Analytical Solution MSE: {mse(X, T, w_solution)}")


def line(x, w):
    return x * w[0] + w[1]


fig, ax = plt.subplots(figsize=(4, 4))
ax.set_title("Height - Age")
ax.set_xlabel("Age")
ax.set_ylabel("Height")
ax.set_xlim((4, 30))
ax.plot(
    X,
    T,
    marker="o",
    linestyle="None",
    markeredgecolor="black",
    color="cornflowerblue",
)

ax.plot(X, np.array([line(x_i, [w0, w1]) for x_i in X]), color="red")
ax.plot(X, np.array([line(x_i, w_solution) for x_i in X]), color="blue")
ax.grid(True)
plt.show()
