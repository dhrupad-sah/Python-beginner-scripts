name=input()
# name=[str(i) for i in name]
host=input()
# host=[str(i) for i in host]
clause=input()
if len(name+host)!=len(clause):
    print("NO")
    exit()
clause=[str(i) for i in clause]
res=name+host
res=[str(i) for i in res]
res.sort()
clause.sort()
if clause==res:
    print("YES")
else:
    print("NO")