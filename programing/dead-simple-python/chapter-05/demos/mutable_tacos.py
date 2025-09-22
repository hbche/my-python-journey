import copy

class Taco:
    
    def __init__(self, toppings):
        # 将参数传递进来的默认配料进行复制，防止类中的方法篡改外部的参数
        self.ingredients = copy.copy(toppings)
        
    def add_sauce(self, sauce):
        self.ingredients.append(sauce)
        
default_toppings = ["Lettuce", "Tomato", "Beef"]
mild_taco = Taco(default_toppings)
hot_taco = copy.deepcopy(mild_taco)
hot_taco.add_sauce("Salsa")

print(f"Hot: {hot_taco.ingredients}")       # Hot: ['Lettuce', 'Tomato', 'Beef', 'Salsa']
print(f"Mild: {mild_taco.ingredients}")     # Mild: ['Lettuce', 'Tomato', 'Beef']
print(f"Default: {default_toppings}")       # Default: ['Lettuce', 'Tomato', 'Beef']