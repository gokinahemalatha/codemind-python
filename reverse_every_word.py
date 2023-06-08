s=input()
d=[]
for i in s.split():
    d.append(i)
for i in d:
    print(i[::-1],end=' ')