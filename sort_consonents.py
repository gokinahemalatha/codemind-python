s=input()
d=s.split()
m='aeiouAEIOU'
for i in d:
    b=[]
    for j in i:
        if j  not in m:
             b.append(j)
    b.sort()
    x=0
    for k in range(len(i)):
        if i[k] not in m:
            print(b[x],end='')
            x+=1
        else:
            print(i[k],end='')
    print(end=' ')