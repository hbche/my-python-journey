from pathlib import Path

# 创建了一个表示文件pi_digits.txt的Path对象
path = Path('pi_digits.txt')
# 读取文件的全部内容
contents = path.read_text().rstrip()

# 将内容拆解成行，遍历输出
lines = contents.splitlines()
for line in lines:
    print(line)