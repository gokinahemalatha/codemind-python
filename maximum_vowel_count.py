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
print(max)