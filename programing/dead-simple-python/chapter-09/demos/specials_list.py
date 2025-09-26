# 演示列表使用
specials = ["pumkin spice latte", "caramel macchiato", "mocha cappuccino"]

print(specials[1])  # caramel macchiato

drink = specials.pop() # 移除最后一元素，并返回该元素
print(drink)    # mocha cappuccino
print(specials) # ['pumkin spice latte', 'caramel macchiato']

drink = specials.pop(1) # 删除索引为1的元素，并返回该元素
print(drink)    # caramel macchiato
print(specials) # ['pumkin spice latte']

specials.append('cold brew')    # 在列表结尾追加元素
print(specials) # ['pumkin spice latte', 'cold brew']

specials.insert(1, "americano") # 在索引为1的位置插入指定的元素
print(specials) # ['pumkin spice latte', 'americano', 'cold brew']