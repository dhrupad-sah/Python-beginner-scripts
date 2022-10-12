test=int(input())
for i in range(test):
    a,n=map(int,input().split())
    if n==a:
        print(0)
    elif (n%2!=0) and (a%2!=0):
        print(-1)
    else:
        count=0
        count1=0
        if a>n:
            h=a
            s=n
        else:
            h=n
            s=a
        while(s%8==0):
            s/=8
            count1+=1
        while(s%4==0):
            s/=4
            count1+=1
        while(s%2==0):
            s/=2
            count1+=1
        
        while(h%8==0):
            h/=8
            count+=1
        while(h%4==0):
            h/=4
            count+=1
        while(h%2==0):
            h/=2
            count+=1
        if (h==s):
            print(count-count1)
        else:
            print(-1)