n=int(input())
i=0
d=[]
while n>0:
    d.append(n%10)
    n=n//10
    i+=1
for j in range(i-1,-1,-1):
    if d[j]==6:
        d[j]=9
        break
for k in range(i-1,-1,-1):
    print(d[k],end='')