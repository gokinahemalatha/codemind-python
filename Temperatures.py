n=int(input())
a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            c+=1
            b.append(c)
            break
        else:
            c+=1
            if j==n-1:
                c=0
                b.append(c)
                break
    print(c,end=' ')
        