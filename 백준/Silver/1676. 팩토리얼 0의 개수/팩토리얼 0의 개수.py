N = int(input())

def five_count(N):
    count = 0
    while N != 0:
        N //= 5
        count += N
    return count
    
print(five_count(N))