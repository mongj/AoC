with open('3.txt','r') as f:
    lines = (f.readlines())

char_set = {'&', '$', '#', '-', '*', '=', '%', '/', '@', '+'}

sum = 0
N_ROW = len(lines)
N_COL = len(lines[0]) - 1
num_start = None
num_end = None

def is_part_number(row, start, end):
    top_row = max(0, row - 1)
    bottom_row = min(N_ROW - 1, row + 1)
    left_col = max(0, start - 1)
    right_col = min(N_COL - 1, end + 1)
    #print([top_row, bottom_row, left_col, right_col])

    for i in range(top_row, bottom_row + 1):
        for j in range(left_col, right_col + 1):
            print(f"i: {i} j: {j}")
            print(f"i: {i} j: {j} val: {lines[i][j]}")
            if lines[i][j] in char_set:
                return True
    return False

def is_next_elem_num(line, idx):
    try:
        return line[idx + 1].isdigit()
    except:
        return False

for i in range(N_ROW):
    line = lines[i]
    for j in range(N_COL):
        if line[j].isdigit() and num_start is None:
            num_start = j
        
        if num_start is not None and not is_next_elem_num(line, j):
            num_end = j
            if is_part_number(i, num_start, num_end):
               sum = sum + int(line[num_start:num_end + 1])

            num_start = None
            num_end = None

print(sum)