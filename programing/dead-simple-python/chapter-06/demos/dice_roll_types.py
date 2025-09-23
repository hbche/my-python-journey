import typing
import random

# 定义类型别名
TupleInts = typing.Tuple[int, ...]

# 给 roll_dice 增加类型
def roll_dice(sides: int = 6, dice: int = 1) -> TupleInts:
    return tuple(random.randint(1, sides) for _ in range(dice))

roll_cup = roll_dice(dice=3)
print(roll_cup)