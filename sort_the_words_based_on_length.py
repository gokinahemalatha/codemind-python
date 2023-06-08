s=input()
d=s.split()
for i in range(len(d)):
    for j in range(i+1,len(d)):
        if len(d[i])>len(d[j]):
            t=d[i]
            d[i]=d[j]
            d[j]=t
        if len(d[i])==len(d[j]):
            d.sort()
        break
    break
print(*d)