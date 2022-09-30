import sys

n = int(sys.stdin.readline())
co = []

for i in range(n):
    co.append(list(map(int, sys.stdin.readline().split())))
co.sort(key=lambda x: (x[0], x[1]))

for i in co:
    print(i[0], i[1])