from random_walk import RandomWalk
import plotly.express as px

# 生成随机游走的数据
rw = RandomWalk()
rw.fill_walk()

# 使用 plotly 绘制随机游走的点数
title = 'Random Walk Results'
fig = px.scatter(rw.x_values, rw.y_values, title=title)
fig.show()