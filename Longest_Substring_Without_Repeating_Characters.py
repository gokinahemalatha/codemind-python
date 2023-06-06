s=input()
b=[]
m=3
c=0
for i in range(len(s)):
    if s[i] not in b and (s[i].upper() not in b):
        b.append(s[i])
    else:
        if len(b)>=m:
            m=len(b)
            l=""
            for j in b:
                l+=j
            c+=1
        b=[]
        b.append(s[i])
if c==0:
    print(-1)
else:
    print(l)