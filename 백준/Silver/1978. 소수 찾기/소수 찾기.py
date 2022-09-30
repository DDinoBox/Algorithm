import sys

N        = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

count = 0
for i in num_list:
    error = 0
    if i > 1:
        for j in range(2, i//2+1):    
            if (i % j == 0):
                error += 1
        if error == 0:
            count += 1

print(count)