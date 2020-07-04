n=int(input())
coins=[]
x=n-4
j=x//5
coins.append(j)
c=4+(x%5)
if c%2==0:
    coins.append(2)
    c=c-2
elif c%2==1:
    coins.append(1)
    c=c-1
coins.append(c//2)
temp=coins[2]
coins[2]=coins[1]
coins[1]=temp
print(sum(coins),end=" ")
for i in coins:
    print(i,end=" " )
