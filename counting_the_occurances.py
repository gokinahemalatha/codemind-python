s=input()
n=input()
c=0
for i in s:
    if i==n:
        c+=1
if c==0:
    print(-1)
else:
    print(c)