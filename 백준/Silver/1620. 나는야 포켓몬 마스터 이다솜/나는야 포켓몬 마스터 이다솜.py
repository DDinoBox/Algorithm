import sys
from unittest import result

input = sys.stdin.readline

N, M = map(int, input().split())

result = {}

for i in range(1, N + 1):
    j = input().rstrip()
    result[i] = j
    result[j] = i

for i in range(M):
    quest = input().rstrip()
    if quest.isdigit():
        print(result[int(quest)])
    else:
        print(result[quest])