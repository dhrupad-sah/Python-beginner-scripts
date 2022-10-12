import math
a,b=map(int,input().split())
if a==b:
    n=a
elif a>b:
    n=b
else:
    n=a
if n%2!=0:
    print("Akshat")
else:
    print("Malvika")