# 演示具名元组的使用
from collections import namedtuple

CoffeeOrder = namedtuple("CoffeeOrder", ("item", "addons", "to_go"))

order = CoffeeOrder("pumpkin spice latte", ('whipped cream', ), True)
print(order.item)       # pumpkin spice latte
print(order[2])         # True