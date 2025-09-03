# 打印乘法口诀
for i in range(1,10):
    message = ""
    for j in range(1, 10):
        if i >= j:
            message += f"{j} * {i} = {i * j}\t"
    print(f"{message}\n")