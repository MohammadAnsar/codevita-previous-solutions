import math
n=int(input())
g={}
count=0
for i in range(n):
    l=input().split()
    x=int(l[0])
    y=int(l[1])
    v=float(l[2])
    time=(math.sqrt(pow(x,2)+pow(y,2)))/v
    if(g.get(time)==None):
       g[time]=1
    else:
        g[time]+=1
for key in g:
    if g[key]!=1:
        for i in range(1,g[key]):
            count+=i
print(count)
