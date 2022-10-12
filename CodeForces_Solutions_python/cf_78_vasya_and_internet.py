s=input()
k=[str(i) for i in s]
if s[0]=="h":
    if (s[-1]=="u") and (s[-2]=="r"):
        p=s[4:len(s)-2]
        print("http://"+p+".ru")
    else:
        for i in range(len(s)):
            if (s[i]=="r") and (s[i+1]=="u"):
                if i==4:
                    continue
                else:
                    p=s[4:i]
                    r=s[i+2:]
                    print("http://"+p+".ru/"+r)
                    break
else:
    if (s[-1]=="u") and (s[-2]=="r"):
        p=s[3:len(s)-2]
        print("ftp://"+p+".ru")
    else:
        for i in range(len(s)):
            if (s[i]=="r") and (s[i+1]=="u"):
                if i==3:
                    continue
                else:
                    p=s[3:i]
                    r=s[i+2:]
                    print("ftp://"+p+".ru/"+r)
                    break
                

        

        


    