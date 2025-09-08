from car_module import Car
from electric_car_module import ElectricCar as EC

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_tesla = EC('tesla', 'model s', 2024)
print(my_tesla.get_descriptive_name())