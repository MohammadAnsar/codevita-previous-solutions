import math
x_l=int(input())
y_l=int(input())
x_w=int(input())
y_w=int(input())
f=float(input())
speed=1
xi=x_w
dist1=math.sqrt((pow((x_l-xi),2)+pow(y_l,2)))
dist2=math.sqrt((pow((x_w-xi),2)+pow(y_w,2)))
time1=dist1/(speed*f)
time2=dist2/(speed)
ptime=time1+time2
if x_w==x_l:
    print("{0: .6f}".format(x_l))
if x_w > x_l:
   while xi>=x_l:
        xi-=0.000001
        dist1=math.sqrt((pow((x_l-xi),2)+pow(y_l,2)))
        dist2=math.sqrt((pow((x_w-xi),2)+pow(y_w,2)))
        time1=dist1/(speed*f)
        time2=dist2/(speed)
        time=time1+time2
        if time<ptime:
            ptime=time
        elif time>ptime:
            roo=xi+0.000001
            print(round(roo,6))
            break    
elif x_w < x_l:
    while xi!=x_l:
        xi+=0.000001
        dist1=math.sqrt((pow((x_l-xi),2)+pow(y_l,2)))
        dist2=math.sqrt((pow((x_w-xi),2)+pow(y_w,2)))
        time1=dist1/(speed*f)
        time2=dist2/(speed)
        time=time1+time2
        if time<ptime:
            ptime=time
        elif time>ptime:
            print(round((xi-0.000001),6))
            break  
