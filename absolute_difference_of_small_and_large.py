s=input()
d=[]
for i in s.split():
    d.append(i)
for i in d:
    m=ord(min(i))
    n=ord(max(i))
    print(abs(m-n),end=' ')