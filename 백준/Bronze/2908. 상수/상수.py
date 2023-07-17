A, B = input().split()
A = list(A)
B = list(B)
A.reverse()
B.reverse()
A = ''.join(x for x in A)
B = ''.join(x for x in B)
if A > B:
    print(A)
else:
    print(B)