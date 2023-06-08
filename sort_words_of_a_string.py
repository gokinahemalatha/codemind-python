s=input()
d=s.split()
for i in d:
    b=[]
    for j in i:
        if j.isalpha():
            b.append(j)
    b.sort()
    x=0
    for k in range(len(i)):
        if i[k].isalpha():
            print(b[x],end='')
            x+=1
        else:
            print(i[k],end='')
    print(end=' ')