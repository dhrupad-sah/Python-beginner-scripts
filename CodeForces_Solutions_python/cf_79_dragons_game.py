s,n=map(int,input().split())
d=[]
res=[]
bonus=[]
for i in range(n):
    x,y=map(int,input().split())
    d.append(x)
    res.append(x)
    bonus.append(y)
    d.sort()
for i in range(len(d)):
    if s>d[i]:
        ind=res.index(d[i])
        s+=bonus[ind]
        res.pop(ind)
        bonus.pop(ind)
    else:
        print("NO")
        exit()
print("YES")