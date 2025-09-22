import random

def roll_dice(sides, dice):
    """递归实现掷骰子"""
    # 嵌套函数
    def roll():
        return random.randint(1, sides)
    
    if dice < 1:
        return ()
    
    return (roll(), ) + roll_dice(sides, dice-1)


print("Roll for initiative...")
player1, player2 = roll_dice(20, 2)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")