# # 用input()函数获取用户输入，并打印用户输入
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# # 给while循环指定退出的条件，在符合退出条件时结束while循环
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# 使用标志控制循环
active = True
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end program. "
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)