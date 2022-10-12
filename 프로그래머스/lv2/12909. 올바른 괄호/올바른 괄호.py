def solution(s):
    answer = True
    result = []
    for i in s:
        if i == "(":
            result.append("(")
        if i == ")":
            if not result:
                answer = False
                break
            if "(" in result:
                result.pop()
        if not result:
            answer = True
        else:
            answer = False
    return answer