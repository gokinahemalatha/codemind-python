s=input()
d=[]
a='aeiouAEIOU'
for i in s.split():
    d.append(i)
l=[]
for i in d:
    c=0
    for j in i:
        if j in a:
            c+=1
    l.append(c)
print(*l)