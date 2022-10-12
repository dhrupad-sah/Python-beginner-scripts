n,m=map(int,input().split())
# l=[1,2,6,7,8,9,1]
diff=0
# l.sort(reverse=True)
# for i in range(1,len(l)):
#     if i==1:
#         diff=l[i-1]-l[i]
#     else:
#         d=l[i-1]-l[i]
#         if d>diff:
#             diff=d
# print(diff)

l=input().split()
l=[int(i) for i in l]
l.sort(reverse=True)
for i in range(1,len(l)):
    if i==1:
        diff=l[i-1]-l[i]
    else:
        d=l[i-1]-l[i]
        if d>diff:
            diff=d
        else:
            continue
k=m-l[0]
q=l[-1]
r=diff/2
print(max(k,q,r))
