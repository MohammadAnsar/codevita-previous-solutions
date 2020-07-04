n=int(input())
t=int(input())
x=[]
for i in range(n):
    l=list(map(int,input().split()))[:t+1]
    x.append(l)
for i in range(n):
    temp=0
    for j in range(t):
        x[i][j]=temp+(x[i][j]*x[i][t])
        temp=x[i][j]
xc={}
for j in range(1,t,2):
    lp=[]
    for i in range(n):
        lp.append(x[i][j])
    t=lp.index(max(lp))
    if (xc.get(t)==None):
        xc[t]=1
    else:
        xc[t]+=1
keymax=max(xc,key=xc.get)
print(keymax+1)
