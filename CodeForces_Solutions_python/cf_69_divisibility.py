import math
test=int(input())
for i in range(test):
    a,b=map(int,input().split())
    n=math.ceil(a/b)
    print(b*n-a)