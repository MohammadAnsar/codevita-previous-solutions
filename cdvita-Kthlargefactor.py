n,k=input().split(',')
n=int(n)
k=int(k)
ar=[]
for i in range(1,n+1):
    if n%i==0:
        ar.append(i)
if k<len(ar):
    print(ar[-k])
else:
    print("1")
