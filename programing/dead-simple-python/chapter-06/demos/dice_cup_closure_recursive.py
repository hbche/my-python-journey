import random
# 使用待递归的闭包实现掷骰子
def make_dice_cup(sides=6, dice=1):

    def roll(dice=dice):
        if dice < 1:
            return ()
        return (random.randint(1, sides), ) + roll(dice - 1)
    
    return roll
    
dice_cup = make_dice_cup(sides=8, dice=5)
damage1 = dice_cup()
print(damage1)
damage2 = dice_cup()
print(damage2)