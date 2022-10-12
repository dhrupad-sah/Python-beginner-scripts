m,n=map(int,input().split())
count=0
for i in range(1,(n+1)):
    rem=i%5
    for j in range(1,(m+1)):
        if (j%5)+rem==5:
            count+=1
print(count+(int(m/5))*int(n/5))