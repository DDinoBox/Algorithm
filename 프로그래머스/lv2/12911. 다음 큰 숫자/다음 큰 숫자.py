def solution(n):
    answer = 0
    n_cnt = bin(n).count('1')
    i = n + 1
    while True:
        i_cnt = bin(i).count('1')
        if i_cnt == n_cnt:
            answer = i
            break
        else:
            i += 1
    return answer