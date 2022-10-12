n=int(input())
# height=0
c=1
s=1
# while(n!=0):
#     i=int((c*(c+1))/2)
#     print(i)
#     if n-i>=0:
#         height+=1
#         n-=i
#         c+=1
#     else:
#         break
# print(height)
if n==0:
    print(0)
    exit()
while(True):
    if n>=s:
        c+=1
        n-=s
        s=int((c*(c+1))/2)

    else:
        break

print(c-1)
    

