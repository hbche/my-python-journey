from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    """
    生成一个无限迭代器
    """
    
    while True:
        # 没有return逻辑，将变为无限迭代器
        vehicle = choice(vehicles)
        color = choice(colors)
        try:
            yield f"{color} {vehicle}"
        # 通过捕获 GeneratorExit 异常，可以实现在迭代器关闭的时候做一些其他逻辑
        except(GeneratorExit):
            print("No more vehicles.")
        raise

def car_wash(traffic, limit):
    count = 0
    for count, vehicle in enumerate(traffic, start=1):
        print(f"Washing {vehicle}.")
        
        if count + 1 > limit:
            traffic.close()
            
car_wash(traffic_generator(), 10)