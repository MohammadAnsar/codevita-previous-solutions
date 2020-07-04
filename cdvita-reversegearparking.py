test=int(input())
last=[]
for i in range(test):
    f,b,t,d=map(int,input().split())
    time=0
    dist=0
    while dist<=d:
        dist+=b
        time+=(b*t)
        if dist>=d:
            break
        elif dist<d:
            dist-=f
            time+=(f*t)
    if dist>d:
        time=time-((dist-d)*t)
    last.append(time)
for i in last:
    print(i)
