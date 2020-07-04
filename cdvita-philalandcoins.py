t=int(input())
sol=[]
for i in range(t):
    x=int(input())
    cnt=0
    while x>=1:
        x=int(x/2)
        cnt+=1
    sol.append(cnt)
for j in sol:
    print(j)
