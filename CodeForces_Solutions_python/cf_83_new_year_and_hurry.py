n,t=map(int,input().split())
time=240-t
req=5
count=0
while(time>=req):
    count+=1
    time-=req
    req=5*(count+1)
if count<=n:
    print(count)
else:
    print(n)