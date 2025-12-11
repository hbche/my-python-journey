def generate_divis_by_three():
    for n in range(1, 10):
        if n % 3 == 0:
            yield n
        else:
            yield 'redacted'

# # 使用三元表达式
# def generate_divis_by_three():
#     for n in range(100):
#         yield n if n % 3 == 0 else 'redacted'
            
# divis_by_three = generate_divis_by_three()

# 改为含有三元表达式的生成器表达式
divis_by_three = (n if n % 3 == 0 else 'redacted' for n in range(100))

for i in divis_by_three:
    print(i)