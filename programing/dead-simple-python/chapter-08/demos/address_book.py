# 定义一个存储朋友名称到邮箱地址的字典
friend_emails = {
    "Anne": "anne@example.com",
    "Brent": "brent@example.com",
    "Dan": "dan@example.com",
    "David": "david@example.com",
    "Fox": "fox@example.com",
    "Jane": "jane@example.com",
    "Kevin": "kevin@example.com",
    "Robert": "robert@example.com",
}

def look_email(name):
    """通过名称从字典中查找邮箱地址"""
    try:
        return friend_emails[name]
    except KeyError as e:
        print(f"<No entry for friend {e}>")
        
# 同用户输入获取查找的名称
name = input("Enter name to look up: ")
# 查找邮箱地址
email = look_email(name)
# 打印邮箱地址
print(f"Email: {email}")