n1,n2=input().split()
n1=int(n1)
n2=int(n2)
prime=[]
for i in range(n1,n2+1):
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        prime.append(i)
li=[]
for k in range(len(prime)):
    for r in range(len(prime)):
        if k!=r:
            x=str(prime[k])+str(prime[r])
            xx=int(x)
            li.append(xx)
lo=[]
for i in li:
    if i not in lo:
        lo.append(i)
prime1=[]
for i in lo:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        prime1.append(i)
mini=min(prime1)
maxi=max(prime1)
count=len(prime1)
fib=[]
fib.append(mini)
fib.append(maxi)
tit=2
while tit<count:
    se=mini+maxi
    fib.append(se)
    mini=maxi
    maxi=se
    tit+=1
print(fib[-1])
