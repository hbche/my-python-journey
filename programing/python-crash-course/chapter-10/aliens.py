# 使用 try-except代码块捕获异常
from pathlib import Path

path = Path('aliens.txt')
# 读取一个不存在的文件将触发Python的FileNotFoundError
try:
    contents = path.read_text(encoding='utf-8')         # Sorry, the file aliens.txt does not exist.
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    print(contents)