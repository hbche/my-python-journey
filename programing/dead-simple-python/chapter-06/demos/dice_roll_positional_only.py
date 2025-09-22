# 限制dice参数只能通过位置参数传递
import random

def roll_dice(dice=1, /, sides=6):
    """使用斜杠标识前面的参数指定为仅位置参数，后面的参数即可为位置参数也可谓关键字参数"""
    
    return tuple(random.randint(1, sides) for _ in range(dice))

# 都传递位置参数
dice_cup1 = roll_dice(4, 20)            # dice=4, sides=20
# 仅传入第一个位置参数，sides为默认值
dice_cup2 = roll_dice(4)                # dice=4, sides=6
# 位置参数只用默认值，sides使用关键字参数
dice_cup3 = roll_dice(sides=20)         # dices=4, sides=20
# 位置参数+关键字参数
dice_cup4 = roll_dice(4, sides=20)      # dices=4, sides=20

dice_cup4 = roll_dice(dice=4, sides=20)