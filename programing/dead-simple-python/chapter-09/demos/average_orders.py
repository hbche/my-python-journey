orders_per_day = [56, 41, 49, 22, 71, 43, 18]
average_orders = sum(orders_per_day) // len(orders_per_day)     # 向下取整
print(average_orders)       # 42