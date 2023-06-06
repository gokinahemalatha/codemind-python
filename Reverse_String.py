s=input()
d=[]
for i in s.split():
    d.append(i)
print(*d[::-1])