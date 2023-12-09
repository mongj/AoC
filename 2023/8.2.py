from math import lcm

with open("8.sample.txt", "r") as f:
    lines = f.read().split('\n')

instructions = lines[0]
nodes = {}
for n in lines[2:]:
    tmp = n.split(' = ')
    nodes[tmp[0]] = (tmp[1][1:4], tmp[1][6:9])

starting_nodes = [k for (k, v) in nodes.items() if k[-1] == 'A']

steps = []

for node in starting_nodes:
    count = 0
    found = False

    while True:
        if found:
            steps.append(count)
            break
        else:
            for i in instructions:
                if node[-1] == 'Z':
                    found = True
                    break

                if i == "L":
                    node = nodes[node][0]
                else:
                    node = nodes[node][1]

                count += 1

print(lcm(*steps))