import matplotlib.pyplot as plt

# 就像在MATLIB 中一样，直接使用plt.*
plt.figure(figsize=(8, 4))  # 创建画布
plt.plot([1, 2, 3], [2, 4, 1])  # 在第一张画布上画线
plt.title("MATLIB Style")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.grid(True)
plt.show()
