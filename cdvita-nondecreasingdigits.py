n=list(str(int(input())))
cnt=0
for i in range(len(n)-1):
    if n[i]<n[i+1]:
        cnt=i+1
        continue
    elif n[i]>n[i+1]:
        if i==0:
            n[i]=int(n[i])-1
            for j in range(1,len(n)):
                n[j]=9
            break
        elif i>0:
            n[cnt]=int(n[cnt])-1
            for k in range(cnt+1,len(n)):
                n[k]=9
            break
x="a"
for i in n:
    x=x+str(i)
x=x[1:]
print(int(x))
