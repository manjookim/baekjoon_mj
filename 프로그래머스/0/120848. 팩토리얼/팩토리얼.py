def solution(n):
    for i in range(1,11):
        if factorial(i)>n:
            return i-1
        elif factorial(i) == n:
            return i
    
'''
    while(1):   
        i = 1
        if factorial(i) > n:
            return i-1
        else:
            i += 1
        
'''   
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n * factorial(n-1)
        
