t=int(input())
last=[]
for i in range(t):
    n=int(input())
    monk=list(map(int,input().split()))[:n]
    asit=['A','B','C','D','E','F']
    temp=[]
    temp=asit
    cnt=0
    flag=[0]*n
    for i in range(n):
        j=monk[i]-1
        flag[j]=asit[i]
    temp=flag
    cnt+=1
    while temp!=asit:
        flag=[0]*n
        for i in range(n):
            j=monk[i]-1
            flag[j]=temp[i]
        temp=flag
        cnt+=1
    last.append(cnt)
for i in last:
    print(i)
        
