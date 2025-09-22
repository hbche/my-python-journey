import random

# 使用闭包重写掷骰子
def make_dice_cup(sides=6, dice=1):
    def roll():
        return tuple(random.randint(1, sides) for _ in range(dice))
    return roll

roll_for_damage = make_dice_cup(sides=8, dice=5)
damage = roll_for_damage()
print(damage)