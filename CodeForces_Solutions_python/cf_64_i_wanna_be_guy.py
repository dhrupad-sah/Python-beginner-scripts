n=int(input())
l=input().split()
m=input().split()
l=[int(i) for i in l]
m=[int(i) for i in m]
l.remove(l[0])
m.remove(m[0])
k=set(l+m)
if len(k)>=n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")