n=int(input())
a=list(map(int,input().split()))
m=0
for i in a:
    if a.count(i)>m:
        m=a.count(i)
b=[]
for i in a:
    if a.count(i)==m:
        b.append(i)
print(min(b))