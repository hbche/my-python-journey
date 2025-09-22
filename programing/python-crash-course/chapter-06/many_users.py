# 在字典中存储字典
many_users = {
    'robin': {
        'first': 'robin',
        'last': 'che',
        'location': 'Wuhan',
        },
    "sam": {
        'first': 'sam',
        'last': 'alter',
        'location': 'Guangzhou',
        }
    }
for user, info in many_users.items():
    print(f"\nUsername: {user}")
    full_name = f"{info['first']} {info['last']}"
    location = info['location']

    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")