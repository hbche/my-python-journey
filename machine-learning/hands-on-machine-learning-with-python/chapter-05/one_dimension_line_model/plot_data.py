import matplotlib.pyplot as plt
import numpy as np

def plot_data(X, T):
    """
    plot_data: 绘制数据分布图
    
    :param X: 年龄数据
    :param T: 身高数据
    """
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_title('Height - Age')
    ax.set_xlabel('Age')
    ax.set_ylabel('Height')
    ax.set_xlim((4, 30))
    ax.plot(X, T, marker='o', linestyle='None', markeredgecolor='black', color='cornflowerblue')
    ax.grid(True)

    plt.show()