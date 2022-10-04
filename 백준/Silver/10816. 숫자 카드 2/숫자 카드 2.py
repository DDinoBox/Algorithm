from sys         import stdin
from collections import Counter

N     = stdin.readline()
N_num = stdin.readline().split()
M     = stdin.readline()
M_num = stdin.readline().split()

count = Counter(N_num)

print(' '.join(f'{count[i]}' if i in count else '0' for i in M_num))