s=input().lower()
v='aeiou'
b=[]
for i in s:
    if i in v:
        b.append('V')
    else:
        b.append('C')
n=len(b)
if n<2:
    s1=""
    for i in b:
        s1+=i
    print(s1)
else:
    j=0
    for i in range(n):
        if b[j]!=b[i]:
            j+=1
            b[j]=b[i]
    j+=1
    b=b[:j]
    s1=""
    for i in b:
        s1+=i
    print(s1)