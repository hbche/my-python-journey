current_score = 0

def score():
    # 声明此处是全局变量，不是函数内部新声明的局部变量
    global current_score
    new_score = 465
    current_score = new_score
        
score()
print(current_score)        # 0