import random
import functools

character = "Sir Bob"
xp = 0
health = 15

def character_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kw_args):
        if health <= 0:
            print(f"{character} is too weak.")
            return
        
        result = func(*args, **kw_args)
        print(f"Health: {health} | XP: {xp}")
        return result
    
    return wrapper

@character_action
def eat_food(food):
    global health
    print(f"{character} ate {food}")
    health += 1

@character_action
def fight_monster(monster, strength):
    global xp, health
    if random.randint(1, 20) >= strength:
        xp += 10
        print(f"{character} defeated {monster}.")
    else:
        health -= 10
        xp += 5
        print(f"{character} flees from {monster}")
    
# 模拟吃面包
eat_food('bread')
# 魔精 一种小型恶魔或精怪
fight_monster('Imp', 15)
# 恐狼 史塔克家族的冰原狼就是典型的Direwolf
fight_monster('Direwolf', 15)
# 米诺陶洛斯 源自​​希腊神话​​的著名怪物
fight_monster('Minotaur', 19)
