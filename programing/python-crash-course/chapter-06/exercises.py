# # 练习6.1：人　
# # 使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市。
# # 该字典应包含键first_name、last_name、age和city。
# # 将存储在该字典中的每项信息都打印出来。
# person_info = {
#     'first_name': 'Che',
#     'last_name': 'Robin',
#     'age': 29,
#     'city': 'Wuhan',
#     }
# print(f"first_name: {person_info['first_name']}")
# print(f"last_name: {person_info['last_name']}")
# print(f"age: {person_info['age']}")
# print(f"city: {person_info['city']}")

# # 练习6.2：喜欢的数1　使用一个字典来存储一些人喜欢的数。
# # 请想出5个人的名字，并将这些名字用作字典中的键。
# # 再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。
# # 打印每个人的名字和喜欢的数。
# # 为了让这个程序更有趣，通过询问朋友确保数据是真实的。
# favorite_numbers = {
#     'robin': 8,
#     'jim': 9,
#     'lucy': 1,
#     'candy': 6,
#     'jack': 2
# }
# print(f"Robin's favorite number is {favorite_numbers['robin']}.")
# print(f"Jim's favorite number is {favorite_numbers['jim']}.")
# print(f"Lucy's favorite number is {favorite_numbers['lucy']}.")
# print(f"Candy's favorite number is {favorite_numbers['candy']}.")
# print(f"Jack's favorite number is {favorite_numbers['jack']}.")

# 练习6.3：词汇表1　Python字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
# 1. 想出你在前面学过的5个编程术语，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# 2. 以整洁的方式打印每个术语及其含义。
# 为此，既可以先打印术语，在它后面加上一个冒号，再打印其含义；
# 也可以先在一行里打印术语，再使用换行符(\n)插入一个空行，然后在下一行里以缩进的方式打印其含义。
vocabulary = {
    'if': '用于条件判断，根据条件的真假制定不同的代码块',
    'for': '用于循环遍历',
    'range': '用于生成数值型列表',
    'append': '用于在列表结尾追加值',
    'insert': '用于在列表中插入值',
    'pop': '用于删除列表结尾数据或者指定索引数据',
    'remove': '用于删除列表中与方法参数第一个匹配的值',
    'del': '用于删除列表、字典的值',
    'reverse': '用于反转列表',
    'sort': '用于对列表进行永久排序',
    'sorted': '用于对列表进行临时排序，不修改原始列表',
    }
for key in vocabulary:
    print(f"{key}: {vocabulary[key]}\n")