from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    i = deque(people)
    while i:
        if len(i) >= 2:
            if i[0] + i[-1] <= limit:
                i.pop()
                i.popleft()
                answer += 1
            elif i[0] + i[-1] > limit:
                i.pop()
                answer += 1
        else:
            if i[0] <= limit:
                i.pop()
                answer += 1
    return answer