# 使用生成器表达式初始化元组和列表
import array

symbols = '$¢£¥€¤'
codes = tuple(ord(symbol) for symbol in symbols)
list = array.array('I', (ord(symbol) for symbol in symbols))

print(codes)        # (36, 162, 163, 165, 8364, 164)
print(list)         # array('I', [36, 162, 163, 165, 8364, 164])
