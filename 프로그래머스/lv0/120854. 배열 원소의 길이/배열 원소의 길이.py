def solution(strlist):
    arr = []
    for each in strlist:
        arr.append(len(each.strip('"')))
    return arr

solution(["We", "are", "the", "world!"])