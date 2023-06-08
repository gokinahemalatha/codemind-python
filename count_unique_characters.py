s=input()
c=[]
d=0
m=s.lower()
for i in m:
    if i==' ':
        continue
    if m.count(i)==1:
        c.append(i)
        d+=1
print(d)