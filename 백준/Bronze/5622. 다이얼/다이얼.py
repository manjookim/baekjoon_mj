S = list(input())
t= 0
for i in range(len(S)):
    if S[i]<="C":
        t+=3
    elif S[i]<="F":
        t+= 4
    elif S[i] <= "I":
        t+=5
    elif S[i] <= "L":
        t+=6
    elif S[i] <= "O":
        t+=7
    elif S[i] <= "S":
        t+=8
    elif S[i] <= "V":
        t+=9
    elif S[i] <= "Z":
        t+=10
    else:
        t+=11
print(t)
