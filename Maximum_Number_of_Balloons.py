s=input()
c=0
b=[]
l=[]
for i in s:
    b.append(i)

l.append(b.count('b'))
l.append(b.count('a'))
l.append(b.count('l')//2)
l.append(b.count('o')//2)
l.append(b.count('n'))
print(min(l))