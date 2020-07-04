slabs=list(map(int,input().split()))
rates=list(map(int,input().split()))
rebate=int(input())
emp_tax=list(map(int,input().split()))
slab_tax=[]
x=0
for i in range(len(slabs)):
    if i==0:
        slab_tax.append(x)
    elif i>0:
        x+=int(((slabs[i]-slabs[i-1])*rates[i-1])/100)
        slab_tax.append(x)
total=0
for j in emp_tax:
    summ=0
    for k in range(len(slab_tax)):
        if j<=slab_tax[k]:
            summ=summ+slabs[k-1]
            taxx=j-slab_tax[k-1]
            sall=(taxx*100)/rates[k-1]
            sal=sall+summ
            salary=sal+rebate
            #print(salary)
            total=total+salary
            break
        elif ((k==len(slab_tax)-1) and j>slab_tax[k]):
            summ=summ+slabs[k]
            taxx=j-slab_tax[k]
            sall=(taxx*100)/rates[k]
            sal=sall+summ
            salary=sal+rebate
            #print(salary)
            total=total+salary
print(total)
