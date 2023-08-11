x = (input())
cro_language = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro_language:
    x = x.replace(i, '*') #i를 *으로 바꾸어주는 함수
print(len(x))
