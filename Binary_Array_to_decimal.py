n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n-1,-1,-1):
    c=n-i-1
    while a[i]:
        s=s+(2**c)*a[i]
        a[i]=a[i]//10
print(s)