# 练习7.1：汽车租赁　编写一个程序，询问用户要租什么样的汽车，并打印一条消息，如下所示。　　
# Let me see if I can find you a Subaru.

car = input("What kind of car would you like to rent? ")
print(f"Let me see if I can find you a {car}.")

# 练习7.2：餐馆订位　编写一个程序，询问用户有多少人用餐。
# 如果超过8个人，就打印一条消息，指出没有空桌；否则指出有空桌。

people = int(input("How many people are in your dinner group? "))
if people > 8:
    print("Sorry, there are no available tables.")
else:
    print("There are available tables.")

# 练习7.3: 10的整数倍　让用户输入一个数，并指出这个数是否是10的整数倍。

number = int(input("Enter a number, and I'll tell you if it's a multiple of 10: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")


# 练习7.4：比萨配料　编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。
# 每当用户输入一种配料后，都打印一条消息，指出要在比萨中添加这种配料。
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"Adding {topping} to your pizza.")

# 练习7.5：电影票　有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3（含）～12岁的观众收费10美元；年满12岁的观众收费15美元。
# 请编写一个循环，在其中询问用户的年龄，并指出其票价。

while True:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is ${price}.")


# 练习7.6：三种出路　以不同的方式完成练习7.4或练习7.5，在程序中采取如下做法。
# • 在while循环中使用条件测试来结束循环。
# • 使用变量active来控制循环结束的时机。

active = True
while active:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            price = 0
        elif 3 <= age <= 12:
            price = 10
        else:
            price = 15
        print(f"Your ticket price is ${price}.")


# • 使用break语句在用户输入'quit'时退出循环。
active = True
while active:
    age = input("Enter your age (or 'quit' to finish): ")
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"Your ticket price is ${price}.")

# 练习7.7：无限循环　编写一个没完没了的循环，并运行它。​（要结束该循环，可按Ctrl + C，也可关闭显示输出的窗口。​）

while True:
    print("This loop will run forever.")

# 练习7.8：熟食店　创建一个名为sandwich_orders的列表，其中包含各种三明治的名字，再创建一个名为finished_sandwiches的空列表。
# 遍历列表sandwich_orders，对于其中的每种三明治，都打印一条消息，如“I made your tuna sandwich.”​，并将其移到列表finished_sandwiches中。
# 当所有三明治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)

# 练习7.9：五香烟熏牛肉卖完了　使用为练习7.8创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
# 在程序开头附近添加这样的代码：先打印一条消息，指出熟食店的五香烟熏牛肉(pastrami)卖完了；
# 再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。
# 确认最终的列表finished_sandwiches中未包含'pastrami'。

sandwich_orders = ['tuna', 'ham', 'pastrami', 'turkey', 'pastrami', 'veggie', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:  
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
for sandwich in finished_sandwiches:
    print(sandwich)

# 练习7.10：梦想中的度假胜地　编写一个程序，调查用户梦想中的度假胜地。使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查结果的代码块。
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

for name, place in responses.items():
    print(f"{name} would like to visit {place}.")