import sys

n    = int(sys.stdin.readline())
data = []

for _ in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")