# from collections import deque

# customers = deque(['Kyle', 'Simon', 'James'])
# customers.append('Daniel')
# first, second, _, _ = customers
# print(first)        # Kyle
# print(second)       # Simon

# # 注意：只有一个元素的元组，结尾需要保留一个逗号，区分()运算符
# baristas = ('Jason', )
# barista,  = baristas
# print(barista)

from collections import deque

# 星号表达式
customers = deque(['Kyle', 'Simon', 'James', 'Daniel'])
*_, second_to_last, last = customers
print(second_to_last)   # James
print(last)             # Daniel