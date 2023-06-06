n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
c=0
for i in a:
    if i>=l and i<=r:
        continue
    else:
        print(i,end=' ')
        c+=1
if c==0:
    print(-1)