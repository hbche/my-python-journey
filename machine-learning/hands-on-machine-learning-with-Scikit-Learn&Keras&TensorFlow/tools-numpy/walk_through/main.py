import matplotlib.pyplot as plt
import numpy as np

x_coords = np.arange(0, 1024)
y_coords = np.arange(0, 768)
X, Y = np.meshgrid(x_coords, y_coords)
data = np.sin(X * Y / 40.5)

fig = plt.figure(1, figsize=(7, 6))
plt.imshow(data, cmap="hot")
plt.show()
