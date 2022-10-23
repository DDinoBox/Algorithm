def solution(brown, yellow):
    result = brown + yellow
    for i in range(1, result+1):
        if (result / i) % 1 == 0:
            j = result // i
            if j >= i:
                if 2*i + 2*j == brown + 4:
                    answer = [j,i]
                    return answer