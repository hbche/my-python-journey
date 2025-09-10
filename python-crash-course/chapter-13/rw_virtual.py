import matplotlib.pyplot as plt
from random_walk import RandomWalk

random_walker = RandomWalk()

while True:
    random_walker.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(random_walker.x_values, random_walker.y_values, s=10)
    ax.set_aspect('equal')

    plt.show()
    
    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break