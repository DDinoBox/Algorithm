import sys

M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        word, X = temp[0], temp[1]
        X = int(X)

        if word == 'add':
            S.add(X)
        elif word == 'remove':
            S.discard(X)
        elif word == 'check':
            print(1 if X in S else 0)
        elif word == 'toggle':
            if X in S:
                S.discard(X)
            else:
                S.add(X)