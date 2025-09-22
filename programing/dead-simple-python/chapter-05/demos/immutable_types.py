eggs = 12
carton = eggs
print(eggs is carton)   # True
eggs +=1
print(eggs is carton)   # False
print(eggs)             # 13
print(carton)           # 12