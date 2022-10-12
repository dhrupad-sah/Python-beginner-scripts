n,m=map(int,input().split())
l=input().split()
l=[int(i) for i in l]
count=0
for i in range(len(l)):
    if i==0:
        count+=(l[i]-1)
    else:
        count+=(l[i]-1)
        if l[i]>l[i-1]:
            count-=(l[i-1]-1)
        elif l[i]<l[i-1]:
            count+=(n-l[i-1]+1)
        else:
            count-=(l[i]-1)
            continue
print(count)
    
