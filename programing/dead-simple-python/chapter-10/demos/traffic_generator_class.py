from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

class Traffic:
    """
    定义迭代器类，模拟车流量
    """
    
    def __iter__(self):
        """
        不需要初始化器，因为没有实例属性。定义返回self的__iter__()特殊方法，是这个类变成可迭代的
        """
        return self

    def __next__(self):
        """
        为这个类定义__next__()方法，作为迭代器
        """
        vehicle = choice(vehicles)
        
        if vehicle is None:
            raise StopIteration
        
        color = choice(colors)
        
        return f"{color} {vehicle}"
    
count = 0
for count, vehicle in enumerate(Traffic(), start=1):
    print(f"Wait for {vehicle}...")
    
print(f"Merged after {count} vehicles!")

# Wait for white motorcycle...
# Wait for green motorcycle...
# Merged after 2 vehicles!