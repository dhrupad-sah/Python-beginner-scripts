n,m=map(int,input().split())
l=input().split()
l=[int(i) for i in l]
l.sort()
r=[]
for i in range(m-n+1):
    k=l[i:(i+n)]
    Mi=min(k)
    Ma=max(k)
    r.append(Ma-Mi)
print(min(r))

