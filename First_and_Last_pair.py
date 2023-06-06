n=int(input())
a=list(map(int,input().split()))
x=0
k=len(a)-1
b=[]
while(x<k):
    b.append(a[x])
    b.append(a[k])
    x+=1
    k-=1
if n%2==0:
    print(*b)
else:
    b.append(a[(n//2)])
    b.append(0)
    print(*b)