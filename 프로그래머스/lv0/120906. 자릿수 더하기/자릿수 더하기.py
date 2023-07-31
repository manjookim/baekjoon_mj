def solution(n):
    n = str(n)
    arr = list(n)
    arr = list(map(int,n))
    sum = 0
    for each in arr:
        sum += each
    return sum