n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    if i==1:
        s=s+i
    for j in range(1,i):
        if i==j*j:
            s=s+i
print(s)
        