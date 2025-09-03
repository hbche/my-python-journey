# # 使用 for 循环遍历列表
# magicians = []
# magicians.append('alice')
# magicians.append('david')
# magicians.append('carolina')
# for magician in magicians:  # for循环结构
#     print(magician)         # 使用缩进表示for循环结构内部的逻辑

# 循环后不必要的缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
    
    print("Thank you, everyone. That was a great magic show!")      # 错误缩进，导致原本执行一次的语句，变为循环内部逻辑，随着循环一起执行