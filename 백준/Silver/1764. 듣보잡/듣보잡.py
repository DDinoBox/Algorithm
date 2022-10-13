import sys

n, m = map(int,sys.stdin.readline().split())
N = [sys.stdin.readline().strip() for i in range(n)]
M = [sys.stdin.readline().strip() for i in range(m)]

duplicate_list = []

duplicate_list = list(set(N) & set(M))

print(len(duplicate_list))
for name in sorted(duplicate_list):
    print(name)