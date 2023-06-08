s=input()
a='aeiouAEIOU'
d=[]
for i in s.split():
    d.append(i)
max=0
for i in d:
    c=0
    for j in i:
        if j in a:
            c+=1
    if c>max:
        max=c
s=0
for i in d:
    m=0
    for j in i:
        if j in a:
            m+=1
    if m==max:
        s+=1
print(s)