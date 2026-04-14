import os

filename = 'hello.txt'
path = os.path.join(os.getcwd(), filename)
print(f"The read file: {path}")

file = open(path)
print(file.read())