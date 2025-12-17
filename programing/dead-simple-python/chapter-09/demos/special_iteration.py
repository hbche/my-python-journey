# specials = ['pumpkin spice latte', 'caramel macchiato', 'mocha cappucciono']

# first_iterator = specials.__iter__()
# specials_iterator = specials.__iter__()

# print(type(first_iterator))     # <class 'list_iterator'>

# item = first_iterator.__next__()
# print(item)     # pumpkin spice latte

# item = first_iterator.__next__()
# print(item)     # caramel macchiato

# specials = ['pumpkin spice latte', 'caramel macchiato', 'mocha cappucciono']

# first_iterator = iter(specials)
# second_iterator = iter(specials)

# print(type(first_iterator))     # <class 'list_iterator'>
# item = next(first_iterator)
# print(item)                     # pumpkin spice latte

# item = next(first_iterator)
# print(item)                     # caramel macchiato

# item = next(second_iterator)
# print(item)                     # pumpkin spice latte

# item = next(first_iterator)
# print(item)                     # mocha cappucciono

# next(first_iterator)            # raises StopIteration

# # 使用 while 遍历
# specials = ['pumpkin spice latte', 'caramel macchiato', 'mocha cappucciono']
# iterator = iter(specials)

# while True:
#     try:
#         item = next(iterator)
#     except StopIteration:
#         break
#     else:
#         print(item)

# 使用 for 循环遍历
specials = ['pumpkin spice latte', 'caramel macchiato', 'mocha cappucciono']

for item in specials:
    print(item)