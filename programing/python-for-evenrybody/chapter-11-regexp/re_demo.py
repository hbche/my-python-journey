import re

hand = open('index.md', mode='r', encoding='utf-8')
with hand:
    for line in hand:
        line = line.strip()
        if re.search('^#', line):
            print(line) 