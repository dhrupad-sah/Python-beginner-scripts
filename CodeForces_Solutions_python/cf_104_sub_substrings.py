n=int(input())
for i in range(n):
    s=input()
    if len(s)>2:
        for i in range(1,int(len(s))-1):
            if i%2!=0:
                print(s[i-1],end="")
        print(s[-2]+s[-1])
    else:
        print(s)
    

    