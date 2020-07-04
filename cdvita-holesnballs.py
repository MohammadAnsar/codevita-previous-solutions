n=int(input())
bokkalu=list(map(int,input().split()))[:n]
#bokkal=list(reversed(bokkalu))
m=int(input())
balls=list(map(int,input().split()))[:m]
dic={}
for i in range(m):
    for j in range(n):
        if ((balls[i]<=bokkalu[j]) and (dic.get(j)==None)):
            balls[i]=j+1
            dic[j]=1
        elif ((balls[i]<=bokkalu[j]) and (dic.get(j)<j+1)):
            balls[i]=j+1
            dic[j]+=1
        elif ((balls[i]<=bokkalu[j]) and (dic.get(j)==j+1)):
            continue
        elif (((balls[i]>bokkalu[j])or ((balls[i]<=bokkalu[j]) and (dic.get(j)==j+1))) and (j==n-1)):
            balls[i]=0
for i in balls:
    print(i,end=" ")
