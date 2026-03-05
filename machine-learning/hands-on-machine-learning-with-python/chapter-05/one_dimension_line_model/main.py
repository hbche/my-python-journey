# from generate_data import generate_data
from plot_data import plot_data
import numpy as np
from line_regression import plot_mse

def plot():
    data = np.load('ch5_data.npz')
    X = data['X']
    T = data['T']
    # plot_data(X, T)
    plot_mse(X, T)

plot()