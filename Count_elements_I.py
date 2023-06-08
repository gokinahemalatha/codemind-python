n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
d=[]
s=0
for i in a:
    if i in b:
        c.append(i)
for i in c:
    if i not in d:
        d.append(i)
        s+=1
print(s)