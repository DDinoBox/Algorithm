def solution(s):
    zero_count = 0
    conversion_count = 0
    while True:
        if s == '1':
            break
        else:
            count = s.count('0')
            zero_count += count
            conversion_count += 1
            new_s = s.replace('0', '')
            s = len(new_s)
            s = format(int(s), 'b')
    answer = [conversion_count, zero_count]
    return answer