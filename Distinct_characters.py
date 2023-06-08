s=input()
s=s.lower()
b=[]
for i in s:
    if i==' ':
        continue
    if ord(i) not in b:
        b.append(ord(i))
b.sort()
for i in b:
    print(chr(i),end='')