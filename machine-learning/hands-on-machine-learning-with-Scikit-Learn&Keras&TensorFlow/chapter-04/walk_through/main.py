import matplotlib.pyplot as plt
import numpy as np
from linear_regression import (
    calc_theta,
    calc_theta_by_scikit,
    generate_data,
    plot_data,
    plot_regression,
)

X, Y = generate_data()
m = 100
X_b = np.c_[np.ones((m, 1)), X]  # 添加 x_0 = 1 的偏置项
best_theta = calc_theta(X_b, Y)
print(f"Best Theta: {best_theta.reshape(2)}")
#  [4.51359766 2.98323418]
best_theta_2 = calc_theta_by_scikit(X_b, Y)
print(f"Best theta by sklearn: {best_theta_2}")
# Best theta by sklearn: (array([4.51359766]), array([[0.        , 2.98323418]]))

fig, ax = plt.subplots()
plot_data(ax, X, Y)
plot_regression(ax, X, best_theta.reshape(2))

plt.show()
