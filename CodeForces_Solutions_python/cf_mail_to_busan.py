l = {}
num=int(input())
for _ in range(num):
    s=input()
    if s not in l.keys():
        l[s] = 0#direct appeding
        print("OK")
    else:
        a=l[s]
        l[s] = a+1
        print(s+str(l[s]))


