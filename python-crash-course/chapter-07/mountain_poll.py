# 使用while循环录入用户输入作为字典存储
# 创建空字典用于存储用户的输入
responses = {}

# 声明一个循环标志
polling_active = True

while polling_active:
    # 提示用户输入姓名和喜欢的山
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb someday? ")

    # 将用户的输入存储在字典中
    responses[name] = mountain

    # 询问用户是否继续
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False


# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain}.")