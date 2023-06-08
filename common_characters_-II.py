s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
b=[]
for i in s1:
    if i in s2:
        if i==' ':
           continue
        if ord(i) not in b:
            b.append(ord(i))
print(len(b))