# 定义集合
raffle = {'James', 'Denis', 'Simon'}
# 使用add方法想可变集合中追加元素
raffle.add('Daniel')
raffle.add('Denis')
print(raffle)   # {'James', 'Denis', 'Simon', 'Daniel'}

# 使用discard方法从可变集合中移除元素
raffle.discard('Simon')
print(raffle)   # {'Daniel', 'Denis', 'James'}