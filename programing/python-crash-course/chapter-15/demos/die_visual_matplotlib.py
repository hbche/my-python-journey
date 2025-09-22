from die import Die
import matplotlib.pyplot as plt

dies = [Die(), Die()]

min_side = len(dies)
max_side = 0
for die in dies:
    max_side += die.num_sides
    
# 记录数据
results = []
while len(results) < 1000:
    total = 0
    for die in dies:
        total += die.roll()
    results.append(total)

# 分析数据
sides = range(min_side, max_side + 1)
frequencies = [results.count(side) for side in sides]
print(frequencies)

# 绘制数据
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig, ax = plt.subplots()
ax.bar(sides, frequencies)
ax.set_title(title, fontsize=24)
ax.set_xlabel(labels['x'], fontsize=14)
ax.set_ylabel(labels['y'], fontsize=14)

plt.show()