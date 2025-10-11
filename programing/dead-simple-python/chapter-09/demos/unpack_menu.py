menu = {'drip': 1.95, 'cappuccion': 2.95, 'americano': 2.49}
a, b, c = menu
print(a)        # drip
print(b)        # cappuccion
print(c)        # americano

# 对字典的值进行解包
a, b, c = menu.values()
print(a)        # 1.95
print(b)        # 2.95
print(c)        # 2.49

# 基于字典的 item 视图解包
a, b, c = menu.items()
print(a)        # ('drip', 1.95)
print(b)        # ('cappuccion', 2.95)
print(c)        # ('americano', 2.49)