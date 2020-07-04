def ncr(n,r):
    return int((fact(n)/fact(r))*fact(n-r))
def fact(n):
    res=1
    for i in range(2,n+1):
        res=res*i
    return res
def coprime(p,q):
    temp=0
    x=min(p,q)
    for i in range(1,x+1):
        if (p%i==0 and q%i==0):
            temp=i
    if temp==1:
        pass
    else:
        p=p//temp
        q=q//temp
def mulinv(a):
    m=1000000007
    for i in range(1,m+1):
        if i*(m+1)%a==0:
            b=i*(m+1)//a
            break
    return b
k=int(input())
loje=[]
for i in range(k):
    n,t,m=map(int,input().split())
    p=ncr(n,t)-ncr(m,t)
    q=ncr(n,t)
    coprime(p,q)
    gg=p*mulinv(q)
    loje.append(gg)
for i in loje:
    print(i//2)
    
    
    
    
