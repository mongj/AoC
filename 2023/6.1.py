with open("6.sample.txt", "r") as f:
    time = list(map(int, f.readline().split()[1:]))
    dist = list(map(int, f.readline().split()[1:]))

race_count = len(time)
margin = 1

for i in range(race_count):
    min_dist = dist[i]
    count = 0
    for t in range(time[i] + 1):
        dist_travelled = (time[i] - t) * t
        if dist_travelled > min_dist:
            count += 1
    margin *= count

print(margin)