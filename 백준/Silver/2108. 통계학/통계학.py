from collections import Counter
from itertools import count
import sys

N = int(sys.stdin.readline())

num = []
for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

count = Counter(num).most_common()

print(round(sum(num) / N))

print(num[N // 2])

if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
        
else:
    print(count[0][0])

print(num[-1] - num[0])