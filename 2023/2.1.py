import re

with open('2.txt','r') as f:
    lines = (f.readlines())

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

sum = 0
game_num = 1

for l in lines:
    blue_numbers = map(lambda x: int(x), re.findall(r'(\d+)\sblue', l))
    green_numbers = map(lambda x: int(x), re.findall(r'(\d+)\sgreen', l))
    red_numbers = map(lambda x: int(x), re.findall(r'(\d+)\sred', l))

    if (max(red_numbers) <= MAX_RED and
        max(green_numbers) <= MAX_GREEN and 
        max(blue_numbers) <= MAX_BLUE):
        sum = sum + game_num

    game_num = game_num + 1

print(sum)