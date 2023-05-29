m=int(input())
n=int(input())
a=[]
for i in range(m,n+1):
    a.append(i)
c=0
for i in range(len(a)):
    if a[i]%2!=0:
        c+=1
    s=a[i]
    for j in range(i+1,len(a)):
        s=s+a[j]
        if s%2!=0:
            c+=1
print(c)