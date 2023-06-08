s=input()
d=[]
for i in s.split():
    d.append(i)
print(min(d[0]),max(d[-1]),end=' ')