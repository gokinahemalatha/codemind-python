s=input()
d=[]
for i in s.split():
    d.append(i)
max=0
for i in d:
    if len(i)>max:
        max=len(i)
print(max)