# 解析数字字符串，计算平均值，演示 else 子句
import math

def average_string(number_string):
    try:
        numbers = [float(n) for n in number_string.split()]
    except ValueError:
        total = math.nan
        values = 1
    else:
        total = sum(numbers)
        values = len(numbers)
    
    # 使用 try 子句处理 values 为 0 的情况
    try:
        average = total / values
    except ZeroDivisionError:
        average = math.inf
        
    return average
    
while True:
    number_string = input("Enter space-delimited list of numbers:\n ")
    print(average_string(number_string))