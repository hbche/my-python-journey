class Car:
    """模拟汽车类，存储汽车相关的信息"""
    
    
    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """返回格式化的描述信息"""
        long_name = f"{self.years} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """声明更新里程数的方法"""
        self.odometer_reading = mileage
        
    def increment_odometer(self, miles):
        """让里程表读数增加指定的量"""
        self.odometer_reading += miles


# 实例化一辆汽车
my_used_car = Car('subaru', 'outback', 2024)
# 打印格式化后的描述信息
print(my_used_car.get_descriptive_name())

# 通过方法修改属性值
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# 通过方法递增属性值
my_used_car.increment_odometer(100)
# 通过方法打印属性值
my_used_car.read_odometer()
