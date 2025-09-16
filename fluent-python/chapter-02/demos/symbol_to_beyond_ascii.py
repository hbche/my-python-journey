# # 使用列表推导来创建列表
# symbols = '$¢£¥€¤'
# beyond = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
# print(beyond)           # [162, 163, 165, 8364, 164]

# 使用filter和map组合来创建列表
symbols = '$¢£¥€¤'
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(codes)              # [162, 163, 165, 8364, 164]