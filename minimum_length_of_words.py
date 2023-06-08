s=input()
d=[]
for i in s.split():
    d.append(i)
min=999
for i in d:
    if len(i)<min:
        min=len(i)
print(min)