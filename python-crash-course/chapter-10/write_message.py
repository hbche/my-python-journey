# # 写入文件
# from pathlib import Path

# # 生成写入文件的路径
# path = Path('programing.txt')
# # 向文件中写入内容，接收可选的encoding参数指定写入的编码
# path.write_text("I love programing.")
# # 会覆盖之前写入的内容，实际只有下面这句内容
# path.write_text("我热爱编程。", encoding='utf8')

# 写入多行数据
from pathlib import Path

# 生成写入文件的路径
path = Path('programing.txt')
# 创建变量记录写入的多行数据
contents = 'I love programing.'
contents += '\n我热爱编程。'

# 以指定编码向文件中写入内容
path.write_text(contents, encoding='utf8')