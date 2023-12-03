with open('1.txt','r') as f:
    lines = (f.readlines())

sum = 0

for l in lines:
    nums = list(filter(lambda x: x.digit(), l))
    sum = sum + int(nums[0]) * 10 + int(nums[-1])

print(sum)