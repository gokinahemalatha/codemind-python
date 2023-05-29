n=int(input())
l=list(map(int,input().split()))
s=sorted(l)
a=len(s)-2
b=[]
while(a>=0):
    b.append(s[a])
    b.append(s[a+1])
    if a==1:
        break
    a-=2
while(a>0):
    b.append(s[a-1])
    a-=1
print(*b)