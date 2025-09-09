from pathlib import Path
import json

def save_info(info, file):
    """
    将指定信息对象存储到给定的文件中
    """
    # 将信息对象转换成json字符串
    contents = json.dumps(info)
    path = Path(file)
    # 将信息对象json字符串写入到文件中
    path.write_text(contents)
    
def get_info(file):
    path = Path(file)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        info = json.loads(contents)
        return info
    
print("Enter your name, and I will remember it.")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
save_info({'first_name': first_name, 'last_name': last_name}, 'user_info.json')
user_info = get_info('user_info.json')
# print(user_info)
print(f"Hello, {user_info['first_name'].title()} {user_info['last_name'].title()}!")