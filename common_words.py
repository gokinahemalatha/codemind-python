s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
b=[]
for i in s2.split():
    if i in s1.split():
        if i==' ':
            continue
        b.append(i)
        c+=1
if c==0:
    print(-1)
else:
    print(*b)