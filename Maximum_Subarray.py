n=int(input())
a=list(map(int,input().split()))
s=0
m=-999
for i in range(n):
    s=a[i]
    if s>m:
        m=s
    for j in range(i+1,n):
        s=s+a[j]
        if s>m:
            m=s
print(m)