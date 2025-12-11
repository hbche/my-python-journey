from random import choice

colors = ['red', 'green', 'blue', 'silver', 'white', 'black']
vehicles = ['car', 'truck', 'semi', 'motorcycle', None]

def traffic_generator():
    while True:
        vehicle = choice(vehicles)
        color = choice(colors)
        try:
            yield f"{color} {vehicle}"
        except ValueError:
            # 跳过指定车辆，跳过逻辑又上层函数控制
            print(f"Skipping {color} {vehicle}...")
            continue
        except GeneratorExit:
            print("No more vehicles.")
            raise
        
def wash_vehicle(vehicle):
    # 如果当前车辆包含 semi ，则抛出异常，交由上层函数处理
    if 'semi' in vehicle:
        raise ValueError("Cannot wash vehicle.")
    print(f"Washing {vehicle}.")
            
            
def car_wash(traffic, limit):
    count = 0
    for vehicle in traffic:
        # 此处捕获 wash_vehicle抛出的 ValueError，通过traffic.throw(ValueError)，将异常传递到生成器内部，触发ValueError，实现skip逻辑
        try:
            wash_vehicle(vehicle)
        except Exception as e:
            traffic.throw(e)
        else:
            count += 1
            
        if count >= limit:
            traffic.close()
            
car_wash(traffic_generator(), 10)
        