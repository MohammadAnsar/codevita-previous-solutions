t=int(input())
fin=[]
for i in range(t):
    n=int(input())
    li=list(map(int,input().split()))[:n]
    lo=list(sorted(li))
    su=lo[0]
    ro=[]
    for j in range(1,n):
        su+=lo[j]
        ro.append(su)
    tot=0
    for k in ro:
        tot+=k
    fin.append(tot)
for se in fin:
    print(se)
