# 使用列表推导生成笛卡尔积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
# # 先以颜色排序，再以尺寸排序
# tshirts = [(color, size) for color in colors for size in sizes]
# print(tshirts) # [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
# 先以尺寸排序，再以颜色排序
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)  # [('black', 'S'), ('white', 'S'), ('black', 'M'), ('white', 'M'), ('black', 'L'), ('white', 'L')]