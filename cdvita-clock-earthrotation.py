period=int(input())
long=float(input())
time=(period*long)/360
hrs=int(time)
mins=int(((time-hrs)*30)//0.5)
if hrs==12:
    hrs=0
hrangle=(hrs*30)+(mins*0.5)
minangle=mins*6
x=abs(hrangle-minangle)
if x<180:
    print("{0: .2f}".format(x))
elif x>180:
    print("{0: .2f}".format(360-x))
