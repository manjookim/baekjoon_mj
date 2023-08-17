N,M = map(int,input().split())
A = []
B = []
arr = []

for i in range(N):
    i = list(map(int,input().split()))
    A.append(i)
    
for j in range(N):
    j = list(map(int,input().split()))
    B.append(j)

for i in range(N):
    arr.append([])
    

for i in range(N):
    for j in range(M):
        arr[i].append(A[i][j]+B[i][j])
        
for i in range(N):
    for j in range(M):
        print(arr[i][j],end =' ')
    print()
