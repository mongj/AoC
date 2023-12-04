with open("4.txt", "r") as f:
    lines = f.readlines()

sum = 0

for line in lines:

    l, r = line.split(" | ")

    win_num = {*l.split()[1:]}
    my_num = {*r.split()}
    
    win_count = len(win_num & my_num)

    if win_count > 0:
        sum = sum + pow(2, win_count - 1)

print(sum)