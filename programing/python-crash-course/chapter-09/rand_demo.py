from random import randint
from random import choice

# 生成指定范围内的整数，包含范围的起点和终点
rand_int_num = randint(1, 6)
print(rand_int_num)

choice_list = ['apple', 'banana', 'orange', 'pear']
# 从列表中随机选择一个元素
rand_choice = choice(choice_list)
print(rand_choice)