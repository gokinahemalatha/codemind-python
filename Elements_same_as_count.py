n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
   if i not in b and a.count(i)==i:
       b.append(i)
       c+=1
if c==0:
    print(-1)
else:
    print(*b)