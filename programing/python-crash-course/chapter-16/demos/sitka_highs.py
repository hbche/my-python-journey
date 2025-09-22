from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('data/wuhan_july_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# # 获取表头以及索引
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
    
# 读取每日的最高温度、最低温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[0], r'%Y%m%d')
    high = int(row[2])
    low = int(row[3])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
    
# 绘制武汉7月份每日对应的最高温度
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
# 给两条连线区域着色
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title("Daily High Temperature of Wuhan, July 2025", fontsize=24)
ax.set_xlabel("Date", fontsize=14)
ax.set_ylabel("Temperature", fontsize=14)
# 绘制倾斜的日期标签
fig.autofmt_xdate()
ax.tick_params(labelsize=16)
ax.set_aspect('equal')

# plt.show()
plt.savefig('sitka_hights_fill_between.png', bbox_inches="tight")