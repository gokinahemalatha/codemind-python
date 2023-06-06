n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
k=s//n
c=0
for i in a:
    if i<=k:
        c+=1
print(c)