b,c=map(int,input().split())
co=0
a=list(map(int,input().split()))
l,k=[],[]
for i in a:
    l.append((abs(i)))
for m in l:
    k.append(str(m))
for h in k:
    if len(h)==c:
        co+=1
    else:
        pass
print(co)