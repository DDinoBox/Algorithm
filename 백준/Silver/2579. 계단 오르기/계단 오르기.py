import sys
input = sys.stdin.readline

N = int(input().rstrip())
l = [0]
for _ in range(N):
    l.append(int(input().rstrip()))

if N ==1:
    print(l[1])
else:
    DP = [0]*(N+1)
    DP[1] = l[1]
    DP[2] = l[1]+l[2]
    for i in range(3, N+1):
        DP[i] = max(DP[i-3]+l[i]+l[i-1], DP[i-2]+l[i])

    print(DP[N])