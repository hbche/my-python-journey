# # 使用 range 函数快速生成指定范围的数
# for value in range(1, 5):
#     print(value)
# # 1
# # 2
# # 3
# # 4

# # 使用 list() 函数将range()函数返回的结果转换成数值列表
# numbers = list(range(1, 5))
# print(numbers)

# # 使用 range() 函数的步长参数
# numbers = list(range(2, 11, 2))
# print(numbers)          # [2, 4, 6, 8, 10]

# 对数值列表进行简单的统计计算
digits = list(range(1, 10))
digits.append(0)
print(min(digits))      # 最小值
print(max(digits))      # 最大值
print(sum(digits))      # 总和