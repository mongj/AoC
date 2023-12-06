with open("6.sample.txt", "r") as f:
    time = int(f.readline().split(':')[1].replace(" ",""))
    dist = int(f.readline().split(':')[1].replace(" ",""))


count = 0
for t in range(time + 1):
    dist_travelled = (time - t) * t
    if dist_travelled > dist:
        count += 1

print(count)