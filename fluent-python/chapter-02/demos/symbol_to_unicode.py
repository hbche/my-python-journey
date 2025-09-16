# # 讲一个字符串转换成Unicode码位的列表
# symbols = "$¢£¥€¤"
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))

# print(codes)            # [36, 162, 163, 165, 8364, 164]


# 讲一个字符串转换成Unicode码位的列表
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
