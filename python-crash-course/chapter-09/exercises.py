# # 练习9.1：餐馆　创建一个名为Restaurant的类，为其__init__()方法设置两个属性：restaurant_name和cuisine_type。
# # 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# # 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

# class Restaurant:
#     """模拟一个餐馆类"""
    
    
#     def __init__(self, restaurant_name, cuisine_type):
#         """初始化方法，指定餐馆名称和菜系"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
        
#     def describe_restraurant(self):
#         """打印属性信息"""
#         print(f"I found one delicious {self.cuisine_type} restaurant, it was {self.restaurant_name}.")
        
#     def open_restaurant(self):
#         """支出餐厅当前正在营业中"""
#         print("We are serving now.")

# # 练习9.2：三家餐馆　根据为练习9.1编写的类创建三个实例，并对每个实例调用describe_restaurant()方法。

# # 粤菜餐厅 - 翡翠轩
# restaurant_01 = Restaurant('Jade Garden', 'Cantonese Cuisine')
# restaurant_01.describe_restraurant()
# # 川菜餐厅 - 蜀香园
# restaurant_02 = Restaurant('Spice Kingdom', 'Sichuan Cuisine')
# restaurant_02.describe_restraurant()
# # 陕西菜餐厅 - 面堂
# restaurant_03 = Restaurant('Noodle Loft', 'Shaanxi Cuisine')
# restaurant_03.describe_restraurant()

# # 练习9.3：用户　创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介中通常会有的其他几个属性。
# # 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
# # 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# # 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。

# class User:
#     """模拟用户信息类"""
    
    
#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name
        
#     def describe_user(self):
#         """描述用户信息"""
#         print(f"First Name: {self.first_name}\tLast Name: {self.last_name}")
        
#     def greet_user(self):
#         """向用户问好"""
#         print(f"Hello, {self.first_name} {self.last_name}!")
        
# user_01 = User('Robin', 'Che')
# user_01.describe_user()
# user_01.greet_user()

# user_02 = User('Hey', 'Jinh')
# user_02.describe_user()
# user_02.greet_user()

# # 练习9.4：就餐人数　在为练习9.1编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# # 根据这个类创建一个名为restaurant的实例。
# # 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印。
# # 添加一个名为set_number_served()的方法，用来设置就餐人数。
# # 调用这个方法并向它传递新的就餐人数，然后再次打印这个值。
# # 添加一个名为increment_number_served()的方法，用来让就餐人数递增。
# # 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

# class Restaurant:
#     """模拟一个餐馆类"""
    
    
#     def __init__(self, restaurant_name, cuisine_type):
#         """初始化方法，指定餐馆名称和菜系"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
        
#     def describe_restraurant(self):
#         """打印属性信息"""
#         print(f"I found one delicious {self.cuisine_type} restaurant, it was {self.restaurant_name}.")
        
#     def open_restaurant(self):
#         """支出餐厅当前正在营业中"""
#         print("We are serving now.")
        
#     def describe_number_served(self):
#         """打印累计服务人数"""
#         print(f"{self.restaurant_name} has served a total of {self.number_served} customers.")
        
#     def set_number_served(self, number_served):
#         """更新就餐人数"""
#         self.number_served = number_served
        
#     def increment_number_served(self, increased_number_served):
#         """递增服务人数"""
#         self.number_served += increased_number_served
        

# restaurant = Restaurant('Jade Garden', 'Cantonese Cuisine')
# restaurant.describe_number_served()         # Jade Garden has served a total of 0 customers.

# restaurant.set_number_served(20_000)
# restaurant.describe_number_served()         # Jade Garden has served a total of 20000 customers.

# restaurant.increment_number_served(300)
# restaurant.describe_number_served()         # Jade Garden has served a total of 20300 customers.

# # 练习9.5：尝试登录次数　在为练习9.3编写的User类中，添加一个名为login_attempts的属性。
# # 编写一个名为increment_login_attempts()的方法，用来将属性login_attempts的值加1。
# # 再编写一个名为reset_login_attempts()的方法，用来将属性login_attempts的值重置为0。

# class User:
#     """模拟用户类，存储用户相关信息"""
    
    
#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
        
#     def describe_login_attempts(self):
#         """打印登录通过次数"""
#         print(f"Hello {self.first_name}! You have loginned {self.login_attempts}.")
        
#     def increment_login_attempts(self):
#         """累加登录通过次数"""
#         self.login_attempts += 1
        
#     def reset_login_attempts(self):
#         """重置登录通过次数"""
#         self.login_attempts = 0
        
