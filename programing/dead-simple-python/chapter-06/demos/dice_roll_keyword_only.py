# 使用可选参数限制函数只能传递关键字参数
import random

def roll_dice(*, dice=1, sides=6):
    # 此处使用了未命名的可选参数*，以确保参数列表中该可变参数之后的每个参数都只能通过名称来访问。
    return tuple(random.randint(1, sides) for _ in range(dice))

# 使用位置参数
dice_cup = roll_dice(6, 2)
print(dice_cup)