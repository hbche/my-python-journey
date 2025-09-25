# 演示 while 循环

number = None

while number is None:
    try:
        raw = input("Enter a number: ")
        if raw == 'q':
            # 提前终止循环
            break
        number = int(raw)
    except ValueError:
        print("You must enter a number.")
else:
    # 循环顺利结束时才执行，任何提前结束的场景都不执行else子句 
    print(f"You entered {number}")