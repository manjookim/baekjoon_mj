def solution(array, n):
    answer = array[0]
    cnt = abs(array[0]-n)
    for i in array:     
        if abs(i-n) < cnt :
            answer = i
            cnt = abs(i-n)
        elif abs(i-n) == cnt:
            answer = min(answer,i)   
    return answer