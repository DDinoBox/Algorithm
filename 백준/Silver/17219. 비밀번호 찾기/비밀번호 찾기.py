import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MEMO = {}

for i in range(N):
    key, value = input().split()
    MEMO[key] = value

for i in range(M):
    key = input().strip()
    print(MEMO[key])