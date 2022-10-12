test=int(input())
for i in range(test):
    n,k=map(int,input().split())
    a=input().split()
    b=input().split()
    res=a
    res=[int(i) for i in res]
    a=[int(i) for i in a]
    b=[int(i) for i in b]
    a.sort()
    for i in range(len(a)):
        if a[i]<=k:
            ind=res.index(a[i])
            k+=b[ind]
            res.pop(ind)
            b.pop(ind)
        elif a[i]>k:
            break
    print(k)
    
