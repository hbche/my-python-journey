class Car:
    """模拟传统汽车模型"""
    
    
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回格式规范的描述名称"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一个句子，支出汽车的行驶里程"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """更新里程表读数设置为给定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """让里程表读数增加给定的量"""
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        """加满箱油"""
        print("This car fill a gas tank!")
        

class Battery:
    """模拟电池类"""
    
    def __init__(self, battery_size=40):
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


# 声明电动轿车类
class ElectricCar(Car):
    """电动汽车的独特之处"""
    
    
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 电车特有的属性，电池容量
        self.battery = Battery()
        
    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        # print(f"This car has a {self.battery_size}-kWh battery.")
        self.battery.describe_battery()
    
    def fill_gas_tank(self):
        """加满箱油"""
        print("This car doesn't have a gas tank!")
        
    
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())           # 2024 Nissan Leaf
# 调用子类特有的方法
my_leaf.describe_battery()                      # This car has a 40-kWh battery.            
# 调用子类重写的方法
my_leaf.fill_gas_tank()                         # This car doesn't have a gas tank!