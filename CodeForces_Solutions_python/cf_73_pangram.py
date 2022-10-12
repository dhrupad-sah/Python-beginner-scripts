import string
n=int(input())
s=input().lower()
s=[str(i) for i in s]
l=list(string.ascii_lowercase) 
count=0
if len(s)>=26:
    for i in s:
        if i in l:
            count+=1
            l.remove(i)
        if count==26:
            print("YES")
            break
    if count!=26:
        print("NO")
else:
    print("NO")
