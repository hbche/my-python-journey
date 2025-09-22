# from car_module import Car
# # 实例化一辆汽车
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.fill_gas_tank()
# my_new_car.read_odometer()
# my_new_car.update_odometer(500)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()

# from car_module import ElectricCar, Car
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# # 实例化一辆电动汽车
# my_tesla = ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.get_descriptive_name())

# import car_module as car
# my_mustang = car.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'model s', 2024)
# print(my_tesla.get_descriptive_name())

from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())