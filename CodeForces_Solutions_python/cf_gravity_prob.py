col=int(input())
l=input().split()
l=[int(i) for i in l]
l.sort()
# q.sort()
# while(l!=q):
#     for i in range(col-1):
#         if l[i]>l[i+1]:
#             l[i]=l[i]-1
#             l[i+1]=l[i+1]+1
print(*l)


