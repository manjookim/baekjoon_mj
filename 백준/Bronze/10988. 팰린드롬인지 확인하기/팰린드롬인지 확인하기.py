word = list(input())
cnt = 0
for i in range(len(word)//2):
    if word[i] != word[len(word)-i-1]:
        cnt += 1
if cnt == 0:
    print(1)
else:
    print(0)
        
