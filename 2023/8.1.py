with open("8.sample.txt", "r") as f:
    lines = f.read().split('\n')

instructions = lines[0]
nodes = {}
for n in lines[2:]:
    tmp = n.split(' = ')
    nodes[tmp[0]] = (tmp[1][1:4], tmp[1][6:9])

steps = 0
curr = 'AAA'
target = 'ZZZ'
found = False

while True:
    if found:
        break
    else:
        for i in instructions:
            if curr == target:
                found = True
                break

            if i == "L":
                curr = nodes[curr][0]
            else:
                curr = nodes[curr][1]

            steps += 1


print(steps)