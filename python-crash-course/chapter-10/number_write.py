import json
from pathlib import Path

numbers = [1, 3, 5, 7, 9]
# 调用json.dumps转储内容，转换成json格式的字符串
contents = json.dumps(numbers)
path = Path('numbers.json')
# 将json字符串写入文件
path.write_text(contents)