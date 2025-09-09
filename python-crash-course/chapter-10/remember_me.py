from pathlib import Path
import json

def get_stored_username():
    """
    如果存储了用户名，就获取它
    """
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    return None

def greet_user():
    """
    问候用户，并指出其名字
    """
    path = Path('username.json')
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        path.write_text(json.dumps(username))
        print(f"We'll remember you when you come back, {username}!")

greet_user()