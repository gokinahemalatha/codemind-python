n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    b.append(i*i)
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            t=b[i]
            b[i]=b[j]
            b[j]=t
print(*b)