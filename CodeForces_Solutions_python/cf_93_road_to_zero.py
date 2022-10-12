test=int(input())
count=0
for i in range(test):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    diff=abs(x-y)
    count=a*diff
    if x>y:
        h=x
        l=y
    else:
        h=y
        l=x
    count1=(l*b)
    count2=(l*2*a)
    if count1>count2:
        print(count+count2)
    else:
        print(count+count1)
