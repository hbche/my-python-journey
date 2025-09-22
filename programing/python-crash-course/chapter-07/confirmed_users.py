# 首先创建一个待验证的用户列表
unconfirmed_users = ['alice', 'brian', 'candace']
# 创建一个空的用于存储经过验证的用户列表
confirmed_users = []
# 利用 while 循环移动列表
while unconfirmed_users:
    # 弹出未验证列表中最后的用户
    current_user = unconfirmed_users.pop()
    # 模拟验证过程
    print(f"Verifying user: {current_user.title()}")
    # 将验证过的用户添加到已验证列表中
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
# 显示所有已验证的用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())