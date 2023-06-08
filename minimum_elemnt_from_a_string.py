s1=input()
s2=s1.split(' ')
s=s2[-1]
b=[]
for i in s:
    b.append(ord(i))
c=min(b)
m=chr(c)
if m.lower() in s:
    print(m.lower())
else:
    print(m)