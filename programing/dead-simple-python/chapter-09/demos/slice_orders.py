orders = [
    "caramel macchiato", 
    "drip",
    "pumpkin spice latte", 
    "drip",
    "cappuccino",
    "americano",
    "mocha latte",
]

# three_four_five = orders[3:6]
# print(three_four_five)      # ['drip', 'cappuccino', 'americano']

# after_third = orders[4:]
# print(after_third)          # ['cappuccino', 'americano', 'mocha latte']

# next_two = orders[:2]
# print(next_two)             # ['caramel macchiato', 'drip']

# print(orders[-1])           # mocha latte

# # 获取末尾的3个元素
# last_three = orders[-3:]
# print(last_three)           # ['cappuccino', 'americano', 'mocha latte']

# # 指定步长为2，实现每个一个元素取一项
# every_order = orders[1::2]
# print(every_order)          # ['drip', 'drip', 'americano']

# reverse = orders[::-1]
# print(reverse)              # ['mocha latte', 'americano', 'cappuccino', 'drip', 'pumpkin spice latte', 'drip', 'caramel macchiato'] 

order_copy = orders[:]
orders.append('the end item')
print(order_copy)           # ['caramel macchiato', 'drip', 'pumpkin spice latte', 'drip', 'cappuccino', 'americano', 'mocha latte']
print(orders)               # ['caramel macchiato', 'drip', 'pumpkin spice latte', 'drip', 'cappuccino', 'americano', 'mocha latte', 'the end item']