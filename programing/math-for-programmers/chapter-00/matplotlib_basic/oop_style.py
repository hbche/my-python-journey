import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))  # fig是画板，ax是画布
ax.plot([1, 2, 3], [2, 4, 1])   # 在 ax 上画线
ax.set_title("OOP Style")
ax.set_xlabel("X axis")
ax.set_ylabel("y axis")
ax.grid(True)
plt.show()