from pathlib import Path
import json

path = Path('numbers.json')
# 将文件内容读到内存中
contents = path.read_text()
# 将内存中的数据转换成python的数据结构
numbers = json.loads(contents)
print(numbers)