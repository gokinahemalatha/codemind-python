n=int(input())
a=list(map(int,input().split()))
c=0
if a[0]<a[1]:
    b=[]
    e=[]
    for i in range(len(a)):
        if i%2!=0:
            b.append(a[i])
        else:
            e.append(a[i])
    for i in range(len(b)):
        if b[i]<e[i]:
            c=1
            break
    if c==0:
        print('yes')
    else:
        print('no')
elif a[0]>a[1]:
    b=[]
    e=[]
    for i in range(len(a)):
        if i%2!=0:
            b.append(a[i])
        else:
            e.append(a[i])
    for i in range(len(b)):
        if b[i]>e[i]:
            c=1
            break
    if c==0:
        print('yes')
    else:
        print('no')