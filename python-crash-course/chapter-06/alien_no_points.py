# # 使用中括号语法访问不存在的键值对
# alien_no_points = {
#     "color": 'green',
#     'speed': 'slow'
#     }
# print(alien_no_points['points'])

# 使用 get() 方法获取不存在的键，并指定默认值
alien_no_points = {
    'color': 'green',
    'speed': 'slow'
    }
print(alien_no_points.get('points', 'No point value assigned.'))        # No point value assigned.