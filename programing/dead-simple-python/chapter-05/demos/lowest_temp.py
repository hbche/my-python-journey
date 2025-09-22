def find_lowest(temperatures):
    # 使用 sorted 对原始列表排序并返回新的列表，不修改原始列表
    sorted_temps = sorted(temperatures)
    print(sorted_temps[0])

temps = [85, 76, 79, 72, 81]
find_lowest(temps)
print(temps)        # [85, 76, 79, 72, 81]