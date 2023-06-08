s=input()
c=0
b=[]
a='AEIOUaeiou'
for i in s:
    if i in a:
        b.append(i)
        c+=1
if c==0:
    print(-1)
else:
    l=[]
    for i in b:
        if i not in l:
            l.append(i)
    print(*l)