import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    random_walker = RandomWalk(50_000)
    random_walker.fill_walk()

    plt.style.use('classic')
    # 调整屏幕尺寸
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(len(random_walker.x_values))
    # 给随机路径的点设置着色，越往后出现的点颜色越深
    ax.scatter(random_walker.x_values, random_walker.y_values, s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none")
    ax.set_aspect('equal')
    # 隐藏坐标
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break