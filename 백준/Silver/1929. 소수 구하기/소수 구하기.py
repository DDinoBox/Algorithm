import math

def prime(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

T = list(map(int, input().split()))
for i in range(T[0], T[1]+1):
    if prime(i):
        print(i)