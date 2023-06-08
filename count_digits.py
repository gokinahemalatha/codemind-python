b=int(input())
a=list(map(int,input().split()))
l,k=[],[]
for i in a:
    l.append((abs(i)))
for m in l:
    k.append(str(m))
for j in k:
    print(len(j),end=" ")