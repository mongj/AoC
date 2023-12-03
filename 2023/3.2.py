with open('3.txt','r') as f:
    lines = (f.readlines())

N_ROW = len(lines)
N_COL = len(lines[0]) - 1

def is_next_elem_num(r, c):
    try:
        return lines[r][c + 1].isdigit()
    except:
        return False

def is_prev_elem_num(r, c):
    try:
        return lines[r][c - 1].isdigit()
    except:
        return False

def get_num(r, c):
    start_col = end_col = c
    # look back
    while is_prev_elem_num(r, start_col):
        start_col = start_col - 1
    # look ahead
    while is_next_elem_num(r, end_col):
        end_col = end_col + 1
    
    return (r, start_col, end_col)

sum = 0

for i in range(N_ROW):
    line = lines[i]
    for j in range(N_COL):
        if line[j] == "*":
            # check the 9 adjacent cells
            nums = set()
            for r in range (i - 1, i + 2):
                for c in range (j - 1, j + 2):
                    try:
                        if lines[r][c].isdigit():
                            nums.add(get_num(r,c))
                    except:
                        continue
            
            if len(nums) == 2:
                g1 = nums.pop()
                g2 = nums.pop()
                gear_ratio = int(lines[g1[0]][g1[1]:g1[2] + 1]) * int(lines[g2[0]][g2[1]:g2[2] + 1])
                sum = sum + gear_ratio

print(sum)