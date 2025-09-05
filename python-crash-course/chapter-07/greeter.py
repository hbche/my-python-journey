# # 给input() 函数指定参数，便于给用户提供清晰的提示
# name = input("Please enter your name: ")
# print(f"Hello, {name}!")
# # Please enter your name: Robin
# # Hello, Robin!

# 对于提示信息较长的时候，可以先将提示信息存在一个变量中，在给input()函数传入该变量
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

# If you share your name, we can personalize the messages you see.
# What is your first name? Robin

# Hello, Robin!