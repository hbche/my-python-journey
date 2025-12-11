from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    """
    生成器函数，构建一个无限迭代器 
    """
    while True:
        vehicle = choice(vehicles)
        # if vehicle is None:
        #     return
        
        color = choice(colors)
        yield f"{color} {vehicle}"
        
def car_wash(traffic, limit):
    """
    接受一个无限迭代器，在迭代limit次数之后，关闭迭代器
    """
    count = 0
    for vehicle in traffic:
        print(f"Washing {vehicle}.")
        count += 1
        if count >= limit:
            traffic.close()
            
# 传入无限迭代器
queue = traffic_generator()
car_wash(queue, 10)
# queue迭代器已经在car_wash函数中被关闭了，所以后续不再支持迭代，继续迭代的话会触发 StopIteration。
next(queue)