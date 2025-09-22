# 利用求模运算判断用户输入的数是奇数还是偶数
number = input("Enter a number, i will tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
