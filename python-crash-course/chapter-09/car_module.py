class Car:
    """模拟传统油车模型"""


    def __init__(self, make, model, years):
        """初始化汽车类的信息"""
        self.make = make
        self.model = model
        self.years = years
        # 增加里程表读书参数，默认0
        self.odometer_reading = 0
        # 增加油箱容量，默认值为15
        self.fuel_tank_capacity = 15

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

    def fill_gas_tank(self):
        """打印一条加满油箱的消息"""
        print(f"This car's gas tank capacity is {self.fuel_tank_capacity} gallons.")