with open('1.txt','r') as f:
    lines = (f.readlines())

map_table = [["one", "o1e"],["two", "t2o"],["three", "t3e"],["four", "f4r"],["five", "f5e"],["six", "s6x"],["seven", "s7n"],["eight", "e8t"],["nine", "n9e"]]

sum = 0

for l in lines:
    for c in map_table:
        l = l.replace(c[0], c[1])
    nums = list(filter(lambda x: x.isdigit(), l))
    sum = sum + int(nums[0]) * 10 + int(nums[-1])

print(sum)