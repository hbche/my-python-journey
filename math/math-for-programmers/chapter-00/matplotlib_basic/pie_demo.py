# 绘制饼图
import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()