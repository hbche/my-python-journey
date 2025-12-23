with open('213AnywhereAve.txt', 'r') as house:
    print(repr(house.readline()))   # '78 Somewhere Road, Anytown PA\n'
    print(house.tell()) # 31
    print(repr(house.readline()))   # 'Cozy 2-bed, 1-bath bungalow. Full of potential.\n'
    print(house.tell()) # 80
