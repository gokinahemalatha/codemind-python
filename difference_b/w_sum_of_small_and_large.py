s=input()
m=0
n=0
d=[]
for i in s.split():
    d.append(i)
for i in d:
    m=m+ord(max(i))
    n=n+ord(min(i))
print(m-n)