from die import Die
import plotly.express as px

# 创建骰子列表
dies = [Die(), Die()]

# 将掷骰子的结构存储在此列表中
results = []
while len(results) < 1000:
    # 将所有骰子点数相乘
    total = 1
    for die in dies:
        total *= die.roll()
    results.append(total)
    
# 分析结果
frequencies = []
# 骰子面数对应列表
max_side = 1
min_side = 1
for die in dies:
    max_side *= die.num_sides
# 生成 min_side ~ max_side 之间的整数列表
sides = range(min_side, max_side + 1)
frequencies = [results.count(side) for side in sides]
    
    
# 对结果进行可视化
# 设置样式
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=sides, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()