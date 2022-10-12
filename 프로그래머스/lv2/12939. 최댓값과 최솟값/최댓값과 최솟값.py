def solution(s):
    s = s.split(' ')
    s = list(map(int, s))
    s_min = min(s)
    s_max = max(s)
    answer = str(s_min) + ' ' + str(s_max)
    return answer