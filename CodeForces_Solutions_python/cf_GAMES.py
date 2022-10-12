n=int(input())
l=[]
count=0
for i in range(n):
    a=input().split()
    a=[str(i) for i in a]
    l.append(a)
for i in range(len(l)):
    for j in range(0,len(l)):
        if  (j != i) and (l[i][0]==l[j][1]): 
            count+=1
print(count)
