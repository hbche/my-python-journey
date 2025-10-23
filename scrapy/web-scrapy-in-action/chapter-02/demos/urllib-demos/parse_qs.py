from urllib.parse import parse_qs

query = 'name=hanbin&age=25'
url = 'https://www.baidu.com/index.html;user?name=hanbin'
# 解析查询字符串 query
print(parse_qs(query))      # {'name': ['hanbin'], 'age': ['25']}
print(parse_qs(url))        # {'https://www.baidu.com/index.html;user?name': ['hanbin']}