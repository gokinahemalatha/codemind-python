n=int(input())
a=list(map(int,input().split()))
k=int(input())
while k:
    j=a[n-1]
    for i in range(n-2,-1,-1):
        a[i+1]=a[i]
    a[0]=j
    k-=1
for i in range(0,n):
    print(a[i],end=' ')