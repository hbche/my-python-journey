# 声明 Dog 类
class Dog:
    """一次模拟小狗的简单尝试"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name.title()} is now sitting.")
        
    def roll_over(self):
        """模拟小狗收到命令是打滚"""
        print(f"{self.name.title()} rolled over!")
        
# 创建一个Dog实例，并访问该实例的属性
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# 调用示例的方法
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('Lucy', 3)
print(f"Your dog's name is {your_dog.name.title}.")
print(f"Your dog is {your_dog.age} years old.")
# 调用示例的方法
your_dog.sit()
your_dog.roll_over()