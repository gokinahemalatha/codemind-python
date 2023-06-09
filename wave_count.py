n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
e=[]
m=0
for i in range(len(a)):
    if i%2!=0:
        b.append(a[i])
    else:
        e.append(a[i])
for i in range(len(b)):
    if b[i]<e[i]:
        c=1
        break
if c==1:
    print(-1)
else:
    print(len(e)-1)