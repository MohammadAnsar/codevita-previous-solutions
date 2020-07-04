n=int(input())
prime=[]
for i in range(2,n+1):
    cnt=0
    for j in range(1,n+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        prime.append(i)
cnt=0
for y in prime[1:]:
    tot=0
    r=0
    while tot<y and r<=len(prime):
        tot+=prime[r]
        r+=1
        if tot==y:
            cnt+=1
            break
print(cnt)

