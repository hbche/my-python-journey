# 使用双端队列模拟咖啡店排队
from collections import deque
customers = deque(['Daniel', 'Denis'])
customers.append('Simon')
print(customers)    # deque(['Daniel', 'Denis', 'Simon'])
customer = customers.popleft() # 从队列中移除最前面的元素
print(customer)     # Daniel
print(customers)    # deque(['Denis', 'Simon'])
customers.appendleft('James')
print(customers)    # deque(['James', 'Denis', 'Simon'])
last_in_line = customers.pop()
print(last_in_line) # Simon
print(customers)    # eque(['James', 'Denis'])