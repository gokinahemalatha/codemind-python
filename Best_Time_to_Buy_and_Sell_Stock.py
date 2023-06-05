n=int(input())
a=list(map(int,input().split()))
m=n//2
min=999
for i in range(m+1):
    if a[i]<min:
        min=a[i]
max=0
for i in range(m,n):
    if a[i]>max:
        max=a[i]
if(max-min)>0:
    print(max-min)
else:
    print(0)