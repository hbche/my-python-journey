temps = [87, 76, 79]
highs = temps
print(temps is highs) # True
temps += [81]
print(temps is highs) # True
print(highs)          # [87, 76, 79, 81]
print(temps)          # [87, 76, 79, 81]