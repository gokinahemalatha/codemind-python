T=int(input())
while(T>0):
    n=int(input())
    s=input()
    d=0
    for i in s:
        if s.count(i)==1:
            c=i
            break
        else:
            d+=1
    if d==n:
        print(-1)
    else:
        print(c)
    T-=1
