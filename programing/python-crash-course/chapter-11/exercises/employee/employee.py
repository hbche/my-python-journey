# 练习11.3：雇员　编写一个名为Employee的类，其__init__()方法接受名、姓和年薪，并将它们都存储在属性中。
# 编写一个名为give_raise()的方法，它默认将年薪增加5000美元，同时能够接受其他的年薪增加量。
# 为Employee类编写一个测试文件，其中包含两个测试函数：test_give_default_raise()和test_give_custom_raise()。
# 在不使用夹具的情况下编写这两个测试，并确保它们都通过了。
# 然后，编写一个夹具，以免在每个测试函数中都创建一个Employee对象。重新运行测试，确认两个测试都通过了。

class Employee:
    """模拟一个雇员类，存储名、姓和年薪"""
    
    def __init__(self, first_name, last_name, annual_salary):
        """初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, raise_salary=5000):
        """默认将年薪增加5000美元，同时能够接受其他的年薪增加量"""
        self.annual_salary += raise_salary
        