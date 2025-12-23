# from pathlib import PurePath

# path = PurePath('../index.md')
# with open(path, 'r', encoding='utf-8') as file:
#     print(file.read())
    
# # AttributeError: 'PureWindowsPath' object has no attribute 'touch'
# path.touch()

from pathlib import Path

path = Path('../index.md')
with open(path, 'r', encoding="utf-8") as file:
    print(file.read())

path.touch()