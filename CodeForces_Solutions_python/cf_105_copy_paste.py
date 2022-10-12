test=int(input())
for i in range(test):
    n,k=map(int,input().split())
    l=input().split()
    l=[int(i) for i in l]
    l.sort()
    count=0
    k1=min(l)
    for i in range(1,n):
        diff=k-l[i]
        count+=(int(diff/k1))
    # for i in range(1,n-1):
    #     if l[i]<k:
    #         while(l[i]<k):
    #             count+=1
    #             l[i]+=k1
    #     else:
    #         break
    print(count)




