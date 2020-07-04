p=int(input())
time=int(input())
ding=[]
for i in range(2):
    n=int(input())
    summ=0
    for i in range(n):
        peri,rate=input().split()
        peri=int(peri)
        rate=float(rate)
        rx=pow((1+rate),(peri*12))
        emi=p*rate/(1-1/rx)
        summ+=emi
    ding.append(summ)
if ding[0]<ding[1]:
    print("Bank A")
elif ding[1]<ding[0]:
    print("Bank B")
