N = int(input())
result = 0
for each in range(N):
    x = list(input())
    arr = []
    while(1):
        i = 0
        while(1):
            i += 1
            if i == len(x) or x.count(x[0]) == len(x):
                break
            if x[0] != x[i] :
                arr.append(x[0])
                x = x[i:]
                break
            #print("x : ", x)
        if len(x) == 1 :
            arr.append(x[0])
            break
        if x.count(x[0]) == len(x):
            arr.append(x[0])
            break
        #print(arr)
    #print('arr:',arr)
    if len(arr) >= 2:
        cnt = 0
        for j in range(len(arr)-1):
            for k in range(j+1,len(arr)):
                if ord(arr[j]) == ord(arr[k]):
                    cnt+=1
        #print(cnt)
        if cnt == 0:
            result += 1
    else:
        result +=1
     #print(arr)
    #print(each , result)
        
    
print(result)
    