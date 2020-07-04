t=int(input())
last=[]
for i in range(t):
    s=str(input())
    j=1
    dup=[]
    s=list(s)
    cj=0
    for don in s:
        if don not in dup:
            dup.append(don)
    for son in dup:
        l=s.count(son)
        if l==ord(son)-96:
            cj+=1
            #print(ord(son)-96)
    if cj==len(dup):
        last.append("Yes")
    elif cj!=len(dup):
        last.append("No")
for u in last:
    print(u)
