test=int(input())
for i in range(test):
    h=int(input())
    l=input().split()
    l=[int(i) for i in l]
    l.sort()
    k=max(l[:(h)])
    q=min(l[h:])
    print(abs(k-q))


