a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
s=0
for i in range(len(a)):
    for j in range(len(b)):
        if i==j:
            if a[i]>b[j]:
                c+=1
            if a[i]<b[j]:
                s+=1
print(c,s,end=' ')