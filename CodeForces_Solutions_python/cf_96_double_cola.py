n=int(input())
sum=0
i=0
while((5*pow(2,i))<=n):
    i+=1
    print(i)
for i in range(i+1):
    sum+=5*(pow(2,i))
    print(sum)
diff=abs(sum-n)
if diff in range(pow(2,i)):
    print("h")
elif diff in range(pow(2,i),pow(2,(i+1))):
    print("r")
elif diff in range(pow(2,(i+1)),pow(2,(i+2))):
    print("p")
elif diff in range(pow(2,(i+2)),pow(2,(i+3))):
    print("l")
else:
    print("s")