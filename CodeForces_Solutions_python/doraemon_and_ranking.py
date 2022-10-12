test=int(input())
for i in range(test):
    n,x=map(int,input().split())
    l=input().split()
    l=[int(i) for i in l]
    l=set(l)
    l=list(l)
    l.sort()
    a=x
    if len(l)==1:
        if l[0]<x:
            print(x)
            break
        else:
            print(x+1)
            break
    else:
        k=[range(1,x)]
        for i in k:
            if i in l:
                p=1
                k.append(x+p)
                p+=1
            else:
                if a>0:
                    a-=1
        print(k[-1])


        
