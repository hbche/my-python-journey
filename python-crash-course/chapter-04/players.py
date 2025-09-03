# # 切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])         # ['charles', 'martina', 'michael']

# # 省略第一个索引
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:4])              # ['charles', 'martina', 'michael', 'florence']

# # 省略结尾索引
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:])          # ['michael', 'florence', 'eli']

# # 负数索引
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])          # ['michael', 'florence', 'eli']

# # 指定步长
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[::2])          # ['charles', 'michael', 'eli']

# 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("There are the first three players on my team:")
for player in players[:3]:
    print(player.title())