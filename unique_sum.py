n=int(input())
a=list(map(int,input().split()))
b=[]
s=0
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    s=s+i
print(s)