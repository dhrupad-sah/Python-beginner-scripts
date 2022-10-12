n,m=map(int,input().split())
names=[]
res=names
ip=[]
action=[]
res2=action
ip2=[]
for i in range(n):
    a,b=input().split()
    b=b+";"
    a="#"+a
    names.append(a)
    ip.append(b)
for i in range(m):
    a,b=input().split()
    action.append(a)
    ip2.append(b)
names=ip
action=ip2
for i in range(m):
    for j in range(n):
        if action[i]==names[j]:
            print(res2[i],action[i],res[j])