import re

with open("5.1.txt", "r") as f:
    buffer = f.read()
    buffer = re.sub("\n\n", "\n", buffer)
    buffer = re.sub("seeds|[a-z\-]*\smap", "", buffer)
    buffer = buffer.split(':\n')[1:]

seeds = list(map(int, buffer[0].split()))
maps = [list(map(lambda x: list(map(int, x.split())), m.split('\n')[0:-1])) for m in buffer[1:]]
locations = []

for seed in seeds:
    src = seed
    dest = src
    for m in maps:
        dest = src
        for line in m:
            if src >= line[1] and src < line[1] + line[2]:
                dest = line[0] + src - line[1]
        src = dest
    locations.append(dest)

print(min(locations))