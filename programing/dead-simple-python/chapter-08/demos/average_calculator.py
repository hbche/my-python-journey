class AverageCalculator:
    
    def __init__(self):
        self.total = 0
        self.sum = 0
        
    def __call__(self, *values):
        """实现 __call__ 特殊方法，使得类变得可调用，用于计算参数的平均值"""
        if values:
            for value in values:
                self.total += 1
                self.sum += float(value)
        return self.sum / self.total
    
average = AverageCalculator()
values = input("Enter scores, seperated by spaces:\n").split()
try:
    print(f"Average is {average(*values)}.")
# 如果没有输入的值的话，total为空，在计算平均值的时候，分母为空，导致报错ZeroDivisionError
except ZeroDivisionError:
    print("Error: No values provided.")
# 如果输入的不是数值型的字符串，float在进行类型转换的时候会报 ValueError
except (ValueError, UnicodeError):
    print(f"Error: All inputs should be numeric.")
