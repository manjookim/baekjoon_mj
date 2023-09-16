def solution(n):
    answer = []
    if n%2 == 0:
        for i in range(n//2):        
            answer.append(i*2+1)
    else:
        for i in range(n//2+1):        
            answer.append(i*2+1)
        

    return answer