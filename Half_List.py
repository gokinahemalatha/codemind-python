n=int(input())
a=list(map(int,input().split()))
m=n//2
for i in range(n-1,m-1,-1):
    print(a[i],end=' ')
for i in range(0,m):
    print(a[i],end=' ')