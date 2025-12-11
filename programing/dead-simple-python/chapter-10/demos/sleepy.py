import time

# sleepy = ['no pause', time.sleep(1), time.sleep(2)]
# print(sleepy[0])    # 终止 3秒，再执行输出语句

# sleepy = (time.sleep(t) for t in range(0, 3))

sleepy = (print(t) for t in [1, 2, 3, 4, 5])

print("Calling...")
next(sleepy)
print("Done!")