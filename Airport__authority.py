s=int(input())
a=[]
c=0
for t in range(s):
    n=int(input())
    a.append(n)
T=int(input())
for i in range(len(a)):
    if a[i]>T:
        c=c+2
    else:
        c=c+1
print(c)