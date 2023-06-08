s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
b=[]
for i in s1:
    if i in s2:
        if i==' ':
            continue
        if ord(i) not  in b:
            b.append(ord(i))
            c+=1
if c==0:
    print(-1)
else:
    b.sort()
    for i in b:
        print(chr(i),end='')