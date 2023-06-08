a=list(map(str,input().lower().split()))
j=''.join(a)
l=[]
for i in j:
    if j.count(i)==1:
        l.append(i)
q=sorted(l)
x=''.join(q)
print(x)