T = int(input())

for i in range(T):
    result = []
    
    a = input()
    for j in a:
        if j == '(':
            result.append(j)
        elif j == ')':
            if result:
                result.pop()
            else:
                print("NO")
                break
    else:
        if not result: 
            print("YES")
        else:
            print("NO")