n=int(input())
l=input()
# l=[str(i) for i in l]
# k=[str(i) for i in l]
# k=set(k)
a=len(l)
b=len(set(l))
if a==b:
    print(0)
else:
    cpi=abs(a-b)
    if cpi<=(26-b):
        print(cpi)
    else:
        print(-1)