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

# 练习9.5：尝试登录次数　在为练习9.3编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，用来将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，用来将属性login_attempts的值重置为0。

class User:
    """模拟用户类，存储用户相关信息"""
    
    
    def __init__(self, first_name, last_name):
        """初始化用户信息"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        
    def describe_login_attempts(self):
        """打印登录通过次数"""
        print(f"Hello {self.first_name}! You have loginned {self.login_attempts}.")
        
    def increment_login_attempts(self):
        """累加登录通过次数"""
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        """重置登录通过次数"""
        self.login_attempts = 0
        
user = User('Robin', 'Che')
user.describe_login_attempts()
user.increment_login_attempts()
user.describe_login_attempts()
user.reset_login_attempts()
user.describe_login_attempts()
