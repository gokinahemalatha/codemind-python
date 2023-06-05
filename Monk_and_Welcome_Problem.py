n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            c.append(a[i]+b[j])
print(*c)