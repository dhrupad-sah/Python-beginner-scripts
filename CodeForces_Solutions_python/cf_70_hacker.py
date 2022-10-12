n,m=map(int,input().split())
ip=[]
for i in range(n):
    a,b=input().split()
    b=b+";"
    l=[a,b]
    ip.append(l)
names=[]
for i in range(m):
    a,b=input().split()
    l=[a,b]
    names.append(l)
# print(names)
# print(ip)
for i in range(n):
    for j in range(m):
       if ip[i][1]==names[j][1]:
           print(*names[j]," #",ip[i][0])
            
