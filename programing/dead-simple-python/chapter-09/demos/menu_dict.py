menu = {"drip": 1.95, "cappuccino": 2.95}

# 通过键来访问各个元素
print(menu["drip"])     # 1.95

# 添加元素
menu['americano'] = 2.49
print(menu)     # {'drip': 1.95, 'cappuccino': 2.95, 'americano': 2.49}

# 删除指定元素
del menu['americano']
print(menu)     # {'drip': 1.95, 'cappuccino': 2.95}