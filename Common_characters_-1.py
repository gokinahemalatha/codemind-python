s1=input().lower()
s=s1.split()
d=list(s[0])
s.remove(s[0])
m=len(s)
b=""
l=0
for i in d:
    c=0
    for j in range(m):
        if i in s[j]:
            c+=1
    if c==m:
        b+=i
        l+=1
if l==0:
    print(-1)
else:
    print(b)