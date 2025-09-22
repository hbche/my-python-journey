# 使用while循环从列表中移除所有特定值
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# 使用 while 循环移除列表中的所有猫，直到列表中不再有猫为止
while 'cat' in pets:
    pets.remove('cat')
print(pets)