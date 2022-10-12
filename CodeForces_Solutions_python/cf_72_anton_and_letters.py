l=input()
l=[str(i) for i in l]
k=set(l)
k=list(k)
k.remove("{")
k.remove("}")
if " " in k: 
    k.remove(" ")
if "," in k:
    k.remove(",")
print(len(k))