# 使用 break 结束循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}.")