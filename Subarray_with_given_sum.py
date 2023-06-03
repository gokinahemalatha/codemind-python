n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    k=0
    for i in range(len(x)):
        s=0
        e=[]
        e.append(i+1)
        for j in range(i,len(x)):
            s=s+x[j]
            if s==b:
                e.append(j+1)
                break
            if s>b:
                break
        if len(e)==2:
            print(*e)
            k=2
            break
    if k==0:
        print(-1)