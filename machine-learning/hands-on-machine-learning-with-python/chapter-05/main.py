import numpy as np
import matplotlib.pyplot as plt

def gauss(x, mu, sigma):
    return np.exp(-((x - mu) ** 2 / (2 * sigma ** 2)))

def plotGauss():
    M = 4
    plt.figure(figsize = (4, 4))
    mu = np.linspace(5, 30, M)
    xb = np.linspace(X_min, X_max, 100)
    