n,a,b,c=map(int,input().split())
mi=min(a,b,c)
ma=max(a,b,c)
med=a+b+c-mi-ma
count=0
while(n!=0):
    if (n-mi>0) and ((n-mi) in (a,b,c)):
        n-=mi
        count+=1
    elif (n-med>0) and ((n-med) in (a,b,c)):
        n-=med
        count+=1
    elif (n-ma>0) and (n-ma) in (a,b,c):
        n-=ma
        count+=1