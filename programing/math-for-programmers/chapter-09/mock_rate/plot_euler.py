import matplotlib.pyplot as plt
import numpy as np

def calculate_rate(v, a, dt):
    def instantaneous_rate():

    return instantaneous_rate
    
def approx_s(v, ):


def mock_euler(v, a, t0, t1):
    vx, vy = v
    times = np.arange(t0, t1, 1)
    x_rates = [vx for _ in times]
    y_rates = [vy + a * t for t in times]
    plt.scatter(x_rates, y_rates)
    plt.show()

mock_euler((1, 0), 0.2, 0, 10)
