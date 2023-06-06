s=input()
d=[]
for i in s:
    if i=='.':
        d.append('[.]')
    else:
        d.append(i)
for i in d:
    print(i,end='')