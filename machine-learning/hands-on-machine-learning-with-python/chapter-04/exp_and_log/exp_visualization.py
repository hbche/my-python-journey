import matplotlib.pyplot as plt
import numpy as np


def exp_visualization(a, **kwargs):
    X = np.linspace(-4, 4, 100)
    Y = a**X
    plt.plot(X, Y, **kwargs)


plt.figure(figsize=(5, 5))
exp_visualization(2, c="black", linewidth=3, label="$y=2^x$")
exp_visualization(3, c="cornflowerblue", linewidth=3, label="$y=3^x$")
exp_visualization(0.5, c="gray", linewidth=3, label="$y=0.5^x$")
plt.grid(True)
plt.xlim(-4, 4)
plt.ylim(-2, 6)
plt.legend(loc="lower right")
plt.show()
