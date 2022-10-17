T = int(input())
 
for _ in range(T):
    zero_count = [1,0]
    one_count = [0,1]
    N = int(input())
    if N > 1:
        for i in range(N-1):
            zero_count.append(one_count[-1])
            one_count.append(zero_count[-2]+one_count[-1]) 
 
    print(zero_count[N], one_count[N])