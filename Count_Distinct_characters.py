s=input()
s=s.lower()
b=[]
for i in s:
    if i==' ':
        continue
    if ord(i) not in b:
        b.append(ord(i))
b.sort()
c=0
for i in b:
    c+=1
print(c)