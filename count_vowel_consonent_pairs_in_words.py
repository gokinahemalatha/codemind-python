s=input()
d=s.split()
m='aeiouAEIOU'
c=0
for i in d:
    j=0
    k=len(i)-1
    while j<k:
        if (i[j] in m and i[k] not in m) or (i[j] not in m and i[k] in m):
            c+=1
        j+=1
        k-=1
            
print(c)