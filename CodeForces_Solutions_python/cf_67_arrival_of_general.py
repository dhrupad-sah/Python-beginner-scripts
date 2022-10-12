def duplicates(lst, item):
   return [i for i, x in enumerate(lst) if x == item]
n=int(input())
l=input().split()
l=[int(i) for i in l]
a=max(l)
swap=l.index(a)
l.remove(a)
l.insert(0,a)
b=min(l)
i=duplicates(l,b)
c=max(i)
print(swap+(len(l)-c)-1)
