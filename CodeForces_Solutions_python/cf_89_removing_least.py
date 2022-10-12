test=int(input())
for i in range(test):
    n=int(input())
    l=input().split()
    l=[int(i) for i in l]
    # if n%2==0:
    #     print("NO")
    # elif len(set(l))==1:
    #     print("YES")
    # else:
    k=set(l)
    k=list(k)
    k.sort()
    if len(k)==1:
        print("YES")
    else:
        for i in range(len(k)-1):
            if abs(k[i]-k[i+1])!=1:
                print("NO")
                break
        else:
            print("YES")


            
        