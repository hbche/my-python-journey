from urllib.parse import parse_qsl

query = 'name=hanbin&age=25'
# 以列表形式返回查询字符串的解析结果
print(parse_qsl(query))     # [('name', 'hanbin'), ('age', '25')]