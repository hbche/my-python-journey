# 顾客所点的披萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述顾客所点的披萨
print(f'You ordered a {pizza['crust']}-crust pizza with the following toppings:')
for topping in pizza['toppings']:
    print(f'\t{topping}')
    
# You ordered a thick-crust pizza with the following toppings:
#         mushrooms
#         extra cheese