import re

with open("4.txt", "r") as f:
    lines = f.readlines()

N_ROW = len(lines)

cards = [1] * N_ROW

for i in range(N_ROW):
    line = lines[i]

    l, r = line.split(" | ")

    win_num = {*l.split()[1:]}
    my_num = {*r.split()}
    
    win_count = len(win_num & my_num)

    for j in range(win_count):
        cards[i + j + 1] = cards[i + j + 1] + cards[i]

print(sum(cards))