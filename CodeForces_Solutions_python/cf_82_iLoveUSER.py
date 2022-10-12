n=int(input())
num=input().split()
count=0
num=[int(i) for i in num]
for i in range(1,n):
    seg=num[:i]
    ma=max(seg)
    m=min(seg)
    if (num[i]<m) or (num[i]>ma):
        count+=1
print(count)



