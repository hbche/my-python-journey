from pathlib import PurePath

path = PurePath('../index.md')
with open(path, 'r', encoding='utf-8') as file:
    print(file.read())