# user = User('Robin', 'Che')
# user.describe_login_attempts()
# user.increment_login_attempts()
# user.describe_login_attempts()
# user.reset_login_attempts()
# user.describe_login_attempts()

# # 练习9.6：冰激凌小店　冰激凌小店是一种特殊的餐馆。
# # 编写一个名为IceCreamStand的类，让它继承你为练习9.1或练习9.4编写的Restaurant类。
# # 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# # 添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
# # 编写一个显示这些冰激凌口味的方法。
# # 创建一个IceCreamStand实例，并调用这个方法。

# class IceCreamStand(Restaurant):
#     """模拟冰激凌小店类，继承自Restaurant类"""
    
    
#     def __init__(self, restaurant_name, cuisine_type):
#         """初始化方法，指定餐馆名称和菜系"""
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = []
        
#     def add_flavor(self, flavor):
#         """添加冰激凌口味"""
#         self.flavors.append(flavor)
        
#     def show_flavors(self):
#         """显示冰激凌口味"""
#         print(f"{self.restaurant_name} offers the following ice cream flavors:")
#         for flavor in self.flavors:
#             print(f"- {flavor}")

# # 创建一个IceCreamStand实例
# ice_cream_stand = IceCreamStand('Sweet Treats', 'Ice Cream')
# # 添加冰激凌口味
# ice_cream_stand.add_flavor('Vanilla')
# ice_cream_stand.add_flavor('Chocolate')
# ice_cream_stand.add_flavor('Strawberry')
# # 调用显示冰激凌口味的方法
# ice_cream_stand.show_flavors()


# # 练习9.7：管理员　管理员是一种特殊的用户。
# # 编写一个名为Admin的类，让它继承你为练习9.3或练习9.5完成编写的User类。
# # 添加一个名为privileges的属性，用来存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# # 编写一个名为show_privileges()的方法，显示管理员的权限。
# # 创建一个Admin实例，并调用这个方法。

# class User:
#     """模拟用户类，存储用户相关信息"""
    
    
#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
        
#     def describe_user(self):
#         """描述用户信息"""
#         print(f"First Name: {self.first_name}\tLast Name: {self.last_name}")
        
#     def greet_user(self):
#         """向用户问好"""
#         print(f"Hello, {self.first_name} {self.last_name}!")
        
#     def increment_login_attempts(self):
#         """累加登录通过次数"""
#         self.login_attempts += 1
        
#     def reset_login_attempts(self):
#         """重置登录通过次数"""
#         self.login_attempts = 0
# class Admin(User):
#     """模拟管理员类，继承自User类"""
    
    
#     def __init__(self, first_name, last_name):
#         """初始化管理员信息"""
#         super().__init__(first_name, last_name)
#         self.privileges = [
#             "can add post",
#             "can delete post",
#             "can ban user"
#         ]
        
#     def show_privileges(self):
#         """显示管理员权限"""
#         print(f"{self.first_name} {self.last_name} has the following privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")

# # 创建一个Admin实例
# admin_user = Admin('Alice', 'Smith')
# # 调用show_privileges()方法显示管理员权限
# admin_user.show_privileges()

# # 练习9.8：权限　编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9.7所述的字符串列表。
# # 将方法show_privileges()移到这个类中。在Admin类中，将一个Privileges实例用作其属性。
# # 创建一个Admin实例，并使用方法show_privileges()来显示权限。

# class Privileges:
#     """模拟权限类，存储管理员权限"""
    
    
#     def __init__(self):
#         """初始化权限列表"""
#         self.privileges = [
#             "can add post",
#             "can delete post",
#             "can ban user"
#         ]
        
#     def show_privileges(self):
#         """显示管理员权限"""
#         print("Privileges:")
#         for privilege in self.privileges:
#             print(f"- {privilege}")
# class Admin:
#     """模拟管理员类，继承自User类"""
    
    
#     def __init__(self, first_name, last_name):
#         """初始化管理员信息"""
#         self.first_name = first_name
#         self.last_name = last_name
#         self.privileges = Privileges()
        
#     def describe_user(self):
#         """描述用户信息"""
#         print(f"First Name: {self.first_name}\tLast Name: {self.last_name}")
        
#     def greet_user(self):
#         """向用户问好"""
#         print(f"Hello, {self.first_name} {self.last_name}!")

# # 创建一个Admin实例
# admin_user = Admin('Alice', 'Smith')
# # 调用show_privileges()方法显示管理员权限
# admin_user.privileges.show_privileges()


