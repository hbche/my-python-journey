import random

# 模拟文本大冒险中的玩家角色
# 声明全局变量
# 当前经验值
xp = 10
# 当前血条
health = 10
def attempt(action, min_roll, outcome):
    """
    action: 表示执行某种操作
    min_roll: 表示操作的下限
    outcome: 表示后续操作
    """
    global xp, health
    roll = random.randint(1, 20)
    if roll >= min_roll:
        print(f"{action} SUCCESS.")
        result = True
    else:
        print(f"{action} FAILED.")
        result = False

    scores = outcome(result)
    health = health + scores[0]
    print(f"Health is now {health}")
    xp = xp + scores[1]
    print(f"Experience is now {xp}")

    return result

def eat_bread(success):
    if success:
        return (1, 0)
    else:
        return (-1, 0)
    
def fight_ice_weasel(success):
    if success:
        return (0, 10)
    else:
        return (-10, 10)
    
attempt('Eating bread', 5, lambda success: (1,10) if success else (-1, 0) )
attempt('Fighting ice weasel', 15, lambda success: (0, 10) if success else (-10, 10))