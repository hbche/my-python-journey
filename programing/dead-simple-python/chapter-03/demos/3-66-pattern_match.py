lunch_order = input("What wolud you like for lunch?")

# 捕获模式
match lunch_order:
    case 'salad' | 'soup':
        print("Eating healthy, eh?")
    case order:
        print(f"Enjoy your {order}.")

# # or模式
# match lunch_order:
#     case 'taco':
#         print("Taco, taco, TACO, tacotacotaco!")
#     case 'salad' | 'soup':
#         print("Eating healthy, eh?")
#     case _:
#         print("Yummy.")

# # 文本模式和通配符
# match lunch_order:
#     case "pizza":
#         print("Pizza time!")
#     case "sandwich":
#         print("Here's your sandwich")
#     case 'taco':
#         print("Taco, taco, TACO, tacotacotaco!")
#     case _:
#         print("Yummy.")