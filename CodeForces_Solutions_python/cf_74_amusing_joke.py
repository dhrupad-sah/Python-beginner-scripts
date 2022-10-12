name=input()
name=[str(i) for i in name]
host=input()
host=[str(i) for i in host]
clause=input()
caluse=[str(i) for i in clause]
res=[str(i) for i in clause]
for i in clause:
    if len(clause)<(len(name) + len(host)):
        print("NO")
        exit()
    elif (len(host)>0) and (i in host):
        host.remove(i)
        res.remove(i)
    
    elif (len(name)>0) and (i in name):
        name.remove(i)
        res.remove(i)
if (len(host)==0) and (len(name)==0) and (len(res)==0):
    print("YES")
else:
    print("NO")