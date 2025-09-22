# 使用 tpye() 函数获取某个变量的类型信息
answer = 42
print(type(answer))     # <class 'int'>

if isinstance(answer, int):
    # 判断 answer 的类型是否是 int
    print("What's the question?")       # What's the question?