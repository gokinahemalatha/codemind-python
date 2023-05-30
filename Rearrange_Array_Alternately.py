t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=a[::-1]
    c=[]
    if(len(a)%2==0):
        for i in range((len(a)//2)):
            c.append(b[i])
            c.append(a[i])
        print(*c)
    else:
        for i in range((len(a)//2)):
            c.append(b[i])
            c.append(a[i])
        print(*c,end=' ')
        print(a[(n-1)//2])