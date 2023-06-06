s=input()
f=0
for i in s:
    if s.count(i)>1:
        f=1
        break
if f==0:
    print(-1)
else:
    b=[]
    for i in s:
        if s.count(i) not in b:
             b.append(s.count(i))
    b.sort()
    m=b[-2]
    for i in s:
        if s.count(i)==m:
            print(i,end=' ')
            break