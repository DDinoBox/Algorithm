import sys

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([y, x])

new_data = sorted(data)

for y,x in new_data:
    print(x,y)