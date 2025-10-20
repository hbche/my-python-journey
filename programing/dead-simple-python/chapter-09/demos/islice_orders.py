from itertools import islice

menu = {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}
# 在字典的items视图中，从索引0开始到索引为3的范围内，每各一个元素取一个
menu = dict(islice(menu.items(), 0, 3, 2))
print(menu)     # {'drip': 1.95, 'americano': 2.49}