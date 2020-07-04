n,k=input().split()
n=int(n)
k=int(k)
xx=[]
lis=list(map(int,input().split()))[:n]
for i in range(k):
    lr,hr=input().split()
    lr=int(lr)
    hr=int(hr)
    cnt=0
    for j in lis:
        if j in range(lr,hr+1):
            cnt+=1
    xx.append(cnt)
for k in xx:
    print(k,end=" ")
