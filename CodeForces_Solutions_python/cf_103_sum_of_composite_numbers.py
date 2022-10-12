num=int(input())
if num%2==0:
    k=num-4
    print(k,4)
else:
    i=4
    while(True):
        k=num-i
        if k%3==0:
            print(k,i)
            break
        else:
            i+=2
