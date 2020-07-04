import itertools
from itertools import combinations
hrs,mins,secs=0,0,0
li=list(input().split(','))
comb=list(combinations(li,2))
jojo=[]
for i in comb:
    ding=str(i[0])+str(i[1])
    ding=int(ding)
    if li.count(0)>=4:
        if ding<=24:
            jojo.append(ding)
    elif li.count(0)<4:
        if ding<24:
            jojo.append(ding)
if len(jojo)==0:
    hrs="Impossible"
elif len(jojo)>0:
    hrs=max(jojo)
    hr=list(str(hrs))
    li.remove(hr[0])
    li.remove(hr[1])
comb1=list(combinations(li,2))
jojo1=[]
for i in comb1:
    ding=str(i[0])+str(i[1])
    ding=int(ding)
    if hrs==24:
        if ding==0:
            jojo1.append(ding)
    elif hrs!=24:
        if ding<60:
            jojo1.append(ding)
if len(jojo1)==0:
    mins="Impossible"
elif len(jojo1)>0:
    mins=max(jojo1)
    mi=list(str(mins))
    li.remove(mi[0])
    li.remove(mi[1])
comb2=list(combinations(li,2))
jojo2=[]
for i in comb2:
    ding=str(i[0])+str(i[1])
    ding=int(ding)
    if hrs==24:
        if ding==0:
            jojo2.append(ding)
    elif hrs!=24:
        if ding<60:
            jojo2.append(ding)
if len(jojo2)==0:
    secs="Impossible"
elif len(jojo2)>0:
    secs=max(jojo2)
if (hrs!="Impossible" and secs!="Impossible" and mins!="Impossible"):
    print(hrs,end=":")
    print(mins,end=":")
    print(secs)
else:
    print("Impossible")
