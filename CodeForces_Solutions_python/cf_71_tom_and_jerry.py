s=input()
s=[str(i) for i in s]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        s.pop(i-1)
        s.pop(i)
        i=0
        print(i)
        print(s)