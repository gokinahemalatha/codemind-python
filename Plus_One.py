n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    while(n>=0):
        s=s+(i*(10**(n-1)))
        break
    n-=1
s=s+1
l=[]
while(s):
    r=s%10
    l.append(r)
    s=s//10
for i in range(len(l)-1,-1,-1):
    print(l[i],end=' ')