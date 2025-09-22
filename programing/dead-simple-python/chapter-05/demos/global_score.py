high_score = 10

def score():
    # 声明high_score为外部的全局变量high_score，而不是函数内部的局部变量
    global high_score
    new_score = 465
    if new_score > high_score:
        print("New high score")
        # 更新 high_score
        high_score = new_score
        
score()
print(high_score) # 465