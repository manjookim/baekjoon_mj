def solution(s):
    answer = ''
    rsult = ''
    for i in s:
        if s.count(i) == 1:
            answer += i
    answer = sorted(answer)
    for i in answer:
        rsult += i
    return rsult