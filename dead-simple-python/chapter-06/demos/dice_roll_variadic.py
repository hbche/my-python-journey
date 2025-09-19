import random

# 使用递归实现
def roll_dice(*dice):
    if dice:
        roll = random.randint(1, dice[0])
        # 生成dice 1~列表结尾的切片，*表示将列表进行解包
        return (roll, ) + roll_dice(*dice[1:])
    return ()

# 同时投掷 5 个 6面的骰子
dice_cup = roll_dice(6, 6, 6, 6, 6)
print(dice_cup)

# 同时投掷面数不同的4个骰子
bunch_o_dice = roll_dice(20, 6, 8, 4)
print(bunch_o_dice)