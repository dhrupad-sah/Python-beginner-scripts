p,q=map(int,input().split())
if p>q:
    a=q
else:
    a=p
b=abs(p-q)
print(a,int(b/2))