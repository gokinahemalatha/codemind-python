from itertools import permutations
n,k=map(int,input().split())
s=" "
for i in range(1,n+1):
    s=s+str(i)
l=permutations(s)
c=0
for i in list(l):
    c+=1
    if(c==k):
        m=i
        break
d=" "
for i in m:
    d=d+str(i)
print(int(d))