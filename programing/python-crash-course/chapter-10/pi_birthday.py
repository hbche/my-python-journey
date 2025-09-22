from pathlib import Path

path = Path('pi_million_digits.txt')
lines = path.read_text().strip().splitlines()

pi_string = ''
for line in lines:
    pi_string += line
    
birthday = input('Enter your birthday, in the form mmddyy: ')
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday doesn't appear in the first million digits of pi.")