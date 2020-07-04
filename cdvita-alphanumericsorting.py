t=int(input())
final=[]
for i in range(t):
    words=[]
    numbers=[]
    last=[]
    l=list(input().split())
    for j in range(len(l)):
        if j%2==0:
            words.append(str(l[j]).lower())
        elif j%2==1:
            numbers.append(int(l[j]))
    words=list(sorted(words))
    numbers=list(sorted(numbers))
    x=min(len(words),len(numbers))
    for i in range(x):
        last.append(words[i])
        last.append(numbers[i])
    if len(words)>len(numbers):
        for i in range(len(words)-len(numbers),len(words)):
            last.append(words[i])
    elif len(words)<len(numbers):
        for i in range(len(numbers)-len(words),len(numbers)):
            last.append(numbers[i])
    final.append(last)
for j in final:
    for k in j:
        print(k,end=" ")
    print()
