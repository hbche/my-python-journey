# 计算斐波那契数列

def fibonacci_next(series=None):
    """计算斐波那契数列的下一轮值"""
    if series == None:
        series = [1, 1]
    series.append(series[-2] + series[-1])
    return series

fib1 = fibonacci_next()
print(fib1)
fib1 = fibonacci_next(fib1)
print(fib1)

fib2 = fibonacci_next()
print(fib2)