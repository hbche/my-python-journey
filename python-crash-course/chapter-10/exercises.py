# 练习10.1: Python学习笔记　
# 在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，其中每一行都以“In Python you can”打头。
# 将这个文件命名为learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。
# 编写一个程序，读取这个文件，并将你所写的内容打印两次：第一次打印时读取整个文件；
# 第二次打印时先将所有行都存储在一个列表中，再遍历列表中的各行。

# from pathlib import Path

# path = Path('index.md')
# contents = path.read_text(encoding='utf-8').strip()
# lines = contents.splitlines()

# summary_content = ''
# for line in lines:
#     # if line.startswith('#'):
#     summary_content += f"\n{line.strip()}"
        
# print(f'The Note of Chapter 10 is: {summary_content}')

# # 练习10.2: C语言学习笔记　可使用replace()方法将字符串中的特定单词替换为另一个单词。

# from pathlib import Path

# path = Path('index.md')
# lines = path.read_text(encoding='utf-8').splitlines()

# summary_content = ''
# for line in lines:
#     summary_content += f"\n{line.replace('python', 'c').strip()}"
    
# print(summary_content)

# 练习10.3：简化代码　本节前面的程序file_reader.py中使用了一个临时变量lines，来说明splitlines()的工作原理。

# # 练习10.4：访客　编写一个程序，提示用户输入其名字。在用户做出响应后，将其名字写入文件guest.txt。
# from pathlib import Path

# path = Path('guest.txt')
# first_name = input("Enter your first name: ")
# last_name = input('Enter your last name: ')
# full_name = f"Hello, {first_name} {last_name}!".title()

# path.write_text(full_name)

# # 练习10.5：访客簿　编写一个while循环，提示用户输入其名字。收集用户输入的所有名字，将其写入guest_book.txt，并确保这个文件中的每条记录都独占一行。
# from pathlib import Path

# path = Path('guest_book.txt')
# content = ''

# while True:
#     first_name = input("Enter your first name: ")
#     if first_name == 'q':
#         break
#     last_name = input('Enter your last name: ')
#     if last_name == 'q':
#         break
#     content += f"{first_name} {last_name}\n"

# path.write_text(content, encoding='utf8')

# # 练习10.6：加法运算　在提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。
# # 在这种情况下，当你尝试将输入转换为整数时，将引发ValueError异常。
# # 编写一个程序，提示用户输入两个数，再将它们相加并打印结果。
# # 在用户输入的任意一个值不是数时都捕获ValueError异常，并打印一条友好的错误消息。
# # 对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。

# # 练习10.7：加法计算器　将为练习10.6编写的代码放在一个while循环中，让用户在犯错（输入的是文本而不是数）后能够继续输入数。

# def addTwoNumber(first_string_number, second_string_number):
#     try:
#         first_number = int(first_string_number)
#         second_number = int(second_string_number)
#     except ValueError:
#         print(f"The tow numbers {first_string_number} and {second_string_number} you input are not integer!")
#     else:
#         total = first_number + second_number
#         print(f"{first_number} add {second_number} is {total}.")
    
# print("Enter two number, and I will calculat the sum of them.")
# print("Enter 'q' to quit.")

# while True:
#     first_string_number = input("Input the first number: ")
#     if first_string_number == 'q':
#         break
#     second_string_number = input("Input the second number: ")
#     if second_string_number == 'q':
#         break
#     addTwoNumber(first_string_number, second_string_number)

# # 练习10.8：猫和狗　创建文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
# # 编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。
# # 将这些代码放在一个try-except代码块中，以便在文件不存在时捕获FileNotFoundError异常，并显示一条友好的消息。
# # 将任意一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。

# # 练习10.9：静默的猫和狗　修改你在练习10.8中编写的except代码块，让程序在文件不存在时静默失败。

# from pathlib import Path

# def read_file(file):
#     path = Path(file)
#     try:
#         contents = path.read_text(encoding='utf8')
#     except FileNotFoundError:
#         # print(f"Sorry, the file {path} does not exist.")
#         return []
#     else:
#         lines = contents.splitlines()
#         return lines
    
# cats = read_file('cats.txt')
# for cat in cats:
#     print(f"Hello, {cat.title()}!")
    
# dogs = read_file('dogs.txt')
# for dog in dogs:
#     print(f"Welcome, {dog}!")

# 练习10.10：常见单词　访问古登堡计划，找一些你想分析的图书。
# 下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
# 可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row'在一个字符串中出现了多少次：

# 编写一个程序，读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。
# 这里计算得到的结果并不准确，因为诸如'then'和'there'等单词也被计算在内了。
# 请尝试计算'the'（包含空格）出现的次数，看看结果相差多少。
from pathlib import Path

def count_word_by_count(file, word):
    """统计一个单词在文件中出现了多少次"""
    
    path = Path(file)
    contents = path.read_text(encoding='utf8')
    word_count = contents.count(word)
    print(f"The file {path} has {word_count} \"{word}\".")
    
# def count_word_by_equals(file, word):
#     """根据严格相等进行统计"""
    
#     path = Path(file)
#     contents = path.read_text(encoding='utf8')
#     words = contents.split()
#     word_count = 0
#     for current_word in words:
#         if current_word.strip() == word and len(current_word.strip()) == len(word):
#             word_count += 1
#     print(f"The file {path} has {word_count} \"{word}\".")

def count_word_by_equals(file, word):
    """
    统计文件中指定单词的出现次数（完全匹配）
    
    参数:
        file (str): 文件名
        word (str): 要统计的单词
    
    返回:
        int: 单词出现的次数
    """
    count = 0
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                # 将行拆分为单词列表（按空格分割）
                words_in_line = line.strip().split()
                # 统计完全匹配的单词
                count += words_in_line.count(word)
            print(f"The file {file} has {count} \"{word}\".")
        return count
    except FileNotFoundError:
        print(f"错误：文件 '{file}' 未找到！")
        return 0
    except Exception as e:
        print(f"读取文件时发生错误：{e}")
        return 0
    
def count_word_by_equals_with_line(file, word):
    """根据每行严格相等进行统计"""
    
    path = Path(file)
    contents = path.read_text(encoding='utf8')
    lines = contents.splitlines()
    
    word_count = 0
    for line in lines:
        words = line.split()  
        for current_word in words:
            if current_word.strip() == word:
                word_count += 1 
    print(f"The file {path} has {word_count} \"{word}\".")
    
count_word_by_count('alice.txt', 'the')      # The file alice.txt has 2312 "the".
count_word_by_equals('alice.txt', 'the')      # The file alice.txt has 2312 "the".
count_word_by_equals_with_line('alice.txt', 'the')      