a,b,c,d=map(int,input().split())
m=max(a,b,c,d)
l=[a,b,c,d]
l.remove(m)
n1=m-l[0]
n2=m-l[1]
n3=m-l[2]
print(n1,n2,n3)
