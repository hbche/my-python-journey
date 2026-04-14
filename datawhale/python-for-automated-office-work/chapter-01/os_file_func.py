import os
from pathlib import Path

print(os.getcwd())  # 获取当前工作目录，即执行该代码的文件的所在路径

os.chdir('E:\\my-python-journey\\python-for-automated-office-work')   # 改变当前工作目录
print(os.getcwd())  # E:\my-python-journey\python-for-automated-office-work

path = Path('E:\\my-python-journey\\python-for-automated-office-work\\chapter-01\\os_file_func.py')
print('Create Time: ', os.path.getctime(path))
print('Access Time: ', os.path.getatime(path))
print('Modify Time: ', os.path.getmtime(path))
print('Size: ', os.path.getsize(path))
print('Is Absolute', os.path.isabs(path))
print('Is Dir? ', os.path.isdir(path))
print('Is File? ', os.path.isfile(path))
print('Is Exist? ', os.path.exists(path))

print(os.path.relpath(path, 'E:\\'))    # my-python-journey\python-for-automated-office-work\chapter-01\os_file_func.py
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))

print(f"{path}".split(os.path.sep))

print(os.path.join(os.path.dirname(path), '\\new\\empty'))
# os.makedirs()

print(os.listdir(os.getcwd()))