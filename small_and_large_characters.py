s1=input()
d=[]
for i in s1.split():
        d.append(i)
for i in d:
    print(min(i),max(i),end=' ')