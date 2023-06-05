t=int(input())
while(t):
    n=int(input())
    a=[]
    while(n):
        d=n%10
        a.append(d)
        n=n//10
    b=[]
    l=min(a)
    for i in range(len(a)):
        b.append(l)
        l+=1
    c=0
    for i in a:
        if i not in b:
            c=1
            break
    if c==1:
        print("NO")
    else:
        print("YES")
    t-=1