import sys

K, N = map(int, input().split())

result = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(result)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in result:
        lines += i // mid
        
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)