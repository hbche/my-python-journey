import matplotlib.pyplot as plt
import numpy as np


def plot_log():
    x = np.linspace(0, 1.0, 100)
    y = np.log(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, linestyle="-", color="b", label="data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Plot from provided data")
    plt.grid(True, linestyle=":", alpha=0.7)
    plt.legend()
    plt.show()


plot_log()
