import numpy as np

# a = np.array([0.3,2.9, 4.0])
# exp_a = np.exp(a)
# print(exp_a)
# sum_exp_a = np.sum(exp_a)
# print(sum_exp_a)
# y = exp_a / sum_exp_a
# print(y)

# def softmax(a):
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     return exp_a / sum_exp_a

# a = np.array([1010, 1000, 990])
# max_a = np.max(a)
# c = np.exp(a-max_a)/np.sum(np.exp(a-max_a))
# print(c)
# # [9.99954600e-01 4.53978686e-05 2.06106005e-09]

def softmax(x):
    c = np.max(x)   # 溢出对策
    exp_x = np.exp(x-c)
    return exp_x / np.sum(exp_x)

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)    # [0.01821127 0.24519181 0.73659691]
print(np.sum(y))    # 1.0