# 通过生成二维数组，生成棋盘
board = [['*'] * 3 for _ in range(3)]

# 模拟第一个子
board[1][0] = 'X'

# 打印棋盘
for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")
    
# 结果：
# X * *
# X * *
# X * *