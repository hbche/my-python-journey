# def license_plates():
#     """
#     使用生成器函数
#     """
#     for num in range(1000):
#         yield f"ABC{num: 03}"

# # 使用生成器表达式生成迭代器
# license_plates = (f"ABC {num:03}" for num in range(1000))
        
# for plate in license_plates:
#     print(plate)

# 使用复合循环结构的生成器表达式生成车牌号
from itertools import product
from string import ascii_uppercase as alphabet

## 使用生成器表达式
# license_plates = (f"{''.join(letters)} {num:03}"
#                   for letters in product(alphabet, repeat=3)
#                   if letters != ('G', 'O', 'V')
#                   for num in range(1000))

## 使用生成器函数
# def generate_license_plates():
#     for letters in product(alphabet, repeat=3):
#         if letters != ('G', 'O', 'V'):
#             for num in range(1000):
#                 yield f"{"".join(letters)} {num:03}"
                
# license_plates = generate_license_plates()

# 使用复合的生成器表达式
license_plates = (f"{letters} {num:03}" 
                  for letters in ("".join(chars) for chars in product(alphabet, repeat=3))
                  if letters != 'GOV'
                  for num in range(1000)
                  )

registrations = {}

def new_registration(owner):
    if owner not in registrations:
        plate = next(license_plates)
        registrations[owner] = plate
        return plate
    else:
        return None

# skip_total = (6 * 26 * 26 * 1000) + (14 * 26 * 1000) + (21 * 1000)
skip_total = 4441888
for _ in range(skip_total):
    next(license_plates)

name = 'Jason C. McDonald'
my_plate = new_registration(name)
print(my_plate)
print(registrations[name])