n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(0,n):
    p=1
    for j in range(0,n):
        if a[i]==a[j]:
            continue
        else:
            p=p*a[j]
    b.append(p)
print(*b)    