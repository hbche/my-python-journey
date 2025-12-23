with open('78SomewhereRd.txt', 'r') as house:
    print(repr(house.readline(2)))  # '78'
    print(repr(house.readline(2)))  # ' S'
    print(repr(house.readline(100)))    # 'omewhere Road, Anytown PA\n'
    print(repr(house.readline(2)))  # 'Ti'
    print(repr(house.readline(2)))  # 'ny'
    print(repr(house.readline()))   # ' 2-bed, 1-bath bungalow. Needs repairs.\n'