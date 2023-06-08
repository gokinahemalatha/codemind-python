s=input()
d=[]
for i in s.split():
    d.append(i)
l=[]
c=-1
for i in d:
    c+=1
    if c%2==0:
        l.append(i[::-1])
    else:
        l.append(i)
print(*l)