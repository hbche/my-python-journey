from pathlib import PosixPath

path = PosixPath('/home/jason/.bash_history')

with path.open('r') as file:
    for line in file:
        continue
    print(line.strip())