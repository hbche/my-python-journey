specials = ['pumpkin spice latte', 'caramel macchiato', 'macho cappuccino']
# 使用特殊方法来访问和修改元素
print(specials.__getitem__(1))
specials.__setitem__(1, 'drip')
print(specials.__getitem__(1))
