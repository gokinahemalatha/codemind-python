n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
l=[]
for i in a:
    if i not in b:
        l.append(i)
        c+=1
for i in b:
    if i not in a:
        l.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*l)