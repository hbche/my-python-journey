import random

def generate_puzzle(low=1, high=100):
    """创建一个生成随机数的函数，默认生成1~100之间的整数"""
    print(f"I'm thinking of a number between {low} and {high}.")
    return random.randint(low, high)

def make_guess(target):
    """根据随机生成的数字，获取用户输入，并判断是否猜对"""
    
    # 获取用户输入
    guess = None
    while guess is None:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Enter an integer.")
    
    # 判断用户输入数字是否是随机生成的数字
    # 如果用户猜对了，返回结果True
    if guess == target:
        return True
    
    # 如果没有猜对，需要给出提示，并返回结果False
    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    return False

def play(tries=8):
    """给定尝试次数，开始游戏"""
    
    # 生成随机数
    target = generate_puzzle()
    
    # 根据给定的次数进行游戏
    while tries > 0:
        # 如果猜对了就退出游戏
        if make_guess(target):
            print("You win!")
            return
        # 否则减少尝试次数，打印剩余尝试次数
        tries -= 1
        print(f"{tries} tries left.")
    
    print(f"Game over! The answer was {target}.")
    
if __name__ == "__main__":
    # 如果是主程序就执行
    play()