n=int(input())
a=list(map(int,input().split()))
c=0
s=0
for i in a:
    if i%2!=0:
        s+=1
for i in range(0,n):
    if a[i]%2!=0 and i%2!=0:
        c+=1
if s==c:
    print('True')
else:
    print('False')