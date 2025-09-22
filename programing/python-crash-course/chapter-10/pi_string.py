from pathlib import Path

path = Path('pi_digits.txt')
# 读取文件的内容
contents = path.read_text()
# 将读取的内容拆分长行列表
lines = contents.splitlines()

# 保存pi的值
pi_string = ''
# 遍历pi的内容，记录每行pi的值
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))