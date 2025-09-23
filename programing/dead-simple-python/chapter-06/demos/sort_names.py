people = [
    ("Jason", "McDonald"),
    ("Denis", "Pobedrya"),
    ("Daniel", "Foerster"),
    ("Jaime", "Lopez"),
    ("James", "Beecham")
]

# 使用lambda表达式指定排序的键，通过姓来排序
sorted_by_last_name = sorted(people, key=lambda name: name[1])
print(sorted_by_last_name)