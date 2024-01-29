def solution(s):
    ctrl_z = s.split()
    answer = 0
    for i in range(len(ctrl_z)):
        if ctrl_z[i] == 'Z':
            answer -= int(ctrl_z[i-1])
        elif ctrl_z[i] == ' ':
            answer += 0
        else:
            answer += int(ctrl_z[i])
    return answer