from urllib.robotparser import RobotFileParser

robot_file_url = 'https://www.baidu.com/robots.txt'
robot_parser = RobotFileParser(robot_file_url)
robot_parser.read()
print(robot_parser.can_fetch('Baiduspider', 'https://www.baidu.com'))       # True
print(robot_parser.can_fetch('Baiduspider', 'https://www.baidu.com/homepage/'))     # True
print(robot_parser.can_fetch('Googlebot', 'https://www.baidu.com/homepage/'))       # False