# # 练习9.9：电池升级　在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
# # 这个方法检查电池容量，如果电池容量不是65，就设置为65。
# # 创建一辆电池容量为默认值的电动汽车，调用方法get_range()，然后对电池进行升级，并再次调用get_range()。
# # 你将看到这辆汽车的续航里程增加了。

# class Battery:
#     """模拟电池类，存储电池相关信息"""
    
    
#     def __init__(self, battery_size=75):
#         """初始化电池容量"""
#         self.battery_size = battery_size
        
#     def get_range(self):
#         """返回电池续航里程"""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         else:
#             range = 0
#         return range
    
#     def upgrade_battery(self):
#         """升级电池容量到65"""
#         if self.battery_size < 65:
#             self.battery_size = 65
#     def describe_battery(self):
#         """打印电池容量"""
#         print(f"This car has a {self.battery_size}-kWh battery.")
# class ElectricCar:  
#     """模拟电动汽车类，继承自Car类"""
    
    
#     def __init__(self, make, model, year):
#         """初始化电动汽车信息"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.battery = Battery()  # 创建一个Battery实例作为属性
        
#     def describe_car(self):
#         """描述电动汽车信息"""
#         print(f"{self.year} {self.make} {self.model}")
        
#     def get_range(self):
#         """获取电池续航里程"""
#         return self.battery.get_range()
    
# # 创建一辆电池容量为默认值的电动汽车
# electric_car = ElectricCar('Tesla', 'Model S', 2022)
# # 打印电池容量
# electric_car.battery.describe_battery()  # This car has a 75-kWh battery.   
# # 调用方法get_range()
# print(f"Range: {electric_car.get_range()} miles")  # Range: 260 miles
# # 对电池进行升级
# electric_car.battery.upgrade_battery()
# # 再次调用get_range()
# print(f"Range after upgrade: {electric_car.get_range()} miles")  # Range after upgrade: 260 miles

# 练习9.10：导入Restaurant类　将最新的Restaurant类存储在一个模块中。
# 在另一个文件中导入Restaurant类，创建一个Restaurant实例，并调用Restaurant的一个方法，以确认import语句正确无误。


# 练习9.11：导入Admin类　以为完成练习9.8而做的工作为基础。
# 将User类、Privileges类和Admin类存储在一个模块中，再创建一个文件，在其中创建一个Admin实例并对其调用show_privileges()方法，以确认一切都能正确地运行。


# # 练习9.12：多个模块　将User类存储在一个模块中，并将Privileges类和Admin类存储在另一个模块中。再创建一个文件，在其中创建一个Admin实例并对其调用show_privileges()方法，以确认一切依然能够正确地运行。

# # 练习9.13：骰子　创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
# # 编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。
# # 创建一个6面的骰子并掷10次。
# # 创建一个10面的骰子和一个20面的骰子，再分别掷10次。
# from random import randint

# class Die:
#     """模拟骰子类，存储骰子相关信息"""

#     def __init__(self, sides=6):
#         self.sides = sides

#     def role_die(self):
#         rand_side = randint(1, self.sides)
#         print(f"The die has {self.sides} sides, and the random side is {rand_side}.")


# six_sided_die = Die()
# for _ in range(10):
#     six_sided_die.role_die()
# ten_sided_die = Die(10)
# for _ in range(10):
#     ten_sided_die.role_die()
# twenty_sided_die = Die(20)
# for _ in range(10):
#     twenty_sided_die.role_die()


# # 练习9.14：彩票　创建一个列表或元祖，其中包含10个数和5个字母。
# # 从这个列表或元组中随机选择4个数或字母，并打印一条消息，指出只要彩票上是这4个数或字母，就中大奖了。
# from random import choice
# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
# winning_ticket = [choice(elements) for _ in range(4)]
# print(f"To win the lottery, your ticket must have the following elements: {winning_ticket}")

 
# # 练习9.15：彩票分析　可以使用一个循环来理解中前述彩票大奖有多难。
# # 为此，创建一个名为my_ticket的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
# # 请打印一条消息，报告执行多少次循环才中了大奖。

# from random import choice
# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
# my_ticket = [1, 'A', 3, 'D']
# winning_ticket = []
# attempts = 0
# while winning_ticket != my_ticket:
#     winning_ticket = [choice(elements) for _ in range(4)]
#     attempts += 1
# print(f"To win the lottery with your ticket {my_ticket}, it took {attempts} attempts.")


# 练习9.16: Python 3 Module of the Week　要了解Python标准库，一个很不错的资源是网站Python 3 Module of the Week。
# 请访问该网站并查看其中的目录，找一个你感兴趣的模块进行探索，从模块random开始可能是个不错的选择。