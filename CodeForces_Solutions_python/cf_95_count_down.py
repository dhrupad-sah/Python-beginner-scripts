test=int(input())
for i in range(test):
    n=int(input())
    s=input()
    s=[int(i) for i in s]
    count=sum(s)
    for i in s:
        if i!=0:
            count+=1
    if s[-1]!=0:
        print(count-1)
    else:
        print(count)
