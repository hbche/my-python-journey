# import re

# hand = open('index.md', mode='r', encoding='utf-8')
# with hand:
#     for line in hand:
#         line = line.strip()
#         if re.search('^#', line):
#             print(line) 


# import re

# prompt = 'My 2 favoriate numbers are 19 and 42'
# match_str = re.findall('[0-9]+', prompt)
# print(match_str)    # ['2', '19', '42']

# import re

# prompt = 'From: Using the : character'
# match_str = re.findall('^F.+:', prompt)
# print(match_str)    # ['From: Using the:']

# import re

# prompt = 'From: Using the : character'
# match_str = re.findall('^F.+?:', prompt)
# print(match_str)    # ['From:']

# import re

# email = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# match_str = re.findall('^From .*@([^ ]*)', email)
# print(match_str)

# import re

# hand = open('mbox-short.txt')

# numlist = list()
# with hand:
#     for line in hand:
#         line = line.rstrip() #去掉行尾换行符
#         #只匹配 X-DSPAM-Confidence: 0.1234 的行，并提取冒号后的数字（含小数点）
#         stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#         # #如果提取失败，跳过该行
#         if len(stuff) != 1:
#             continue
#         num = float(stuff[0])
#         numlist.append(num)
#     print('Maximum: ', max(numlist))    # Maximum:  0.9907

import re

prompt = 'We just received $10.00 for cookies.'
match_str = re.findall(r'\$([0-9.]+)\S', prompt)
print(match_str)    # ['10.0'