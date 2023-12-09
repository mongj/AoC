with open("9.sample.txt", "r") as f:
    lines = f.readlines()

def oasis_predict(seq):
    if all(v == 0 for v in seq):
        return 0
    else:
        next_line = [seq[i] - seq[i - 1] for i in range(1, len(seq))]
        return seq[0] - oasis_predict(next_line)

pred = []

for line in lines:
    line = list(map(int, line.split()))
    pred.append(oasis_predict(line))

print(sum(pred))
