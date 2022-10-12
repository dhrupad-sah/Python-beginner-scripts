test=int(input())
for i in range(test):
    a,b=map(int,input().split())
    if a==b:
        print(0)
    else:
        count=0
        diff=abs(a-b)
        if diff>=10:
            count=int(diff/10)
            diff=diff%10
        if diff==0:
            print(count)
        else:
            print(count+1)
        # for i in range(9):
        #     k=9-i
        #     while(diff>=k):
        #         count+=1
        #         diff-=k
        #         if diff==0:
        #             print(count)
        #             break
