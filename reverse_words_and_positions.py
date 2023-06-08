s=input()
d=[]
for i in s.split():
    d.append(i[::-1])
print(*d[::-1])