raffle = {'Kyle', 'Denis', 'Jason'}
# 创建不可变集合，记录过往获奖名单
pre_winners = frozenset({'Denis', 'Simon'})

# 使用 -= 运算符删除过往获奖者
raffle -= pre_winners
print(raffle)   # 打印删除后的抽奖名单  {'Kyle', 'Jason'}

winner = raffle.pop()
print(winner)