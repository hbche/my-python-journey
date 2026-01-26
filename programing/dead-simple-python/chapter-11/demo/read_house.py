with open('SomewhereRd.txt', 'r') as house:
    contents = house.read()
    print(type(contents))
    print(contents)