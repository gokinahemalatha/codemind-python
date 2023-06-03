t=int(input())
while(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(0,n):
        s1=sum(a[:i])
        s2=sum(a[i+1:])
        if s1==s2:
            c+=1
    if c==0:
        print("NO")
    else:
        print("YES")
    t-=1