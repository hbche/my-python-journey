import random

# 使用可选参数收集实参
def roll_dice(*dice):
    """模拟掷骰子"""
    
    # 使用tuple 将生成器转换成元组
    return tuple(random.randint(1, d) for d in dice)

print("Roll for initiative...")
# 两个骰子的面数都是20，第一个参数表示第一个骰子的面数，第二个参数表示第二个骰子的面数
player1, player2 = roll_dice(20, 20)

if player1 > player2:
    print(f"Player 1 goes first (rolled {player1}).")
else:
    print(f"Playerr 2 goes first (rolled {player2}).")