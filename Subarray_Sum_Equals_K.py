m,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(len(a)):
    c=a[i]
    if c==k:
        s+=1
    else:
        for j in range(i+1,len(a)):
            c=c+a[j]
            if (c==k):
                s+=1
                break
print(s)