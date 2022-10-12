def solution(s):
    s = s.split(' ')
    s_list = list(s)
    result_list = []
    for i in range(len(s_list)):
        word = s_list[i]
        x = word.capitalize()
        result_list.append(x)
        result = ' '.join(i for i in result_list)
    return result