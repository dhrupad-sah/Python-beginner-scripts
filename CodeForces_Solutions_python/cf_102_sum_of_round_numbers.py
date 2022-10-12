test=int(input())
for i in range(test):
    num=input()
    l=[]
    for i in range(len(num)):
        if num[i]!="0":
            ind=num.index(num[i])
            k=num[i]+("0"*(len(num)-i-1))
            l.append(k)
    res=" ".join([str(i) for i in l])
    print(len(l))
    print(res)


        


